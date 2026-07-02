import numpy as np 
import matplotlib.pyplot as plt

class OrnsteinUhlenbeck:
    """Ornstein-Uhlenbeck (OU) process."""
    def __init__(self, X0: float, theta: float, mu: float, sigma: float, T: float, dt: float):
        self.X0 = X0
        self.theta = theta
        self.mu = mu 
        self.sigma = sigma
        self.T = T
        self.dt = dt

    def process(self, n_paths: int) -> np.ndarray:
        n_steps = int(self.T / self.dt)

        paths = np.zeros((n_paths, n_steps + 1))
        paths[:, 0] = self.X0

        dW = np.random.normal(0, np.sqrt(self.dt), (n_paths, n_steps))
        for i in range(1, n_steps + 1):
            paths[:, i] = paths[:, i-1] + self.theta * (self.mu - paths[:, i-1]) * self.dt + self.sigma * dW[:, i-1]
            

        return paths
    
    def plot_paths(self, paths, title='Ornstein-Uhlenbeck Simulated Paths', xlabel='Steps', ylabel='Value', average=True, largest=True, smallest=True):
        fig, ax = plt.subplots()
        for path in paths:
            ax.plot(path, color='#1f77b4', linewidth=0.8, alpha=0.5)
        
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

