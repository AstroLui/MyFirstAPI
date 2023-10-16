import numpy as np
import matplotlib.pyplot as plt

#Datos a los que vamos a aproximar 
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([3, 5, 4, 6, 8, 9, 7])

#Obtenemos los valores de los coeficientes a y b
#Utilizando el metodo de los mínimos cuadrados
a, b, c = np.polyfit(x, y, 2)

#Obtenemos los puntos para graficar la parábola aprox
puntos = a * (x**2) + b * x + c

#Imprimimos los puntos originales y la parábola
plt.scatter(x, y, color='green')
plt.plot(x, puntos, color='red')
plt.title('Ajuste de mínimos cuadrados de una parábola')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
