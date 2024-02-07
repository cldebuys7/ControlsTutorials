""" ColormapPolynomialCreator

Creates three polynomials, one for each of RGB, based on a colormap. These polynomials can be evaluated in another
method or even another programming language in order to recreate the colormap. The simplest way to evaluate the
polynomial in Python is polyval. Input to the method which evaluates the polynomial should be a scalar between 0 and 1.
"""

import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly


def sample_colormap(num_samples):
    # colormap = plt.get_cmap('viridis')
    # colormap = plt.get_cmap('PiYG')
    colormap = plt.get_cmap('coolwarm')
    return [colormap(i / num_samples)[:3] for i in range(num_samples)]


def fit_polynomial(data, degree):
    x = np.linspace(0, 1, len(data))
    return poly.polyfit(x, data, degree)


# Implement this method in another language to use the polynomial representation of the colormap in that language.
def evaluate_polynomial(coefficients, x):
    return poly.polyval(x, coefficients)


# Sample the Viridis colormap
num_samples = 50
degree = 5
viridis_samples = sample_colormap(num_samples)

# Separate RGB channels and fit polynomials
r_samples, g_samples, b_samples = zip(*viridis_samples)
r_coeffs = fit_polynomial(r_samples, degree)  # Degree can be adjusted
g_coeffs = fit_polynomial(g_samples, degree)
b_coeffs = fit_polynomial(b_samples, degree)

print("Red coefficients:", r_coeffs)
print("Green coefficients:", g_coeffs)
print("Blue coefficients:", b_coeffs)
