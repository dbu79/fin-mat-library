import numpy as np
import matplotlib.pyplot as plt

class CIR:
    def __init__(self, r0, a, b, sigma):
        self.r0 = r0
        self.a = a
        self.b = b
        self.sigma = sigma

    def sim_paths(self, T, dt, n_paths):
        n_steps = int(T / dt)
        paths = np.zeros((n_paths, n_steps + 1))
        paths[:, 0] = self.r0

        sqrt_dt = np.sqrt(dt)
        for i in range(1, n_steps + 1):
            r_prev = paths[:, i - 1]
            z = np.random.normal(size=n_paths)
            dr = (self.a * (self.b - r_prev) * dt
                  + self.sigma * np.sqrt(r_prev) * sqrt_dt * z)
            paths[:, i] = np.maximum(r_prev + dr, 0)

        return paths

    def plot_paths(self, paths, title='CIR Simulated Paths', xlabel='Steps', ylabel='Rate', average=True, largest=True, smallest=True):
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