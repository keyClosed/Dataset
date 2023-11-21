from docx import Document
import csv


def extraer_datos_por_titulo(doc_path):
    document = Document(doc_path)
    datos = []

    # Iterar sobre los párrafos del documento
    for paragraph in document.paragraphs:
        # Buscar títulos específicos y extraer datos asociados
        if "Fecha:" in paragraph.text:
            fecha = paragraph.text.split(":")[1].strip()
            # Agregar solo datos a partir de 2010
            if int(fecha) >= 2010:
                datos.append({"Fecha": fecha})
        elif "Enfoque:" in paragraph.text:
            if datos:  # Asegurarse de que haya datos antes de agregar 'Enfoque'
                datos[-1]["Enfoque"] = paragraph.text.split(":")[1].strip()
        elif "Región:" in paragraph.text:
            if datos:  # Asegurarse de que haya datos antes de agregar 'Región'
                datos[-1]["Región"] = paragraph.text.split(":")[1].strip()
        elif "Lenguaje:" in paragraph.text:
            if datos:  # Asegurarse de que haya datos antes de agregar 'Lenguaje'
                datos[-1]["Lenguaje"] = paragraph.text.split(":")[1].strip()
        elif "Base de datos:" in paragraph.text:
            if datos:  # Asegurarse de que haya datos antes de agregar 'Base de datos'
                datos[-1]["Base de datos"] = paragraph.text.split(":")[1].strip()

    return datos

# Ruta al documento de Word (.docx)
doc_path = "C:\\Users\\keyly\\Desktop\\Dataset.docx"

# Llamar a la función para extraer datos
datos_extraidos = extraer_datos_por_titulo(doc_path)

# Filtrar datos solo para el año 2010 y posterior
datos_extraidos_2010 = [dato for dato in datos_extraidos if int(dato["Fecha"]) >= 2010]

# Crear un archivo CSV con los datos del 2010 y posterior
csv_file_path = "C:\\Users\\keyly\\Desktop\\Dataset\\Extract_2010.csv"
fieldnames = ["Fecha", "Enfoque", "Región", "Lenguaje", "Base de datos"]

with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Escribir el encabezado
    writer.writeheader()

    # Escribir los datos
    for dato in datos_extraidos_2010:
        writer.writerow(dato)

print(f"Dataset exportado a: {csv_file_path}")
