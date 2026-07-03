import numpy as np
import matplotlib.pyplot as plt

class ArithmeticBrownianMotion:
    """Arithmetic Brownian Motion (ABM) process."""
    def __init__(self, S0: float, mu: float, sigma: float):
        self.S0 = S0
        self.mu = mu
        self.sigma = sigma

    def sim_paths(self, dt: float, T: float, n_paths: int) -> np.ndarray:
        n_steps = int(T / dt)
        paths = np.zeros((n_paths, n_steps + 1))

        dW = np.random.normal(0, 1, (n_paths, n_steps))        
        paths[:, 0] = self.S0

        for i in range(1, n_steps + 1):
            paths[:, i] = paths[:, i-1] + self.mu*dt + self.sigma*np.sqrt(dt)*dW[:, i - 1]

        return paths
    
    def plot_paths(self, paths, title='ABM Simulated Paths', xlabel='Steps', ylabel='Price', average=True, largest=True, smallest=True):
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


