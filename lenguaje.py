import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV con datos del 2010 y posterior
csv_file_path = "C:\\Users\\keyly\\Desktop\\Dataset\\Extract.csv"

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(csv_file_path)

# Limpiar y estandarizar el texto en la columna 'Lenguaje'
df['Lenguaje'] = df['Lenguaje'].str.strip().str.lower().str.replace('.', '')

# Combinar las cuentas para el mismo lenguaje
df['Lenguaje'] = df['Lenguaje'].replace({'español ': 'español'})

# Mostrar los valores únicos y sus recuentos en 'Lenguaje'
unique_language_counts = df['Lenguaje'].value_counts()
print("Valores únicos y sus recuentos en 'Lenguaje' después de limpieza:")
print(unique_language_counts)

# Crear una figura con subgráficos
fig, ax = plt.subplots(figsize=(10, 10))  # Ajusta el tamaño según tus preferencias

# Generar explode dinámicamente basado en el número de lenguajes
explode = tuple(0.1 + 0.05 * i for i in range(len(unique_language_counts)))

# Obtener etiquetas de idiomas
language_labels = unique_language_counts.index

# Diagrama de torta para la distribución de lenguajes
df['Lenguaje'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, explode=explode, ax=ax, labels=language_labels)

# Ajustar el diseño para evitar superposiciones de etiquetas
plt.tight_layout()

# Mostrar el gráfico
plt.show()
