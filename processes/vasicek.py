import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class VasicekModel:
    def __init__(self, theta, mu, sigma, r0, T, dt):
        self.theta = theta
        self.mu = mu
        self.sigma = sigma
        self.r0 = r0
        self.T = T
        self.dt = dt
    
    def rates(self):
        # Euler-Maruyama method for simulating the Vasicek model
        n_steps = int(self.T / self.dt)
        rates = np.zeros(n_steps + 1)
        rates[0] = self.r0

        for t in range(1, n_steps + 1):
            dr = self.theta * (self.mu - rates[t - 1]) * self.dt + self.sigma * np.sqrt(self.dt) * np.random.normal()
            rates[t] = rates[t - 1] + dr
        return rates
    
    def mc_sim(self, n_paths):
        # Monte Carlo simulation for the Vasicek model
        n_steps = int(self.T / self.dt)
        all_sims = np.zeros((n_steps + 1, n_paths))

        for i in range(n_paths):
            all_sims[:, i] = self.rates()
            
        return pd.DataFrame(
            all_sims, 
            columns=[f'Simulation {i + 1}' for i in range(n_paths)]
            )
        
    def plot_paths(self, df, title='Simulated Vasicek Interest Rate Paths', xlabel='Time', ylabel='Interest Rate', average=True, largest=True, smallest=True): 
        n_steps = int(self.T / self.dt)
        time_points = np.linspace(0, self.T, n_steps + 1)
        
        fig, ax = plt.subplots()
        for col in df.columns:
            ax.plot(time_points, df[col], color='#1f77b4', linewidth=0.8, alpha=0.5)

        average_ = df.mean(axis=1)
        largest_ = df.max(axis=1)
        smallest_ = df.min(axis=1)
        if average:
            ax.plot(time_points, average_, color='purple', linewidth=0.8, alpha=0.5)
        if largest:
            ax.plot(time_points, largest_, color='green', linewidth=0.8, alpha=0.5)
        if smallest:
            ax.plot(time_points, smallest_, color="red", linewidth=0.8, alpha=0.5)

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_xlim(0, self.T)
        plt.show()

