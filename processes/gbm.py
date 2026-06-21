import numpy as np

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
                prices.append(prices[-1]*np.exp((mu - 0.5*(sigma**2))*(T - time) + sigma*np.random.normal(0, np.sqrt(T-time))))

        
            paths.append(prices)
        return paths
