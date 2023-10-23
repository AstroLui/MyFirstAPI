import numpy as np
import matplotlib.pyplot as plt

#Datos a los que vamos a aproximar 
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([3, 5, 4, 6, 8, 9, 7])

def imprimir(x,y,p):
    plt.scatter(x, y, color='green')
    plt.plot(x, p, color='red')
    plt.title('Ajuste de mínimos cuadrados de una parábola')
    plt.xlabel('x')
    plt.ylabel('y')
    root = plt.get_current_fig_manager().window
    root.geometry("800x500+1000+400")
    plt.show()
#Obtenemos los valores de los coeficientes a y b
#Utilizando el metodo de los mínimos cuadrados
def recta(x,y):
    a, b= np.polyfit(x, y, 1)
    puntos = a * x + b
    imprimir(x,y,puntos)
def parabola(x,y):
    a, b, c = np.polyfit(x, y, 2)
    puntos = a * (x**2) + b * x + c
    imprimir(x,y,puntos)

