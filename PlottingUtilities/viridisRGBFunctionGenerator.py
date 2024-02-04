import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly


def sample_viridis(num_samples):
    colormap = plt.get_cmap('viridis')
    return [colormap(i / num_samples)[:3] for i in range(num_samples)]


def fit_polynomial(data, degree):
    x = np.linspace(0, 1, len(data))
    return poly.polyfit(x, data, degree)


# Sample the Viridis colormap
num_samples = 50
viridis_samples = sample_viridis(num_samples)

# Separate RGB channels and fit polynomials
r_samples, g_samples, b_samples = zip(*viridis_samples)
r_coeffs = fit_polynomial(r_samples, 5)  # Degree can be adjusted
g_coeffs = fit_polynomial(g_samples, 5)
b_coeffs = fit_polynomial(b_samples, 5)

print("Red coefficients:", r_coeffs)
print("Green coefficients:", g_coeffs)
print("Blue coefficients:", b_coeffs)
