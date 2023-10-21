import numpy as np
import matplotlib.pyplot as plt

#Define la ecuación diferencial
def f(t, y):
    return y - t**2 + 1

def calcEDO(ti,yi,size, steps):
    # Initialize the arrays for t and y
    t = np.zeros(steps+1)
    y = np.zeros(steps+1)
    # Set the initial values
    t[0] = ti
    y[0] = yi
    # Use the Euler method to solve the differential equation
    for i in range(steps):
        y[i+1] = y[i] + size*f(t[i], y[i])
        t[i+1] = t[i] + size
    
    # Plot the results
    plt.plot(t, y, 'b')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Euler Method')
    plt.show()

calcEDO(0, 0.5, 0.1, 10)


"""In this example, the differential equation is defined in the function f(t, y). The initial conditions are defined as t0 and y0. The step size h and number of steps n are also defined. The arrays for t and y are initialized with zeros, and the initial values are set. The Euler method is then used to solve the differential equation, and the results are plotted using Matplotlib."""