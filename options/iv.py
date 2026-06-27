import numpy as np
from copy import deepcopy
from .option import Option

class ImpliedVolatility:

    @staticmethod
    def solve(option: Option, market_price, pricer, initial=0.2, tol=1e-8, max_iter=100, h=1e-4, seed=None):
        sigma = initial
        copy_ = deepcopy(option)

        def price_at(sigma_val):
            copy_.sigma = sigma_val
            if seed is not None:
                np.random.seed(seed)
            return pricer(copy_)
        
        for _ in range(max_iter):
            model_price = price_at(sigma)
            
            if abs(model_price - market_price) < tol:
                return sigma
            
            price_up = price_at(sigma + h)
            price_down = price_at(sigma - h)
            vega = (price_up - price_down) / (2 * h)

            if abs(vega) < 1e-10 or not np.isfinite(vega):
                return np.nan
            
            sigma_new = sigma - (model_price - market_price) / vega
            if not np.isfinite(sigma_new) or sigma_new <= 0: 
                return np.nan

            sigma = sigma_new
        
        return np.nan
    
