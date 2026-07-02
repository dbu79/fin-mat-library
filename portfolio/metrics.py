import numpy as np


class PortfolioMetrics:
    """Performance/risk metrics for a daily returns series."""

    def __init__(self, returns, risk_free_rate: float = 0.0):
        self.returns = np.asarray(returns, dtype=float)
        self.risk_free_rate = risk_free_rate  # annualized

    def annualized_return(self) -> float:
        return np.mean(self.returns) * 252

    def annualized_volatility(self) -> float:
        return np.std(self.returns, ddof=1) * np.sqrt(252)

    def sharpe_ratio(self) -> float:
        vol = self.annualized_volatility()
        return (self.annualized_return() - self.risk_free_rate) / vol if vol != 0 else np.inf

    def downside_deviation(self) -> float:
        daily_rf = self.risk_free_rate / 252
        downside = self.returns[self.returns < daily_rf]
        if len(downside) == 0:
            return 0.0
        return np.sqrt(np.mean((downside - daily_rf)**2)) * np.sqrt(252)

    def sortino_ratio(self) -> float:
        downside_vol = self.downside_deviation()
        if downside_vol == 0:
            return np.inf
        return (self.annualized_return() - self.risk_free_rate) / downside_vol

    def max_drawdown(self) -> float:
        """Assumes self.returns is chronologically ordered."""
        cumulative_returns = np.cumprod(1 + self.returns)
        running_max = np.maximum.accumulate(cumulative_returns)
        drawdowns = (cumulative_returns - running_max) / running_max
        return np.min(drawdowns)

    def calmar_ratio(self) -> float:
        max_dd = self.max_drawdown()
        return self.annualized_return() / abs(max_dd) if max_dd < 0 else np.inf