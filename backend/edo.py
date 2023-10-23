import numpy as np
import matplotlib.pyplot as plt

"""
El método de Euler es un procedimiento numérico de primer orden para resolver ecuaciones diferenciales ordinarias de
primer orden, siempre que se conozca su condición inicial. La idea del método es encontrar una solución
numérica a la ecuación diferencial en el intervalo comprendido entre un x0 y un Xf.
En primer lugar, se discretiza el intervalo en n+1 puntos: x0, x1, x2, x3…, xn.
Luego, se hace una predicción aproximada del valor de la función y(x) en el punto siguiente.
El procedimiento se repite para obtener los sucesivos puntos.

ejemplos:
dy/dx = -1
el resultado de esta ecuación diferencial es la integral de -1, por lo que da y=-x
y(0) = 0
h= 0.5
n=2
por ende el intervalo es [0,1]

dy/dx = 1
y=x
y(0) = 0
h=0.2
n = 5
[0,1]

dy/dx = x
y= x^2/2
y(0.5) = 0.125
h= 0.1
n=10
[0,1]


"""



#Define la ecuacion diferencial ordinaria de primer orden con dy despejada, la función f despeja dy para poder
#usar sus valores en la aproximación con el método de euler
#t es la variable independiente, y es la variable dependiente, el resto son los coeficientes

#Por cuestiones de practicidad restrigimos los grados de los polinomios a primer grado, pero por ejemplo para 
#polinomios de 2do grado o mas, habria agregar el coeficiente y sumar la respectiva multiplicación del coef con su
#variable elevada al exponente del grado correspondiente: x3*(t**3) + x2*(t**2) ... x0

def f(t, y, x1, x0, y1, y0):
    return -(x1*t+x0)/(y1*y+y0)

#ti yi definen las condiciones iniciales
#size define el tamaño de los pasos y steps define el número de pasos en el método,
#Escoger valores más pequeños de size hará que los resultados sean más precisos y que
#el tiempo de cómputo sea mayor
def calcEDO(ti,yi,size, steps, x1, x0, y1, y0):
    # Inicializar arreglos en cero para t, y
    t = np.zeros(steps+1)
    y = np.zeros(steps+1)
    # Colocar los valores iniciales de t, y
    t[0] = ti
    y[0] = yi
    #Usar el método de Euler para calcular el resto de valores de t, y
    for i in range(steps):
        y[i+1] = y[i] + size*f(t[i], y[i], x1, x0, y1, y0)
        t[i+1] = t[i] + size
    
    #Mostrar los resultados
    plt.plot(t, y, 'b')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Euler Method')
    plt.show()