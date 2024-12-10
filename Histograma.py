### Primero, importamos la librería pandas para anaizar datos
import pandas as pd 

# Crearemos un diccionario Estrenos por año, en el que las claves serán los años y los valores son la cantidad de películas estrenadas por año
Estrenos_por_año = {'2000': 5,'2001': 9,'2002': 10,'2003': 19,'2004': 19 ,'2005': 19,'2006': 17,'2007': 28,'2008': 26,'2009': 28,'2010': 38,'2011': 40,'2012': 32,'2013': 47,'2014': 41,'2015': 67,'2016': 53,'2017': 59,'2018': 61,'2019': 56,'2020': 41,'2021': 70,'2022': 75,'2023': 81} 

# Ahora, importamos la librería matplotlib
import matplotlib.pyplot as plt

# Extraer los años y los valores de estrenos
años = list(Estrenos_por_año.keys())
estrenos = list(Estrenos_por_año.values())

# Crear la figura y el gráfico
plt.figure(figsize=(12, 6))

# Crear el gráfico de barras (histograma) usando los estrenos
plt.bar(años, estrenos, color='gold', edgecolor='black')

# Añadir título y etiquetas
plt.title('Estrenos por Año')
plt.xlabel('Año')
plt.ylabel('Número de Estrenos')

# Ajustar el diseño para que todo se vea bien
plt.tight_layout()

# Mostrar el gráfico
plt.show()