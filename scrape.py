import pandas as pd
import matplotlib.pyplot as plt
tabla = pd.read_html('https://datosmacro.expansion.com/otros/coronavirus')
df = tabla[0]  # Selecciona el primer DataFrame de la lista

print(df)  # Imprime la tabla completa
print(df.head(5))  # Muestra los primeros 5 registros de la tabla

# Si quieres exportarlo a CSV:
# df.to_csv('nombrearchivo.csv')

# Asegúrate de que la columna "Confirmados" sea numérica, reemplazando valores no numéricos si es necesario
df['Confirmados'] = pd.to_numeric(df['Confirmados'], errors='coerce')

# Ordenar por la columna "Confirmados" y seleccionar los 5 países con más casos
top_5 = df.sort_values(by='Confirmados', ascending=False).head(5)

# Extraer los datos para la gráfica
x = top_5['Países']  # Eje X: nombres de los países
y = top_5['Confirmados']  # Eje Y: número de confirmados

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='skyblue')
plt.xlabel('Países')
plt.ylabel('Número de Confirmados')
plt.title('Top 5 Países con Mayor Número de Casos Confirmados')
plt.xticks(rotation=45)
plt.show()


