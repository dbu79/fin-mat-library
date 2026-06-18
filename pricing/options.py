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
        self.opt_type = opt_type

    @property
    def d1(self):
        return (np.log(self.S / self.K) + (self.r + (self.sigma**2)/2)*self.T)/(self.sigma*self.T**0.5)

    @property
    def d2(self):
        return self.d1 - self.sigma*(self.T**0.5)


    def price(self):
        if self.style == 'european':
            return self.price_european()
        elif self.style == 'asian': 
            return self.price_asian()
        elif self.style == 'american':
            return self.price_american()
        

    def price_european(self):
        # Black-Scholes for European Options
        # d1 = (np.log(self.S / self.K) + (self.r + (self.sigma**2)/2)*self.T)/(self.sigma*self.T**0.5)
        # d2 = d1 - self.sigma*(self.T**0.5)

        call_option = self.S * norm.cdf(self.d1) - self.K*np.exp(-self.r*self.T)*norm.cdf(self.d2)
        put_option = self.K*np.exp(-self.r*self.T)*norm.cdf(-self.d2) - self.S*norm.cdf(-self.d1)

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
        
        if self.opt_type == 'call':
            payoffs = np.maximum(avg_prices - self.K, 0)
            return np.exp(-self.r * self.T) * payoffs.mean()
        elif self.opt_type == 'put':
            payoffs = np.maximum(self.K - avg_prices, 0)
            return np.exp(-self.r * self.T) * payoffs.mean()
        else:
            raise ValueError("Valid types are: 'call' and 'put'")

    def price_american(self):
        pass 

    def delta(self):
        if self.opt_type == 'call':
            return norm.cdf(self.d1)
        elif self.opt_type == 'put':
            return norm.cdf(self.d1) - 1
        else:
            raise ValueError("Valid types are: 'call' and 'put'")
    
    def gamma(self):
        return norm.cdf(self.d1)/(self.S * self.sigma * np.sqrt(self.T))

    def vega(self):
        return self.S * norm.pdf(self.d1) * np.sqrt(self.T)
    
    def theta(self):
        base_theta = -(self.S * norm.pdf(self.d1) * self.sigma) / (2 * np.sqrt(self.T))
        if self.opt_type == 'call':
            return base_theta - (self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2))
        elif self.opt_type == 'put':
            return base_theta + (self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2))
        else:
            raise ValueError("Valid types are 'call' and 'put'")
        
    def rho(self):
        if self.opt_type == 'call':
            return self.K * self.T * np.exp(-self.r*self.T) * norm.cdf(self.d2)
        elif self.opt_type == 'put':
            return -self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-self.d2)
        else:
            raise ValueError("Valid types are 'call' and 'put'")

    @staticmethod
    def implied_volatility(market_price, S, K, T, r, opt_type='call', style='european', tol=1e-6, max_iter=100):
        if T <= 0 or S <= 0 or K <= 0 or market_price <= 0:
            return np.nan

        sigma = np.sqrt(2 * np.pi / T) * (market_price / S)
        sigma = max(sigma, 0.001)

        for _ in range(max_iter):
            temp_opt = Option(S, K, T, r, sigma, style=style, opt_type=opt_type)
            price = temp_opt.price_european()
            vega = temp_opt.vega()

            if abs(price - market_price) < tol:
                return sigma
            
            if abs(vega) < 1e-8:
                return np.nan

            sigma_new = sigma - (price - market_price) / vega
            if not np.isfinite(sigma_new):
                return np.nan
            if sigma_new <= 0 or sigma_new > 5:
                return np.nan
            
            sigma = sigma_new
        return np.nan 
