#Derivar

#Librerias a usar
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x, y = symbols('x y', integer = True) # definir simbolos en sympy de tipo entero

#Definir la funcion (se puede poner la funcion que sea)
y = x**2

#Hace la derivada de la funcion
resultado = integrate(y, 0, 5)

#Puntos en los que se ven la grafica de la derivada (limite inferior grafica, limite maximo grafica, cantidad de ptos que tendra la funcion)
puntos = np.linspace(-10, 10, 20)

#Evaluar la funcion en un lambda
f1 = lambdify(x, y, 'numpy') #da valores float

#Evaluar la derivada en un lambda
f2 = lambdify(x, resultado, 'numpy') #da valores float

#graficas
nombre = [r'$f(x)$', r'$\frac{df(x)}{dx}$']
plt.figure(figsize = (11,6))
plt.plot(puntos, f1(puntos), '-b.', label= r'%s'%nombre[0]) #grafica funcion
plt.plot(puntos, f2(puntos), '-r.',label= r'%s'%nombre[1]) #grafica derivadas
plt.hlines(0, -10, 10, colors = 'k', linestyle= 'dotted') #eje horizontal
plt.vlines(0, -20, 20, colors = 'k', linestyle= 'dotted') #eje vertical
plt.xlabel('x [Abcisas]', fontsize = 16) #titulo de eje x
plt.ylabel('y [Ordenadas]', fontsize = 16) #titulo de eje y
plt.legend(loc='best',fontsize = 16) #para mostrar la leyenda de la derivada y la funcion
plt.title('Grafica de una funcion y su derivada', fontsize = 16) #titulo de la grafica
plt.grid() #lineas de la grafica
plt.show()