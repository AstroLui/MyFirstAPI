import numpy as np
import matplotlib.pyplot as plt

#Datos a los que vamos a aproximar 
x = np.random.randint(0, 10, 8)
y = np.random.randint(0, 10, 8)

#Obtenemos los valores de los coeficientes a y b
#Utilizando el metodo de los mínimos cuadrados
a, b= np.polyfit(x, y, 1)

#Obtenemos los puntos para graficar la recta aprox
puntos = a * x + b

