class Option:
    def __init__(self, S, K, T, r, sigma, style='european', type='call'):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.style = 'european'
        self.type = 'call'
        return 

    def price(self):
        if self.style == 'european':
            return self.price_european()
        elif self.style == 'asian': 
            return self.price_asian()
        elif self.style == 'american':
            return self.price_american()
        

    def price_european(self):
        pass 
    def price_asian(self):
        pass
    def price_american(self):
        pass 
