import numpy as np
from options.option import Option
import matplotlib.pyplot as plt

class HestonModel:
    @staticmethod
    def price(option: Option, kappa, theta, sigma, rho, v0, n_paths=10000, n_steps=252):
        S0 = option.S
        K = option.K
        T = option.T
        r = option.r
        opt_type = option.opt_type

        dt = T / n_steps
        
        dW1 = np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))
        dW2 = rho * dW1 + np.sqrt(1 - rho**2) * np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))

        S = np.zeros((n_paths, n_steps + 1))    
        v = np.zeros((n_paths, n_steps + 1))

        S[:, 0] = S0
        v[:, 0] = v0 

        for i in range(1, n_steps + 1):
            S[:, i] = S[:, i - 1] * np.exp((r - 0.5 * v[:, i - 1]) * dt + np.sqrt(v[:, i - 1]) * dW1[:, i - 1])
            sqrt_v = np.sqrt(np.maximum(v[:, i-1], 0))
            v_next = (v[:, i-1] + kappa*(theta - v[:, i-1])*dt + sigma*sqrt_v*dW2[:, i-1])
            v[:, i] = np.maximum(v_next, 0)
        
        S_t = S[:, -1]
        payoff = np.maximum(S_t - K, 0) if opt_type == 'call' else np.maximum(K - S_t, 0)
        price = np.exp(-r * T) * np.mean(payoff)
        return price


