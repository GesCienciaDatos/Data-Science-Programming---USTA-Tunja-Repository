# Databricks notebook source
# MAGIC %md
# MAGIC # 02 · CRISP-DM Fases 1-3 y compuertas de calidad CRISP-ML(Q)
# MAGIC **Trabajo de Grado 1 · Especialización en Ciencia de Datos · Universidad Santo Tomás, Tunja**
# MAGIC Caso: detección temprana de fraude transaccional en canales digitales (4.060 transacciones reales, Hito G1).

# COMMAND ----------

# MAGIC %pip install seaborn -q

# COMMAND ----------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================================================================
# CRISP-DM FASE 2: COMPRENSIÓN DE LOS DATOS (DATA UNDERSTANDING)
# ==============================================================================

# El CSV se importó al workspace, en la misma carpeta que este cuaderno
df = pd.read_csv("transacciones_fraude.csv")

print("=" * 75)
print("CRISP-DM FASE 2: COMPRENSIÓN DE LOS DATOS (DATA UNDERSTANDING)")
print("=" * 75)
print(f"-> Volumen total de la muestra : {df.shape[0]:,} transacciones")
print(f"-> Variables analíticas        : {df.shape[1]} descriptores transaccionales")
print(f"-> Nombres de variables        : {list(df.columns)}")
print("\nPrimeras observaciones de la muestra:")
display(df.head(5))

# COMMAND ----------

# ==============================================================================
# CRISP-ML(Q) QA GATE 2.1: COMPLETITUD Y UNICIDAD (ESTÁNDAR DAMA DMBOK)
# ==============================================================================

nulos_totales = df.isnull().sum()
duplicados_totales = df.duplicated().sum()

reporte_integridad = pd.DataFrame({
    "Variable": df.columns,
    "Tipo_Dato": df.dtypes.astype(str).values,
    "Valores_Nulos": nulos_totales.values,
    "Completitud (%)": ((len(df) - nulos_totales.values) / len(df)) * 100,
    "Valores_Distintos": df.nunique().values
})

print("\n" + "=" * 75)
print("AUDITORÍA DAMA: COMPLETITUD Y UNICIDAD")
print("=" * 75)
print(f"-> Registros Duplicados en la Muestra : {duplicados_totales} ({duplicados_totales / len(df) * 100:.2f}%)")
display(reporte_integridad)

# COMMAND ----------

# ==============================================================================
# CRISP-ML(Q) QA GATE 2.2: CONSISTENCIA Y VALORES ATÍPICOS (MÉTODO IQR)
# ==============================================================================

q1 = df["monto_transaccion"].quantile(0.25)
q3 = df["monto_transaccion"].quantile(0.75)
iqr = q3 - q1
limite_superior_iqr = q3 + 1.5 * iqr

atipicos = df[df["monto_transaccion"] > limite_superior_iqr]
fraudes_en_atipicos = int(atipicos["es_fraude"].sum())
fraudes_totales = int(df["es_fraude"].sum())

print("\n" + "=" * 75)
print("AUDITORÍA DE CONSISTENCIA: RANGO INTERCUARTÍLICO (IQR) EN MONTOS")
print("=" * 75)
print(f"-> Monto Mínimo Transaccional    : ${df['monto_transaccion'].min():,.2f}")
print(f"-> Monto Máximo Transaccional    : ${df['monto_transaccion'].max():,.2f}")
print(f"-> Primer Cuartil (Q1 - 25%)     : ${q1:,.2f}")
print(f"-> Tercer Cuartil (Q3 - 75%)     : ${q3:,.2f}")
print(f"-> Rango Intercuartílico (IQR)   : ${iqr:,.2f}")
print(f"-> Límite Superior de Corte IQR  : ${limite_superior_iqr:,.2f}")
print(f"-> Transacciones Atípicas Altas  : {len(atipicos):,} transacciones ({len(atipicos)/len(df)*100:.2f}%)")
print(f"-> Dictamen Data Steward: los valores atípicos se preservan (contienen {fraudes_en_atipicos} de los "
      f"{fraudes_totales} fraudes confirmados, el {fraudes_en_atipicos / fraudes_totales * 100:.1f}%).")

# COMMAND ----------

# ==============================================================================
# CRISP-ML(Q) QA GATE 2.3: DISTRIBUCIÓN Y DESBALANCE DE LA VARIABLE OBJETIVO
# ==============================================================================

conteo_clases = df["es_fraude"].value_counts()
proporcion_clases = df["es_fraude"].value_counts(normalize=True) * 100

print("\n" + "=" * 75)
print("AUDITORÍA DEL TARGET (DESBALANCE EXTREMO DE CLASES)")
print("=" * 75)
print(f"-> Clase 0 (Operaciones Legítimas)  : {conteo_clases[0]:,} transacciones ({proporcion_clases[0]:.2f}%)")
print(f"-> Clase 1 (Operaciones Fraudulentas): {conteo_clases[1]:,} transacciones ({proporcion_clases[1]:.2f}%)")
print(f"-> Factor Real de Desbalance        : 1 fraude por cada {conteo_clases[0] // conteo_clases[1]} operaciones legítimas.")

# COMMAND ----------

# ==============================================================================
# VISUALIZACIÓN ANALÍTICA DE MINERÍA DE DATOS (CRISP-DM FASE 2)
# ==============================================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), dpi=100)
colores = {0: "#2b5c8f", 1: "#d95f02"}

# Gráfica A: Boxplot de montos con escala logarítmica
sns.boxplot(data=df, x="es_fraude", y="monto_transaccion", hue="es_fraude",
            palette=colores, legend=False, ax=axes[0])
axes[0].set_title("Distribución de Montos por Diagnóstico de Fraude", fontsize=11, fontweight="bold")
axes[0].set_xticks([0, 1])
axes[0].set_xticklabels(["Legítima (0)", "Fraude (1)"])
axes[0].set_yscale("log")
axes[0].set_ylabel("Monto Transaccional ($ Escala Logarítmica)")
axes[0].grid(True, linestyle="--", alpha=0.5)

# Gráfica B: Dispersión multivariable latencia vs reintentos
sns.scatterplot(
    data=df, x="tiempo_respuesta_ms", y="intentos_previos", hue="es_fraude",
    palette=colores, alpha=0.65, s=40, ax=axes[1]
)
axes[1].set_title("Patrones de Intrusión: Latencia vs Intentos Previos", fontsize=11, fontweight="bold")
axes[1].set_xlabel("Tiempo de Respuesta en Red (milisegundos)")
axes[1].set_ylabel("Intentos Fallidos en 24 Horas")
axes[1].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
