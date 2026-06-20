import numpy as np 
import pandas as pd
from options import Option


class OptionChain:
    def __init__(self, data, strike_col, price_col, dte_col):
        # Rename inputted df so class methods can work
        self.data = data
        self.data = data.rename(
            columns={
                strike_col: "strike", 
                price_col: "lastPrice", 
                dte_col: "dte"
            }
        )

    def implied_volatilities(self, S, r, opt_type='call'):
        ivs = []
        
        for _, row in self.data.iterrows():
            iv = Option.implied_volatility(
                market_price=row['lastPrice'],
                S=S,
                K=row['strike'],
                T=row['dte']/365,
                r=r,
                opt_type=opt_type
            )
            ivs.append(iv)
        self.data['iv'] = ivs

        return self.data
