def simple_interest(P, r, t):
    return P(1 + r * t)
    
def compound_interest(P, r, n, t):
    return P((1 + r/n)**(n*t))
    
def future_value(PV, r, n):
    return PV((1 + r)**n)

def present_value(FV, r, n):
    return FV/((1 + r)**n)

def annuinity_pv(PMT, r, n):
    return PMT * ((1 + r)**n - 1) / r

def annuity_fv(PMT, r, n):
    return PMT * (1 - (1 + r)**-n)/r

def bond_price(PMT, FV, r, n, t):
    return PMT / (1 + r)**t + FV / (1 + r)**n 

def convexity(P0, pl, pm, y):
    return (pm + pl - 2*P0)/(P0 * y**2)