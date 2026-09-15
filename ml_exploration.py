import pandas as pd

df = pd.read_csv("data/nonbankrupt_retail_16_year_13_14_15.csv", sep=";") 
print(df.shape)        # ¿cuántas filas y columnas tiene?
print(df.head())       # las primeras filas, para ver cómo se ven los datos
print(df.info())       # tipos de datos, valores nulos por columna