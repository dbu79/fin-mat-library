import numpy as np
import matplotlib.pyplot as plt

class VasicekModel:
    def __init__(self, theta, mu, sigma, r0):
        self.theta = theta
        self.mu = mu
        self.sigma = sigma
        self.r0 = r0

    def sim_paths(self, T, dt, n_paths):
        n_steps = int(T / dt)
        paths = np.zeros((n_paths, n_steps + 1))
        paths[:, 0] = self.r0

        sqrt_dt = np.sqrt(dt)
        for i in range(1, n_steps + 1):
            r_prev = paths[:, i - 1]
            z = np.random.normal(size=n_paths)
            dr = self.theta * (self.mu - r_prev) * dt + self.sigma * sqrt_dt * z
            paths[:, i] = r_prev + dr

        return paths

    def plot_paths(self, paths, T, dt, title='Simulated Vasicek Interest Rate Paths', xlabel='Time', ylabel='Interest Rate', average=True, largest=True, smallest=True):
        n_steps = int(T / dt)
        time_points = np.linspace(0, T, n_steps + 1)

        fig, ax = plt.subplots()
        for path in paths:
            ax.plot(time_points, path, color='#1f77b4', linewidth=0.75, alpha=0.5)

        average_ = np.mean(paths, axis=0)
        largest_ = np.max(paths, axis=0)
        smallest_ = np.min(paths, axis=0)
        if average:
            ax.plot(time_points, average_, color='purple', linewidth=0.8, alpha=0.4)
        if largest:
            ax.plot(time_points, largest_, color='green', linewidth=0.8, alpha=0.4)
        if smallest:
            ax.plot(time_points, smallest_, color="red", linewidth=0.8, alpha=0.4)

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_xlim(0, T)
        plt.show()