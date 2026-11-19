# Databricks notebook source
# MAGIC %md
# MAGIC # 03 · CRISP-DM Fase 4 (Modelado) · Diseño de Experimentos (DoE) y MLflow
# MAGIC **Trabajo de Grado 1 · Especialización en Ciencia de Datos · Universidad Santo Tomás, Tunja**
# MAGIC
# MAGIC ## 1. Problema analítico
# MAGIC Prevalencia de fraude de solo **1.48 %** (60 fraudes en 4,060 transacciones) y costos asimétricos:
# MAGIC
# MAGIC * Falso negativo (fraude no detectado): **\$1,200 USD**
# MAGIC * Falso positivo (falsa alarma gestionada): **\$15 USD**
# MAGIC
# MAGIC ## 2. Hipótesis (α = 0.05)
# MAGIC * **H0:** la calibración de `C` con `class_weight='balanced'` no logra *Recall* ≥ 91.7 % con *Precision* ≥ 85 % en la prueba independiente.
# MAGIC * **H1:** el modelo calibrado logra *Recall* ≥ 91.7 % (al menos 11 de los 12 fraudes de prueba) con *Precision* ≥ 85 %, y reduce la pérdida económica en más del 80 % frente al modelo base que nunca detecta fraude.
# MAGIC
# MAGIC ## 3. Variables del experimento
# MAGIC * **Independientes:** `C` ∈ {0.01, 0.1, 1.0, 10.0}, `class_weight` y kernel RBF.
# MAGIC * **Dependientes:** Recall, Precision, F1 y pérdida financiera total (USD).
# MAGIC * **Control:** `random_state=42`, partición estratificada 80/20 y escalado z-score ajustado solo con entrenamiento.

# COMMAND ----------

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# ==============================================================================
# CRISP-DM FASE 4: PARTICIÓN ESTRATIFICADA SIN FUGA DE INFORMACIÓN
# ==============================================================================

# El CSV se importó al workspace, en la misma carpeta que este cuaderno
df = pd.read_csv("transacciones_fraude.csv")

X = df[["monto_transaccion", "tiempo_respuesta_ms", "intentos_previos"]]
y = df["es_fraude"]

# Compuerta QA 3.1: la partición estratificada preserva la prevalencia
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print("=" * 75)
print("CRISP-DM FASE 4: PROTOCOLO DE PARTICIÓN ESTRATIFICADA (DoE)")
print("=" * 75)
print(f"-> Entrenamiento : {X_train.shape[0]:,} transacciones ({y_train.sum()} fraudes | {y_train.mean()*100:.2f}%)")
print(f"-> Prueba (test) : {X_test.shape[0]:,} transacciones ({y_test.sum()} fraudes | {y_test.mean()*100:.2f}%)")

# El escalador se ajusta SOLO con entrenamiento (evita data leakage)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("✅ Estandarización z-score completada sin fuga de información.")

# COMMAND ----------

import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

COSTO_FN = 1200.0  # fraude no detectado
COSTO_FP = 15.0    # falsa alarma

# En Databricks el experimento se nombra con ruta absoluta dentro del workspace
usuario = spark.sql("SELECT current_user()").first()[0]
mlflow.set_experiment(f"/Users/{usuario}/Experimento_Deteccion_Fraude_DoE")

# Modelo base de referencia: nunca detecta fraude -> pierde todos los fraudes de prueba
costo_base = int(y_test.sum()) * COSTO_FN

# (C, class_weight): barrido de C + un control sin ponderación para contrastar H0
configuraciones = [(0.01, "balanced"), (0.1, "balanced"), (1.0, "balanced"), (10.0, "balanced"), (1.0, None)]
resultados_experimentales = []

print("\n" + "=" * 96)
print(f"{'C':<7} | {'class_weight':<12} | {'Precision':<9} | {'Recall':<7} | {'F1':<7} | {'FN':<3} | {'FP':<3} | {'Costo Total ($)':<15}")
print("=" * 96)

for c, cw in configuraciones:
    nombre = f"SVM_RBF_C_{c}_{'balanced' if cw else 'sin_pesos'}"
    with mlflow.start_run(run_name=nombre):
        modelo = SVC(C=c, kernel="rbf", class_weight=cw, random_state=42)
        modelo.fit(X_train_scaled, y_train)
        predicciones = modelo.predict(X_test_scaled)

        prec = precision_score(y_test, predicciones, zero_division=0)
        rec = recall_score(y_test, predicciones)
        f1 = f1_score(y_test, predicciones)
        tn, fp, fn, tp = confusion_matrix(y_test, predicciones).ravel()
        costo_total = fn * COSTO_FN + fp * COSTO_FP

        # Trazabilidad en MLflow Tracking
        mlflow.log_params({"model_type": "SVC", "C": c, "kernel": "rbf", "class_weight": str(cw)})
        mlflow.log_metrics({
            "test_accuracy": accuracy_score(y_test, predicciones),
            "test_precision": prec,
            "test_recall": rec,
            "test_f1": f1,
            "falsos_negativos": int(fn),
            "falsos_positivos": int(fp),
            "costo_financiero_total_usd": costo_total,
        })
        firma = infer_signature(X_train_scaled, predicciones)
        mlflow.sklearn.log_model(modelo, name="model", signature=firma)

        resultados_experimentales.append(
            {"C": c, "class_weight": cw, "Precision": prec, "Recall": rec, "F1": f1, "FN": int(fn), "FP": int(fp), "Costo": costo_total}
        )
        print(f"{c:<7} | {str(cw):<12} | {prec:<9.4f} | {rec:<7.4f} | {f1:<7.4f} | {fn:<3} | {fp:<3} | ${costo_total:<14,.2f}")

print("=" * 96)
print(f"Modelo base (nunca detecta fraude): costo = ${costo_base:,.2f}")

# COMMAND ----------

import matplotlib.pyplot as plt

# ==============================================================================
# VISUALIZACIÓN: COMPROMISO PRECISION-RECALL VS COSTO TOTAL
# ==============================================================================

barrido = [r for r in resultados_experimentales if r["class_weight"] == "balanced"]
cs = [r["C"] for r in barrido]

fig, ax1 = plt.subplots(figsize=(10.5, 4.8), dpi=100)
ax1.plot(cs, [r["Recall"] for r in barrido], marker="o", color="#21918c", linewidth=2.4, label="Recall (fraudes capturados)")
ax1.plot(cs, [r["Precision"] for r in barrido], marker="s", color="#3b528b", linewidth=2.4, label="Precisión (confiabilidad de la alarma)")
ax1.axvline(x=0.1, color="#5c6274", linestyle=":", linewidth=2, label="Primer C sin pérdida (C = 0.1)")
ax1.set_xscale("log")
ax1.set_xlabel("Parámetro de regularización C (escala logarítmica)", fontsize=10)
ax1.set_ylabel("Métrica (0.0 a 1.0)", color="#21918c", fontsize=10)
ax1.set_ylim(0.55, 1.05)
ax1.grid(True, which="both", linestyle="--", alpha=0.5)

ax2 = ax1.twinx()
ax2.plot(cs, [r["Costo"] for r in barrido], marker="^", color="#d43d51", linewidth=2.5, linestyle="--", label="Pérdida financiera total (USD)")
ax2.set_ylabel("Costo en el conjunto de prueba (USD)", color="#d43d51", fontsize=10)

plt.title("Fase 4 CRISP-DM: sesgo-varianza frente a pérdida financiera", fontsize=11, fontweight="bold", pad=34)
fig.legend(loc="upper center", bbox_to_anchor=(0.5, 0.93), ncol=4, framealpha=0.9, fontsize=8)
plt.tight_layout()
plt.show()

# COMMAND ----------

# ==============================================================================
# DICTAMEN ESTADÍSTICO DE LAS HIPÓTESIS
# ==============================================================================
elegido = next(r for r in resultados_experimentales if r["C"] == 1.0 and r["class_weight"] == "balanced")
n_fraudes = int(y_test.sum())
tp_elegido = n_fraudes - elegido["FN"]

# Intervalo de confianza de Wilson (95 %) para el Recall: solo hay 12 fraudes de prueba
z = 1.96
p_hat = tp_elegido / n_fraudes
centro = (p_hat + z**2 / (2 * n_fraudes)) / (1 + z**2 / n_fraudes)
margen = z * np.sqrt(p_hat * (1 - p_hat) / n_fraudes + z**2 / (4 * n_fraudes**2)) / (1 + z**2 / n_fraudes)

ahorro = (1 - elegido["Costo"] / costo_base) * 100
print(f"Modelo seleccionado: SVM RBF, C = 1.0, class_weight = 'balanced'")
print(f"Recall    : {elegido['Recall']*100:.2f}% ({tp_elegido}/{n_fraudes} fraudes)  | IC 95% Wilson: [{(centro-margen)*100:.1f}%, {min(centro+margen,1)*100:.1f}%]")
print(f"Precision : {elegido['Precision']*100:.2f}%")
print(f"Pérdida   : ${elegido['Costo']:,.0f} frente a ${costo_base:,.0f} del modelo base (ahorro {ahorro:.2f}%)")
print("Decisión  : se rechaza H0 (Recall >= 91.7% y Precision >= 85%)" if elegido["Recall"] >= 0.917 and elegido["Precision"] >= 0.85 else "Decisión  : no se rechaza H0")
print("Cautela   : solo 12 fraudes de prueba y clases muy separables; el Video 4 valida con validación cruzada.")
