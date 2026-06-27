from processes.gbm import GeometricBrownianMotion
import numpy as np
from options.option import Option

class MonteCarloPricer: 
    @staticmethod
    def price_european(option: Option, n_paths=10000, n_steps=252):
        gbm = GeometricBrownianMotion(S0=option.S, mu=option.r, sigma=option.sigma)
        paths = gbm.sim_paths(T=option.T, dt=option.T/n_steps, n_paths=n_paths)
        S_t = paths[:, -1]

        if option.opt_type == 'call':
            payoffs = np.maximum(S_t - option.K, 0)
        else:
            payoffs = np.maximum(option.K - S_t, 0)

        price = np.exp(-option.r * option.T) * np.mean(payoffs)
        return price
    
    @staticmethod
    def price_asian(option: Option, n_paths=10000, n_steps=252):
        gbm = GeometricBrownianMotion(S0=option.S, mu=option.r, sigma=option.sigma)
        paths = gbm.sim_paths(T=option.T, dt=option.T/n_steps, n_paths=n_paths)
        path_avg = np.mean(paths, axis=1)

        if option.opt_type == 'call':
            payoffs = np.maximum(path_avg - option.K, 0)
        else: 
            payoffs = np.maximum(option.K - path_avg, 0)

        price = np.exp(-option.r * option.T) * np.mean(payoffs)
        return price