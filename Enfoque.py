import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV con datos del 2010 y posterior
csv_file_path = "C:\\Users\\keyly\\Desktop\\Dataset\\Extract.csv"

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(csv_file_path)

# Crear una figura con subgráficos
fig, ax = plt.subplots(figsize=(10, 6))  # Ajusta el tamaño según tus preferencias

# Grafico de barras para la columna 'Enfoque'
df['Enfoque'].value_counts().plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Distribución por Enfoque')
ax.set_ylabel('Cantidad')

# Ajustar el diseño para evitar superposiciones
fig.tight_layout()

# Mostrar el gráfico
plt.show()