import numpy as np
from options.option import Option

class BinomialTreePricer:
    @staticmethod
    def price_american(option: Option, u, d, n_steps=100):
        S0 = option.S
        K = option.K
        T = option.T
        r = option.r
        opt_type = option.opt_type

        dt = T / n_steps
        q = (np.exp(r * dt) - d) / (u - d)
        discount = np.exp(-r * dt)

        asset_prices = np.zeros(n_steps + 1)
        for i in range(n_steps + 1):
            asset_prices[i] = S0 * (u ** i) * (d ** (n_steps - i))
        
        option_values = np.zeros(n_steps + 1)
        for i in range(n_steps + 1):
            if opt_type == 'call':
                option_values[i] = np.maximum(asset_prices[i] - K, 0)
            else:
                option_values[i] = np.maximum(K - asset_prices[i], 0)

        for i in np.arange(n_steps - 1, -1, -1):
            for j in range(i + 1):
                option_values[j] = discount * (q * option_values[j + 1] + (1 - q) * option_values[j])
                asset_price = S0 * (u ** j) * (d ** (i - j))
                if opt_type == 'call':
                    option_values[j] = np.maximum(option_values[j], asset_price - K)
                else:
                    option_values[j] = np.maximum(option_values[j], K - asset_price)
        return option_values[0]