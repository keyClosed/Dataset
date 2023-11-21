import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ruta al archivo CSV con datos del 2010 y posterior
csv_file_path = "C:\\Users\\keyly\\Desktop\\Dataset\\Extract.csv"

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(csv_file_path)

# Limpiar y estandarizar el texto en la columna 'Base de datos'
df['Base de datos'] = df['Base de datos'].str.strip().str.lower().str.replace('.', '')

# Mostrar los valores únicos y sus recuentos en 'Base de datos'
unique_db_counts = df['Base de datos'].value_counts()
print("Valores únicos y sus recuentos en 'Base de datos' después de limpieza:")
print(unique_db_counts)

# Crear una figura con subgráficos
fig, ax = plt.subplots(figsize=(10, 6))  # Ajusta el tamaño según tus preferencias

# Utilizar un color palette de seaborn
colors = sns.color_palette('husl', n_colors=len(unique_db_counts))

# Grafico de barras para la distribución de bases de datos
bar_plot = df['Base de datos'].value_counts().sort_index().plot(kind='bar', color=colors, ax=ax)

# Personalizar el gráfico
ax.set_title('Distribución de Bases de Datos ')
ax.set_ylabel('Cantidad')
ax.set_xlabel('Base de datos')

# Mostrar la información de recuentos en las barras
for p in bar_plot.patches:
    bar_plot.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                      ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Ajustar el diseño para evitar superposiciones
fig.tight_layout()

# Mostrar el gráfico
plt.show()
