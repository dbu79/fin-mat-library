import numpy as np
import matplotlib.pyplot as plt

class JumpDiffusion:
    """Jump Diffusion process."""
    def __init__(self, S0: float, mu: float, sigma: float, lambda_j: float, mu_j: float, sigma_j: float):
        self.S0 = S0
        self.mu = mu
        self.sigma = sigma
        self.lambda_j = lambda_j
        self.mu_j = mu_j
        self.sigma_j = sigma_j

    def sim_paths(self, T: float, dt: float, n_paths: int) -> np.ndarray:
        n_steps = int(T / dt)
        paths = np.zeros((n_paths, n_steps + 1))
        paths[:, 0] = self.S0

        dW = np.random.normal(0, np.sqrt(dt), (n_paths, n_steps))

        n_jumps = np.random.poisson(self.lambda_j * dt, (n_paths, n_steps))
        jump_mean = n_jumps * self.mu_j
        jump_std = np.sqrt(n_jumps) * self.sigma_j
        log_jumps = np.random.normal(jump_mean, np.where(jump_std > 0, jump_std, 1e-12))
        log_jumps = np.where(n_jumps > 0, log_jumps, 0)



        for i in range(1, n_steps + 1):
            paths[:, i] = paths[:, i-1] * np.exp(
                (self.mu - 0.5*self.sigma**2)*dt + self.sigma*dW[:, i-1] + log_jumps[:, i-1]
            )
        return paths
        
    def plot_paths(self, paths, title='Jump Diffusion Simulated Paths', xlabel='Steps', ylabel='Price', average=True, largest=True, smallest=True):
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
