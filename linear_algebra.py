import numpy as np
import matplotlib.pyplot as plt

#create variables 
start_val = 0
stop_val = 100
n_samples = 200

#create vector containing values between 0-100 in intervals of 0.5
x = np.linspace(start_val, stop_val, n_samples)

params = np.array([2, -5])

#code for applying f(x) on vector x
f_x = params[0] * x + params[1]    #adding because params[0] is -5(negative value)

#plot f(x)
plt.plot(x, f_x)
plt.title("f(x) = 2x - 5")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
