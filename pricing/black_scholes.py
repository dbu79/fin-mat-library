from option import Option
import numpy as np
from scipy.stats import norm

class BlackScholesPricer:
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
    def delta(option: Option):
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
    def gamma(option: Option):
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        sigma = option.sigma

        d1 = (np.log(S / K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
        return norm.pdf(d1)/(S * sigma * np.sqrt(T))

    @staticmethod
    def vega(option: Option):
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        sigma = option.sigma

        d1 = (np.log(S / K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
        return S * norm.pdf(d1) * np.sqrt(T)
    
    @staticmethod
    def theta(option: Option):
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
            return base_theta - (r * K * np.exp(-r * T) * norm.cdf(d2))
        elif opt_type == 'put':
            return base_theta + (r * K * np.exp(-r * T) * norm.cdf(-d2))
        else:
            raise ValueError("Valid types are 'call' and 'put'")
    
    @staticmethod
    def rho(option: Option):
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        sigma = option.sigma
        opt_type = option.opt_type

        d1 = (np.log(S / K) + (r + (sigma**2)/2)*T)/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)

        if opt_type == 'call':
            return K * T * np.exp(-r*T) * norm.cdf(d2)
        elif opt_type == 'put':
            return -K * T * np.exp(-r * T) * norm.cdf(-d2)
        else:
            raise ValueError("Valid types are 'call' and 'put'")
        
    @staticmethod
    def implied_volatility(market_price, option: Option, tol=1e-6, max_iter=100):
        S = option.S
        K = option.K
        T = option.T
        r = option.r
        opt_type = option.opt_type

        if T <= 0 or S <= 0 or K <= 0 or market_price <= 0:
            return np.nan

        sigma = np.sqrt(2 * np.pi / T) * (market_price / S)
        sigma = max(sigma, 0.001)

        for _ in range(max_iter):
            temp_option = Option(S, K, T, r, sigma, opt_type=opt_type)
            price = BlackScholesPricer.price(temp_option)
            vega = BlackScholesPricer.vega(temp_option)

            if abs(price - market_price) < tol:
                return sigma
            
            if abs(vega) < 1e-8:
                return np.nan

            sigma_new = sigma - (price - market_price) / vega
            if not np.isfinite(sigma_new) or sigma_new <= 0 or sigma_new > 5:
                return np.nan
            
            sigma = sigma_new
        return np.nan