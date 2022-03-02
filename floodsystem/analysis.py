import matplotlib.dates
import numpy as np

def polyfit(dates, levels, p):
    # Convert dates from datetime objects to a list of floats
    x = matplotlib.dates.date2num(dates)

    # Find coefficients of best-fit polynomial f(x) of degree p
    # Subtract constant offset from dates to avoid large numbers, which would cause error
    p_coeff = np.polyfit(x - x[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    return poly, x[0]