import numpy as np

class PortfolioMetrics: 
    def __init__(self, returns, risk_free_rate=0.0):
        returns = np.asarray(returns, dtype=float)
        self.returns = returns
        self.risk_free_rate = risk_free_rate

    def annualized_return(self):
        return np.mean(self.returns) * 252
    
    def annualized_volatility(self):
        return np.std(self.returns) * np.sqrt(252)
        
    def sharpe_ratio(self):
        return (self.annualized_return() - self.risk_free_rate) / self.annualized_volatility() if self.annualized_volatility() != 0 else np.inf
    
    def sortino_ratio(self):
        daily_rf = self.risk_free_rate / 252
        excess = self.returns - daily_rf
        downside = excess[excess < 0]

        if len(downside) == 0:
            return np.inf
        
        downside_vol = np.sqrt(np.mean(downside**2)) * np.sqrt(252)
        return (self.annualized_return() - self.risk_free_rate) / downside_vol if downside_vol != 0 else np.inf
    
    def max_drawdown(self):
        cumulative_returns = np.cumprod(1 + self.returns) 
        running_max = np.maximum.accumulate(cumulative_returns)
        drawdowns = (cumulative_returns - running_max) / running_max
        return np.min(drawdowns)
    
    def calmar_ratio(self):
        max_dd = self.max_drawdown()
        return self.annualized_return() / abs(max_dd) if max_dd < 0 else np.inf

    def downside_deviation(self):
        downside = self.returns[self.returns < self.risk_free_rate]
        return np.sqrt(np.mean(downside - self.risk_free_rate)**2) if len(downside) > 0 else 0



    
