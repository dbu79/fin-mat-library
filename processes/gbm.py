import numpy as np

class GeometricBrownianMotion:
    def __init__(self, S0, mu, sigma):
        self.S0 = S0
        self.mu = mu 
        self.sigma = sigma

    def sim_paths(self, T, dt, n_paths):
        n_steps = int(T / dt)
        paths = np.zeros((n_paths, n_steps + 1))
        paths[:, 0] = self.S0

        dW = np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))

        for i in range(1, n_steps + 1):
            paths[:, i] = paths[:, i-1] * np.exp(
                (self.mu - 0.5*self.sigma**2)*dt + self.sigma*dW[:, i-1]
            )
        return paths

