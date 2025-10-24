import matplotlib.pyplot as plt

# Datos simulados de la BD Ferretería Guanaco
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
cemento = [320, 450, 480, 510, 600]
pintura = [250, 300, 350, 380, 420]

# 1️⃣ Gráfico de líneas (tendencia mensual)
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.plot(meses, cemento, marker='o', label='Cemento', color='brown')
plt.plot(meses, pintura, marker='s', label='Pintura', color='blue')
plt.title("Tendencia Mensual de Ventas")
plt.xlabel("Meses")
plt.ylabel("Unidades Vendidas")
plt.legend()
plt.grid(True)

# 2️⃣ Gráfico de barras (comparación visual)
plt.subplot(2, 2, 2)
plt.bar(meses, cemento, color='peru', label='Cemento')
plt.bar(meses, pintura, color='skyblue', alpha=0.7, label='Pintura')
plt.title("Comparación de Ventas Mensuales")
plt.xlabel("Meses")
plt.ylabel("Unidades Vendidas")
plt.legend()

# 3️⃣ Gráfico circular (participación total)
plt.subplot(2, 2, 3)
productos = ['Cemento', 'Pintura']
totales = [sum(cemento), sum(pintura)]
plt.pie(totales, labels=productos, autopct='%1.1f%%', colors=['saddlebrown', 'deepskyblue'])
plt.title("Porcentaje Total de Ventas por Producto")

# 4️⃣ Gráfico de dispersión (relación entre productos)
plt.subplot(2, 2, 4)
plt.scatter(cemento, pintura, color='green')
plt.title("Relación entre Ventas de Cemento y Pintura")
plt.xlabel("Ventas Cemento")
plt.ylabel("Ventas Pintura")
plt.grid(True)

# Ajustar diseño
plt.tight_layout()
plt.show()
