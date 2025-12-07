import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data points
X = np.array([3, 6, 24, 48, 120])
Y = np.array([5.929919137, 52.96495957, 65.76819407, 76.41509434, 89.35309973])

# Log transform
lnX = np.log(X)

# Fit: Y = a ln(X) + b
slope, intercept, r_value, p_value, std_err = linregress(lnX, Y)
R2 = r_value ** 2

# Smooth X range for smooth curve
X_smooth = np.linspace(X.min(), X.max(), 200)
lnX_smooth = np.log(X_smooth)
Y_smooth = slope * lnX_smooth + intercept

# Hypothesis statement
hypothesis = "Reject H₀: slope ≠ 0" if p_value < 0.05 else "Fail to reject H₀"

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color='blue', label='Data Points')
plt.plot(X_smooth, Y_smooth, color='red', label='Logarithmic Fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Log Regression: Y = {slope:.4f}·ln(X) + {intercept:.4f}\n'
          f'R² = {R2:.4f} | p-value = {p_value:.4f} | {hypothesis}')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
