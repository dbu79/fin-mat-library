def simple_interest(P: float, r: float, t: float) -> float:
    return P * (1 + r * t)

def compound_interest(P: float, r: float, n: int, t: float) -> float:
    return P * (1 + r/n)**(n*t)

def future_value(PV: float, r: float, n: int) -> float:
    return PV * (1 + r)**n

def present_value(FV: float, r: float, n: int) -> float:
    return FV / (1 + r)**n

def annuity_pv(PMT: float, r: float, n: int) -> float:
    return PMT * (1 - (1 + r)**-n) / r

def annuity_fv(PMT: float, r: float, n: int) -> float:
    return PMT * ((1 + r)**n - 1) / r

def bond_price(PMT: float, FV: float, r: float, n: int) -> float:
    """PMT: coupon per period, FV: face value, r: yield per period, n: number of periods"""
    coupons = sum(PMT / (1 + r)**t for t in range(1, n + 1))
    principal = FV / (1 + r)**n
    return coupons + principal

def convexity(P0: float, P_plus: float, P_minus: float, dy: float) -> float:
    """P_plus/P_minus: prices after +dy/-dy yield shock"""
    return (P_plus + P_minus - 2 * P0) / (P0 * dy**2)