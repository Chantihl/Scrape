import pandas as pd
import matplotlib.pyplot as plt

# Cargar la tabla de la página
tabla = pd.read_html('https://www.espn.com.co/futbol/copa-america/nota/_/id/13913981/maximos-campeones-titulos-cantidad-futbol-selecciones')
df = tabla[0]  # Extraemos la primera tabla
print (df)

# Renombrar las columnas para facilitar el acceso
df.columns = ['Selección', 'Total', 'Mundial', 'Continental', 'Confederaciones', 'JJOO', 'Europa-Sudamérica', 'Otros']

# Convertir la columna de 'Mundial' a numérica para ordenar y filtrar
df['Mundial'] = pd.to_numeric(df['Mundial'], errors='coerce')

# Seleccionar las 4 selecciones con más títulos en "Mundial"
top_4 = df.nlargest(4, 'Mundial')

# Crear el gráfico de torta
plt.figure(figsize=(8, 6))
plt.pie(top_4['Mundial'], labels=top_4['Selección'], autopct='%1.1f%%', startangle=140)
plt.title('Top 4 Selecciones con Más Títulos Mundiales')
plt.show()
