import pandas as pd
import matplotlib.pyplot as plt

# Importar los datos
tabla = pd.read_html('https://www.365scores.com/es/news/futbol-colombiano-ranking-mas-titulos/')
df = tabla[0]  # Extraemos la primera tabla
print (df)

# Renombrar columnas para facilidad de uso
df.columns = ["Equipo", "Titulos", "Torneos"]

# Convertir la columna de títulos a valores numéricos
df["Titulos"] = pd.to_numeric(df["Titulos"], errors="coerce")

# Seleccionar los 5 equipos con más títulos
top_5 = df.nlargest(5, "Titulos")

# Gráfico de dispersión (scatter plot)
plt.figure(figsize=(10, 6))
plt.scatter(top_5["Equipo"], top_5["Titulos"], color="purple", s=100)  # s=100 ajusta el tamaño de los puntos
plt.title("Top 5 Equipos con Más Títulos en Colombia")
plt.xlabel("Equipo")
plt.ylabel("Número de Títulos")
plt.grid(True)
plt.show()
