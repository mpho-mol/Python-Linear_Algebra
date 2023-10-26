import numpy as np
import matplotlib.pyplot as plt

# Create variables
start_val = 0
stop_val = 100
n_samples = 200

# Create vector containing values between 0-100 in intervals of 0.5
X = np.linspace(start_val, stop_val, n_samples)

params = np.array([2, -5])

# Code for applying f(x) on vector X
f_X = params[0] * X + params[1]    # Adding because params[0] is -5(negative value)

# Plot f(X)
plt.plot(X, f_X)
plt.title("f(x) = 2x - 5")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.show()
plt.savefig("figure.png")