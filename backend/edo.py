import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation
def f(t, y):
    return y - t**2 + 1

# Define the initial conditions
t0 = 0
y0 = 0.5

# Define the step size and number of steps
h = 0.1
n = 10

# Initialize the arrays for t and y
t = np.zeros(n+1)
y = np.zeros(n+1)

# Set the initial values
t[0] = t0
y[0] = y0

# Use the Euler method to solve the differential equation
for i in range(n):
    y[i+1] = y[i] + h*f(t[i], y[i])
    t[i+1] = t[i] + h

def calcEDO(ti,yi,size, steps):
    t = np.zeros(steps+1)
    y = np.zeros(steps+1)
    t[0] = ti
    y[0] = yi
    for i in range(steps):
        y[i+1] = y[i] + size*f(t[i], y[i])
        t[i+1] = t[i] + size

# Plot the results
plt.plot(t, y, 'b')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Euler Method')
plt.show()

"""In this example, the differential equation is defined in the function f(t, y). The initial conditions are defined as t0 and y0. The step size h and number of steps n are also defined. The arrays for t and y are initialized with zeros, and the initial values are set. The Euler method is then used to solve the differential equation, and the results are plotted using Matplotlib."""