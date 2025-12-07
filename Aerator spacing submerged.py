import numpy as np
import matplotlib.pyplot as plt

# Updated spacing formula
def L(W, A):
    return (128 * W) / (419 * A)

# Power range: 500 W to 3200 W in 200 W steps
W_values = np.arange(500, 3201, 200)

# Cross-sectional area: 30 to 100 m²
A_values = np.linspace(30, 100, 300)

# Plot
plt.figure(figsize=(12, 7))

for W in W_values:
    L_line = L(W, A_values)
    plt.plot(A_values, L_line, color='black')
    # Label near the end
    plt.text(A_values[-1] + 1, L_line[-1], f'{W} W',
             va='center', fontsize=8)

plt.xlabel('Cross-sectional Area A (m²)')
plt.ylabel('Aerator Spacing L (m)')
plt.title('Aerator Spacing vs. Channel Cross-sectional Area')
plt.grid(True)
plt.tight_layout()
plt.show()
