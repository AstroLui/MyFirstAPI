import numpy as np
import matplotlib.pyplot as plt

#Define la ecuacion diferencial
def f(t, y):
    return y - t**2 + 1

#ti yi definen las condiciones iniciales
#size define el tamaño de los pasos y steps define el número de pasos,
#Escoger valores más pequeños de size hará que los resultados sean más precisos y que
#el tiempo de cómputo sea mayor
def calcEDO(ti,yi,size, steps):
    # Inicializar arreglos en cero para t, y
    t = np.zeros(steps+1)
    y = np.zeros(steps+1)
    # Colocar los valores iniciales
    t[0] = ti
    y[0] = yi
    #Usar el método de Euler para resolver la ecuación diferencial
    for i in range(steps):
        y[i+1] = y[i] + size*f(t[i], y[i])
        t[i+1] = t[i] + size
    
    #Mostrar los resultados
    plt.plot(t, y, 'b')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Euler Method')
    plt.show()

calcEDO(0, 0.5, 0.1, 10)