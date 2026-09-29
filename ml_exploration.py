import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import joblib

# Después de entrenar modelo y scaler...

df = pd.read_csv("data/nonbankrupt_retail_16_year_13_14_15.csv", sep=";", decimal=",")
dr = pd.read_csv("data/bankrupt_retail_16_year_13_14_15.csv", sep=";", decimal=",")
dr1 = pd.read_csv("data/bankrupt_retail_13_year_10_11_12.csv", sep=";", decimal=",")
dr2 = pd.read_csv("data/bankrupt_retail_14_year_11_12_13.csv", sep=";", decimal=",")
dr3 = pd.read_csv("data/bankrupt_retail_15_year_12_13_14.csv", sep=";", decimal=",")

df_bankrupt1 = dr3
df_bankrupt2 = dr2
df_bankrupt3 = dr1
df_bankrupt = dr
df_nonbankrupt = df

df_bankrupt["target"] = 1
df_bankrupt1["target"] = 1
df_bankrupt2["target"] = 1
df_bankrupt3["target"] = 1
df_nonbankrupt["target"] = 0

df_completo = pd.concat([df_bankrupt, df_bankrupt1, df_bankrupt2, df_bankrupt3, df_nonbankrupt], ignore_index=True)

umbral = 0.3 * len(df_completo)
df_final = df_completo.dropna(axis=1, thresh=len(df_completo) - umbral)
df_final = df_final.fillna(df_final.median(numeric_only=True))
print(df_final.isnull().sum().sum())

X = df_final.drop(columns=["target", "Unnamed: 0"])
y = df_final["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(X_train.shape, X_test.shape)

# Escalar: fit SOLO sobre train
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

modelo = LogisticRegression(max_iter=1000, class_weight="balanced")
modelo.fit(X_train_scaled, y_train)

y_pred = modelo.predict(X_test_scaled)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

joblib.dump(modelo, "modelo_quiebra.pkl")
joblib.dump(scaler, "scaler_quiebra.pkl")