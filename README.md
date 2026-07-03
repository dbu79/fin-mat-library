# Financial Math Library

A Python library for pricing derivatives, simulating stochastic processes, and analyzing fixed income instruments.

## Features

- **Options Pricing**
  - Black-Scholes analytical pricing
  - Heston stochastic volatility model
  - Monte Carlo simulation
  - Binomial/trinomial trees
  - Implied volatility calculation

- **Stochastic Processes**
  - Arithmetic Brownian Motion (ABM)
  - Geometric Brownian Motion (GBM)
  - Cox-Ingersoll-Ross (CIR)
  - Ornstein-Uhlenbeck (OU)
  - Vasicek
  - Jump diffusion (Merton)

- **Fixed Income**
  - Bond pricing and yield curve tools

- **Portfolio**
  - Risk and performance metrics

## Project Structure

```
fixed_income/
    fixed_income.py        # Fixed income pricing and analytics

options/
    iv.py                  # Implied volatility solver
    option.py              # Option contract definitions

portfolio/
    metrics.py             # Portfolio risk/performance metrics

pricing/
    black_scholes.py       # Black-Scholes model
    heston.py               # Heston stochastic volatility model
    monte_carlo.py          # Monte Carlo pricing engine
    trees.py                 # Binomial/trinomial tree pricing

processes/
    abm.py                  # Arithmetic Brownian Motion
    cir.py                    # Cox-Ingersoll-Ross process
    gbm.py                   # Geometric Brownian Motion
    jump_diffusion.py        # Jump diffusion process
    ou.py                      # Ornstein-Uhlenbeck process
    vasicek.py                # Vasicek interest rate model

testing.ipynb              # Example usage and validation notebook
```

## Installation

```bash
pip install finmat
```

## Usage

See `testing.ipynb` for example workflows, including:

- Pricing European options with Black-Scholes and comparing to Monte Carlo
- Simulating asset paths with GBM, CIR, and jump diffusion processes
- Calibrating the Heston model to market data
- Computing implied volatility surfaces
- Evaluating fixed income instruments and portfolio metrics

## Requirements

- Python 3.8+
- NumPy
- SciPy
- matplotlib (for notebook visualizations)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
