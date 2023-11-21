import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV con datos del 2010 y posterior
csv_file_path = "C:\\Users\\keyly\\Desktop\\Dataset\\Extract.csv"

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(csv_file_path)

# Convertir la columna 'Fecha' a formato de fecha
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y')

# Extraer el año y asignarlo a una nueva columna 'Año'
df['Año'] = df['Fecha'].dt.year

# Crear una tabla pivot para contar la frecuencia de cada región por año
pivot_table = df.pivot_table(index='Año', columns='Región', aggfunc='size', fill_value=0)

# Crear una figura con subgráficos
fig, ax = plt.subplots(figsize=(15, 8))  # Ajusta el tamaño según tus preferencias

# Grafico de barras apiladas para la distribución de regiones por año
pivot_table.plot(kind='bar', stacked=True, ax=ax)
ax.set_title('Distribución de Regiones por Año ')
ax.set_ylabel('Cantidad')
ax.set_xlabel('Año')

# Ajustar el diseño para evitar superposiciones
fig.tight_layout()

# Mostrar el gráfico
plt.show()


