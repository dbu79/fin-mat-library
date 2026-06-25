import numpy as np
import matplotlib.pyplot as plt 

class GeometricBrownianMotion:
    def __init__(self, S0, mu, sigma, T, dt):
        self.S0 = S0
        self.mu = mu 
        self.sigma = sigma
        self.T = T
        self.dt = dt

    def sim_paths(self, T, dt, n_paths):
        n_steps = int(self.T / self.dt)
        paths = np.zeros((n_paths, n_steps + 1))
        paths[:, 0] = self.S0

        dW = np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))

        for i in range(1, n_steps + 1):
            paths[:, i] = paths[:, i-1] * np.exp(
                (self.mu - 0.5*self.sigma**2)*dt + self.sigma*dW[:, i-1]
            )
        return paths

    def plot_paths(self, n_paths, title='GBM Simulated Paths', xlabel='Steps', ylabel='Price', average=True, largest=True, smallest=True):
        
        paths = self.sim_paths(self.T, self.dt, n_paths)
        fig, ax = plt.subplots()
        
        for path in paths:
            ax.plot(path, color='#1f77b4', linewidth=0.75, alpha=0.5)
        
        average_ = np.mean(paths, axis=0)
        largest_ = np.max(paths, axis=0)
        smallest_ = np.min(paths, axis=0)
        if average:
            ax.plot(average_, color='purple', linewidth=0.8, alpha=0.4)
        if largest:
            ax.plot(largest_, color='green', linewidth=0.8, alpha=0.4)
        if smallest:
            ax.plot(smallest_, color="red", linewidth=0.8, alpha=0.4)

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.show()
