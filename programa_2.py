import numpy as np
#Matplotlib tiene muchos módulos. Importar uno solo
import matplotlib.pyplot as plt

#Dibujar una función seno
#Crear un ndarray de 1 dimensión, 100 elementos equiespaciados, de 0 a 2*PI
x= np.linspace(0, 2*np.pi, 100)
y= np.sin(x)

#Usar matplotlib
plt.figure(figsize=(8,4))
plt.title("Mi primer gráfico científico en Programación")
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("seno de x")
plt.grid(True)
plt.show()








