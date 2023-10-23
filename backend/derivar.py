#Derivar

#Librerias a usar
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def derivar(valor):

    x = symbols('x', integer = True) # definir simbolos en sympy de tipo entero

    #Definir la funcion (se puede poner la funcion que sea
    fu = valor
    #Hace la derivada de la funcion
    derivada = diff(fu) #pasaselo a un label

    #Puntos en los que se ven la grafica de la integrsl (limite inferior grafica, limite maximo grafica, cantidad de ptos que tendra la funcion)
    puntos = np.linspace(-10, 10, 20)

    #Conversion de la funcion en una funcion que se puede evaluar (usada para los puntos)
    f1 = lambdify(x, fu, 'numpy')

    #Conversion de la derivada en una funcion que se pueda evaluar (usada para los puntos)
    f2 = lambdify(x, derivada, 'numpy')

    #graficas
    nombre = [r'$f(x)$', r'$\frac{df(x)}{dx}$']
    plt.figure(figsize = (11,6)) #alto y ancho de la figura
    plt.plot(puntos, f1(puntos), '-b.', label= r'%s'%nombre[0]) #grafica funcion
    plt.plot(puntos, f2(puntos), '-r.',label= r'%s'%nombre[1]) #grafica derivada
    plt.hlines(0, -10, 10, colors = 'k', linestyle= 'dotted') #eje horizontal en 0
    plt.vlines(0, -20, 20, colors = 'k', linestyle= 'dotted') #eje vertical en 0
    plt.xlabel('x [Abcisas]', fontsize = 16) #titulo de eje x
    plt.ylabel('y [Ordenadas]', fontsize = 16) #titulo de eje y
    plt.legend(loc='best',fontsize = 16) #para mostrar la leyenda de la derivada y la funcion
    plt.title('Grafica de una funcion y su derivada', fontsize = 16) #titulo de la grafica
    plt.grid() #lineas de la grafica
    root = plt.get_current_fig_manager().window
    root.geometry("800x500+1000+400")
    plt.show()