import matplotlib.pyplot as plt   #Importación necesaria

# Datos
nombres = ['Ana', 'Luis', 'Carla', 'Pedro']
edades = [23, 31, 29, 35]

# Gráfico de barras
plt.bar(nombres, edades, color='teal')
plt.title("Edades de los Participantes")
plt.xlabel("Nombre")
plt.ylabel("Edad")

# Mostrar gráfico
plt.show()
