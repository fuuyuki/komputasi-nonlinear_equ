import numpy as np

# x = np.array([0.24, 0.65, 0.95, 1.24, 1.73, 2.01, 2.23, 2.52])
x = np.array([1, 2, 3])
y = np.array([5.1, 5.9, 6.3])

# Linear fit
coeffs_linear = np.polyfit(x, y, 1)
# Quadratic fit
# coeffs_quad = np.polyfit(x, y, 2)
# Cubic polynomial fit
# coeffs_poly3 = np.polyfit(x, y, 3)

print("Linear:", coeffs_linear)
# print("Quadratic:", coeffs_quad)
# print("Cubic:", coeffs_poly3)
