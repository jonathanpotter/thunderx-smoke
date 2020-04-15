# Example Python Program with numpy and scipy
# Basic Numerical Integration: the Trapezoid Rule
# https://nbviewer.jupyter.org/github/ipython/ipython/blob/master/examples/IPython%20Kernel/Trapezoid%20Rule.ipynb

import numpy as np
from scipy.integrate import quad
#import matplotlib.pyplot as plt

# Use NumPy to define a simple function and sample it between 0 and 10 at 200 points

def f(x):
    return (x-3)*(x-5)*(x-7)+85

x = np.linspace(0, 10, 200)
y = f(x)

# Use NumPy to choose a region to integrate over and take only a few points in that region

a, b = 1, 8 # the left and right boundaries
N = 5 # the number of points
xint = np.linspace(a, b, N)
yint = f(xint)

# Draw some stuff with MatPlotLib

#plt.plot(x, y, lw=2)
#plt.axis([0, 9, 0, 140])
#plt.fill_between(xint, 0, yint, facecolor='gray', alpha=0.4)
#plt.text(0.5 * (a + b), 30,r"$\int_a^b f(x)dx$", horizontalalignment='center', fontsize=20);

# Compute the integral both at high accuracy and with the trapezoid approximation

# Use SciPy to calculate the integral
integral, error = quad(f, a, b)

# Use NumPy to calculate the area with the trapezoid approximation
integral_trapezoid = sum( (xint[1:] - xint[:-1]) * (yint[1:] + yint[:-1]) ) / 2

print("The integral is:", integral, "+/-", error)
print("The trapezoid approximation with", len(xint), "points is:", integral_trapezoid)
print("NumPy and SciPy are working!")
