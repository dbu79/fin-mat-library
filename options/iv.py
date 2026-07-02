import numpy as np
from copy import deepcopy
from .option import Option


def solve_implied_vol(option: Option, market_price, pricer, initial=0.2,
                       tol=1e-8, max_iter=100, h=1e-4, seed=None):
    """Solve for implied volatility via Newton-Raphson with numerical vega. Returns NaN if no convergence."""
    sigma = initial
    copy_ = deepcopy(option)
    rng = np.random.default_rng(seed) if seed is not None else None

    def price_at(sigma_val):
        copy_.sigma = sigma_val
        return pricer(copy_, rng=rng) if rng is not None else pricer(copy_)

    for _ in range(max_iter):
        model_price = price_at(sigma)
        if abs(model_price - market_price) < tol:
            return sigma

        vega = (price_at(sigma + h) - price_at(sigma - h)) / (2 * h)
        if abs(vega) < 1e-10 or not np.isfinite(vega):
            return np.nan

        sigma_new = sigma - (model_price - market_price) / vega
        if not np.isfinite(sigma_new) or sigma_new <= 0:
            return np.nan
        sigma = sigma_new

    return np.nan