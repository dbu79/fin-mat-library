import numpy as np
import matplotlib.pyplot as plt 

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

    def show_paths(self, T, dt, n_paths, title='GBM Simulated Paths', xlabel='Price', ylabel='Steps', average=True, largest=True, smallest=True):
        
        paths = self.sim_paths(T, dt, n_paths)
        fig, ax = plt.subplots()
        for path in paths:
            ax.plot(path, color='#1f77b4', linewidth=0.75, alpha=0.3)
        
        average_ = np.mean(paths, axis=0)
        largest_ = np.max(paths, axis=0)
        smallest_ = np.min(paths, axis=0)
        if average:
            ax.plot(average_, color='purple', linewidth=0.8, alpha=0.5)
        if largest:
            ax.plot(largest_, color='green', linewidth=0.8, alpha=0.3)
        if smallest:
            ax.plot(smallest_, color="red", linewidth=0.8, alpha=0.3)

        ax.set_title(f"{title}")
        ax.set_xlabel(f"{xlabel}")
        ax.set_ylabel(f"{ylabel}")
        plt.show()


