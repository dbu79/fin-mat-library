from options.option import Option
import numpy as np
from scipy.stats import norm

class BlackScholesPricer:
    """Black-Scholes pricing and Greeks for European Options."""
    @staticmethod
    def price(option: Option):
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        sigma = option.sigma
        opt_type = option.opt_type

        d1 = (np.log(S / K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)

        if opt_type == 'call':
            return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
        elif opt_type == 'put':
            return K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        else:
            raise ValueError("Valid types are: 'call' and 'put'")
    
    @staticmethod
    def delta(option: Option) -> float:
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        sigma = option.sigma
        opt_type = option.opt_type

        d1 = (np.log(S / K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))

        if opt_type == 'call':
            return norm.cdf(d1)
        elif opt_type == 'put':
            return norm.cdf(d1) - 1
        else:
            raise ValueError("Valid types are: 'call' and 'put'")
    
    @staticmethod
    def gamma(option: Option) -> float:
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        sigma = option.sigma

        d1 = (np.log(S / K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
        return norm.pdf(d1)/(S * sigma * np.sqrt(T))

    @staticmethod
    def vega(option: Option) -> float:
        """Per 1% change in volatility"""
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        sigma = option.sigma

        d1 = (np.log(S / K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
        return S * norm.pdf(d1) * np.sqrt(T) / 100
    
    @staticmethod
    def theta(option: Option) -> float:
        """Per day"""
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        sigma = option.sigma
        opt_type = option.opt_type

        d1 = (np.log(S / K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)

        base_theta = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
        if opt_type == 'call':
            return (base_theta - (r * K * np.exp(-r * T) * norm.cdf(d2)))/365
        elif opt_type == 'put':
            return (base_theta + (r * K * np.exp(-r * T) * norm.cdf(-d2)))/365
        else:
            raise ValueError("Valid types are 'call' and 'put'")
    
    @staticmethod
    def rho(option: Option) -> float:
        """Per 1% change in interest rate"""
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        sigma = option.sigma
        opt_type = option.opt_type

        d1 = (np.log(S / K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)

        if opt_type == 'call':
            return K * T * np.exp(-r*T) * norm.cdf(d2) / 100
        elif opt_type == 'put':
            return -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100
        else:
            raise ValueError("Valid types are 'call' and 'put'")
        
