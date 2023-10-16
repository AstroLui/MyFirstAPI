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

#Imprimimos los puntos originales y la recta
plt.scatter(x, y, color='green')
plt.plot(x, puntos, color='red')
plt.title('Ajuste de mínimos cuadrados de una recta')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
