class Option: 
    def __init__(self, S, K, T, r, sigma, opt_type='call'):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.opt_type = opt_type

        if self.S < 0:
            raise ValueError("Spot price must be greater than 0")
        if self.K < 0:
            raise ValueError("Strike price must be greater than 0")
        if self.T < 0:
            raise ValueError("Time to expiry must be greater than 0")
        if self.r < 0:
            raise ValueError("Sigma must be greater than 0")
        # if opt_type != "call" or opt_type != "put":
        #     raise ValueError("Option type must be 'call' or 'put'")
        