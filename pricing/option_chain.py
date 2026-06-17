import numpy as np 
import pandas as pd
from options import Option
from scipy.stats import norm


class OptionChain:
    def __init__(self, data):
        self.data = data
    
    def implied_volatilities(self, S, r, opt_type='call'):
        ivs = []
        
        for _, row in self.data.iterrows():
            iv = Option.implied_volatility(
                market_price=row['market_price'],
                S=S,
                K=row['strike'],
                T=row['expiry']/365,
                r=r,
                opt_type=opt_type
            )
            ivs.append(iv)
        self.data['iv'] = ivs

chain = pd.DataFrame({
    "strike": [90,95,100,105,110],
    "market_price": [10,9,8,7,6],
    'expiry': [30,30,30,30,30]
})

options = OptionChain(chain)
options.implied_volatilities(100, 0.05)
print(options.data)