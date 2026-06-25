class Option: 
    def __init__(self, S, K, T, r, sigma, opt_type='call'):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.opt_type = opt_type

