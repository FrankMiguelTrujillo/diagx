import pandas as pd

df = pd.read_csv("data/nonbankrupt_retail_16_year_13_14_15.csv", sep=";", decimal=",") 
print(f"cuantas filas y columnas tiene?: {df.shape}")        # ¿cuántas filas y columnas tiene?
print(f"primeras filas: {df.head()}")       # las primeras filas, para ver cómo se ven los datos
print(f"tipos de datos: {df.info()}")  
print(df.isnull().sum().sort_values(ascending=False))# tipos de datos, valores nulos por columna
umbral = 0.3 * len(df)
df_limpio = df.dropna(axis=1, thresh=len(df) - umbral)
print(df_limpio)