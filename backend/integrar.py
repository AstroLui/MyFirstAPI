#Integral


#Librerias a usar
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def integral(valor):

    x = symbols('x') # definir simbolos en sympy de tipo entero

    #Hace la integral definida de la funcion
    integral_definida = integrate(valor, x) #valores dentro de los limites calculados
    #pasaselo al label

    #Puntos en los que se ven la grafica de la integral (limite inferior grafica, limite maximo grafica, cantidad de ptos que tendra la funcion)
    puntos = np.linspace(-10, 10, 5)

    #Convierte la funcion en una funcion numerica usada para evaluar cada punto
    f1 = lambdify(x, valor, 'numpy') 

    #Conversion de la derivada en una funcion numerica que se pueda evaluar (usada para los puntos)
    f2 = lambdify(x, integral_definida, 'numpy')

    #graficas
    nombre = [r'$f(x)$', r'$\int f(x) dx$']
    plt.figure(figsize = (11,6)) #alto y ancho de la figura
    plt.plot(puntos, f1(puntos), '-b.', label= r'%s'%nombre[0]) #grafica funcion
    plt.plot(puntos, f2(puntos), '-r.',label= r'%s'%nombre[1]) #grafica integral
    plt.hlines(0, -10, 10, colors = 'k', linestyle= 'dotted') #eje horizontal en 0
    plt.vlines(0, -20, 20, colors = 'k', linestyle= 'dotted') #eje vertical en 0
    plt.xlabel('x [Abcisas]', fontsize = 16) #titulo de eje x
    plt.ylabel('y [Ordenadas]', fontsize = 16) #titulo de eje y
    plt.legend(loc='best',fontsize = 16) #para mostrar la leyenda de la integral y la funcion
    plt.title('Grafica de una funcion y su derivada', fontsize = 16) #titulo de la grafica
    plt.grid() #lineas de la grafica
    plt.show()