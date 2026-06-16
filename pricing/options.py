import numpy as np
from scipy.stats import norm

class Option:
    def __init__(self, S, K, T, r, sigma, style='european', opt_type='call'):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.style = style
        self.type = opt_type
        return 

    def price(self):
        if self.style == 'european':
            return self.price_european()
        elif self.style == 'asian': 
            return self.price_asian()
        elif self.style == 'american':
            return self.price_american()
        

    def price_european(self):
        # Black-Scholes for European Options
        d1 = (np.log(self.S / self.K) + (self.r + (self.sigma**2)/2)*self.T)/(self.sigma*self.T**0.5)
        d2 = d1 - self.sigma*(self.T**0.5)

        call_option = self.S * norm.cdf(d1) - self.K*np.exp(-self.r*self.T)*norm.cdf(d2)
        put_option = self.K*np.exp(-self.r*self.T)*norm.cdf(-d2) - self.S*norm.cdf(-d1)

        if self.opt_type == 'call':
            return call_option
        elif self.opt_type == 'put':
            return put_option 
        else:
            print("Valid types are: 'call' and 'put'")


    def price_asian(self, n_paths = 10000, n_steps = 252):
        # Monte Carlo for Arithmetic Asian Options, default 10,000 paths 
        dt = self.T / n_steps
        z = np.random.standard_normal((n_paths, n_steps))
        log_returns = (self.r - 0.5 * self.sigma**2) * dt + self.sigma * np.sqrt(dt) * z 

        log_paths = np.cumsum(log_returns, axis=1)
        paths = self.S * np.exp(log_paths)
        avg_prices = paths.mean(axis=1)
        
        if self.type == 'call':
            payoffs = np.maximum(avg_prices - self.K, 0)
            return np.exp(-self.r * self.T) * payoffs.mean()
        elif self.type == 'put':
            payoffs = np.maximum(self.K - avg_prices, 0)
            return np.exp(-self.r * self.T) * payoffs.mean()
        else:
            print("Valid types are: 'call' and 'put'")

    def price_american(self):
        pass 

