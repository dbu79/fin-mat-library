import numpy as np

class BinomialTreePricer:
    def __init__(self, S0, K, T, r, u, d, opt_style='american', opt_type='call', n_steps=100):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.u = u
        self.d = d # d = 1/u
        self.opt_style = opt_style
        self.opt_type = opt_type
        self.n_steps = n_steps
    
    def price(self):
        if self.opt_style == 'american':
            return self.price_american()
        
    def price_american(self):
        dt = self.T / self.n_steps
        q = (np.exp(self.r * dt) - self.d) / (self.u - self.d)
        discount = np.exp(-self.r * dt)

        # Initialize asset prices at maturity
        asset_prices = np.zeros(self.n_steps + 1)
        for i in range(self.n_steps + 1):
            asset_prices[i] = self.S0 * (self.u ** i) * (self.d ** (self.n_steps - i))
        
        # Option payoffs at maturity
        option_values = np.zeros(self.n_steps + 1)
        for i in range(self.n_steps + 1):
            if self.opt_type == 'call':
                option_values[i] = np.maximum(asset_prices[i] - self.K, 0)
            else:
                option_values[i] = np.maximum(self.K - asset_prices[i], 0)

        # Step back through the tree
        for i in np.arange(self.n_steps - 1, -1, -1):
            for j in range(i + 1):
                option_values[j] = discount * (q * option_values[j + 1] + (1 - q) * option_values[j])
                asset_price = self.S0 * (self.u ** j) * (self.d ** (i - j))
                if self.opt_type == 'call':
                    option_values[j] = np.maximum(option_values[j], asset_price - self.K)
                else:
                    option_values[j] = np.maximum(option_values[j], self.K - asset_price)
        return option_values[0]
    