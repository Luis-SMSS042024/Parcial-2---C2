import matplotlib.pyplot as plt   #Importación necesaria

# Datos base
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Gráfico de línea
plt.plot(x, y, color='blue', marker='o')
plt.title("Gráfico de Línea Simple")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostrar gráfico
plt.show()
