class Option:
    """European option contract with Black-Scholes-style parameters."""

    VALID_TYPES = ('call', 'put')

    def __init__(self, S: float, K: float, T: float, r: float, sigma: float, opt_type: str = 'call'):
        if S <= 0:
            raise ValueError("Spot price must be greater than 0")
        if K <= 0:
            raise ValueError("Strike price must be greater than 0")
        if T < 0:
            raise ValueError("Time to expiry must be non-negative")
        if sigma <= 0:
            raise ValueError("Sigma must be greater than 0")
        if opt_type not in self.VALID_TYPES:
            raise ValueError(f"opt_type must be one of {self.VALID_TYPES}")

        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.opt_type = opt_type