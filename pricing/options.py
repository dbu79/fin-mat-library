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


    def price_asian(self):
        d1 = (np.log(self.S / self.K) + (self.r + (self.sigma**2)/2)*self.T)/(self.sigma*self.T**0.5)
        d2 = d1 - self.sigma*(self.T**0.5)

        

    def price_american(self):
        pass 

