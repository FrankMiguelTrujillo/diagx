import pandas as pd

df = pd.read_csv("data/nonbankrupt_retail_16_year_13_14_15.csv", sep=";", decimal=",") 
dr = pd.read_csv("data/bankrupt_retail_16_year_13_14_15.csv", sep=";", decimal=",") 
df_bankrupt = dr  # tu dataset de empresas quebradas
df_nonbankrupt = df  # tu dataset de empresas no quebradas

df_completo = pd.concat([df_bankrupt, df_nonbankrupt], ignore_index=True)

print(f"cuantas filas y columnas tiene?: {df.shape}")        # ¿cuántas filas y columnas tiene?
print(f"primeras filas: {df.head()}")       # las primeras filas, para ver cómo se ven los datos
print(f"tipos de datos: {df.info()}")  
print(df.isnull().sum().sort_values(ascending=False))# tipos de datos, valores nulos por columna
umbral = 0.3 * len(df)
df_limpio = df.dropna(axis=1, thresh=len(df) - umbral)
df_limpio = df_limpio.fillna(df_limpio.median(numeric_only=True))
print(df_limpio.isnull().sum().sum())
print(df_limpio)

print(f"cuantas filas y columnas tiene?: {dr.shape}")        # ¿cuántas filas y columnas tiene?
print(f"primeras filas: {dr.head()}")       # las primeras filas, para ver cómo se ven los datos
print(f"tipos de datos: {dr.info()}")  
print(dr.isnull().sum().sort_values(ascending=False))# tipos de datos, valores nulos por columna
umbral = 0.3 * len(dr)
dr_limpio = dr.dropna(axis=1, thresh=len(dr) - umbral)
dr_limpio = dr_limpio.fillna(dr_limpio.median(numeric_only=True))
print(dr_limpio.isnull().sum().sum())

print(df_completo.shape)
umbral = 0.3 * len(df_completo)
df_final = df_completo.dropna(axis=1, thresh=len(df_completo) - umbral)
print(df_final.shape)

df_final = df_final.fillna(df_final.median(numeric_only=True))
print(df_final.isnull().sum().sum())