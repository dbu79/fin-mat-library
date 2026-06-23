from processes.gbm import GeometricBrownianMotion
import numpy as np

class MonteCarloPricer:
    def __init__(self, S, K, T, r, sigma, opt_style='european', opt_type='call', n_paths=10000, n_steps=252):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.opt_style = opt_style
        self.opt_type = opt_type
        self.n_paths = n_paths
        self.n_steps = n_steps

        self.gbm = GeometricBrownianMotion(S0=S, mu = r, sigma=sigma)
    
    def price(self):
        if self.opt_style == 'european':
            return self.price_european()
        elif self.opt_style == 'asian':
            return self.price_asian()
        else:
            raise ValueError("Unsupported option style. Use 'european' or 'asian'.")

    def price_european(self):
        paths = self.gbm.sim_paths(T=self.T, dt=self.T/self.n_steps, n_paths=self.n_paths)
        S_t = paths[:, -1]

        if self.opt_type == 'call':
            payoffs = np.maximum(S_t - self.K, 0)
        else:
            payoffs = np.maximum(self.K - S_t, 0)

        price = np.exp(-self.r * self.T) * np.mean(payoffs)
        return price

    def price_asian(self):
        paths = self.gbm.sim_paths(T=self.T, dt=self.T/self.n_steps, n_paths=self.n_paths)
        path_avg = np.mean(paths, axis=1)

        if self.opt_type == 'call':
            payoffs = np.maximum(path_avg - self.K, 0)
        else: 
            payoffs = np.maximum(self.K - path_avg, 0)

        price = np.exp(-self.r * self.T) * np.mean(payoffs)
        return price 