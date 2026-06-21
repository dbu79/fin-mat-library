import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

class GeometricBrownianMotion:
    def sim_path(S, mu, sigma, T, dt, n):
        paths = []

        for i in range(n):
            prices = [S]
            time = 0 

            while time + dt <= T:
                prices.append(prices[-1]*np.exp((mu - 0.5*(sigma**2))*dt + sigma*np.random.normal(0, np.sqrt(dt))))
                time += dt 

            if T - time > 0:
                prices.append(prices[-1]*np.exp((mu - 0.5*(sigma**2))*dt + sigma*np.random.normal(0, np.sqrt(T-time))))

        
            paths.append(prices)
        return paths


S = 100 
mu = 0.08
sigma = 0.3 
T = 1
dt = 1/252
n = 100
sample_paths = GeometricBrownianMotion.sim_path(S, mu, sigma, T, dt, n)
for path in sample_paths:
    plt.plot(path)

plt.show()