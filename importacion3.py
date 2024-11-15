import pandas as pd
import matplotlib.pyplot as plt

# Extraemos la tabla desde la URL
tabla = pd.read_html('https://as.com/juegos_olimpicos/2021/07/22/noticias/1626944865_048599.html')
df = tabla[0]  # Extraemos la primera tabla
print(df)

# Renombramos las columnas para facilitar su uso
df.columns = ['País', 'Oro', 'Plata', 'Bronce', 'Total']

# Eliminamos la primera fila (los nombres de columna duplicados en la tabla)
df = df.drop(0)

# Convertimos las columnas de medallas a numérico
df['Oro'] = pd.to_numeric(df['Oro'])
df['Plata'] = pd.to_numeric(df['Plata'])
df['Bronce'] = pd.to_numeric(df['Bronce'])
df['Total'] = pd.to_numeric(df['Total'])

# Seleccionamos los 10 países con más medallas
top_10_paises = df.nlargest(5, 'Total')

# Configuramos los datos para el gráfico de áreas apiladas
medallas = top_10_paises[['Oro', 'Plata', 'Bronce']].set_index(top_10_paises['País'])

# Graficamos
plt.figure(figsize=(12, 6))
medallas.plot(kind='area', stacked=True, color=['gold', 'silver', 'brown'], alpha=0.7, ax=plt.gca())
plt.xlabel('País')
plt.ylabel('Cantidad de Medallas')
plt.title('Top 10 Países con Más Medallas en los Juegos Olímpicos')
plt.xticks(rotation=45)
plt.legend(title='Tipo de Medalla')
plt.tight_layout()
plt.show()
