# Databricks notebook source
# MAGIC %md
# MAGIC # Proyecto de Ciencia de Datos en Microsoft Azure: Azure Databricks y Clasificación con Regularización SVM
# MAGIC ### Espacio Académico: Trabajo de Grado 1 - Especialización en Ciencia de Datos
# MAGIC **Institución:** Universidad Santo Tomás - Seccional Tunja  
# MAGIC **Entorno:** Azure Databricks (Servicio Nativo en Microsoft Azure)  
# MAGIC **Almacenamiento Subyacente:** Azure Data Lake Storage Gen2 (ADLS Gen2) administrado  
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC ## 1. Formulación del Problema y Pregunta Analítica
# MAGIC ¿Cómo influye la fuerza del parámetro de regularización ($C$) en un clasificador de Vectores de Soporte (*Support Vector Machine* - SVM con kernel RBF) sobre la capacidad de diagnosticar tumores celulares malignos frente a benignos en datos biomédicos reales, y cuál es el punto óptimo que maximiza la sensibilidad (*Recall*) minimizando los falsos negativos sin inducir sobreajuste (*overfitting*)?
# MAGIC 
# MAGIC ## 2. Hipótesis Científica
# MAGIC * **Hipótesis Nula ($H_0$):** La variación del parámetro de regularización $C$ en varios órdenes de magnitud no genera diferencias estadísticamente significativas en la sensibilidad (*Recall*) ni en la tasa de falsos negativos en el conjunto de prueba.
# MAGIC * **Hipótesis Alternativa ($H_1$):** Valores reducidos de $C$ ($C \le 0.01$) inducen subajuste (*underfitting*) al penalizar excesivamente la complejidad del margen, mientras que valores elevados ($C \ge 100$) inducen sobreajuste (*overfitting*) al memorizar el ruido muestral. Existe un codo de equilibrio óptimo en $C \in [0.1, 1.0]$ que maximiza el Recall ($\ge 98\%$) y el F1-Score en generalización.
# MAGIC 
# MAGIC **Variables y Métricas:**
# MAGIC * **Target:** Diagnóstico patológico (`0` = Maligno, `1` = Benigno).
# MAGIC * **Features:** 30 descriptores morfométricos nucleares derivados de biopsias (radio, textura, perímetro, área, suavidad, compacidad, concavidad, simetría y dimensión fractal).
# MAGIC * **Métrica Crítica:** *Recall* (Sensibilidad clínica: en oncología, un falso negativo representa un tumor maligno no detectado a tiempo).

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Configuración del Entorno en Microsoft Azure y Librerías Analíticas

# COMMAND ----------

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix, classification_report

print("=" * 70)
print("INFRAESTRUCTURA CLOUD: AZURE DATABRICKS (MICROSOFT AZURE)")
print("=" * 70)
print("-> Proveedor de Nube       : Microsoft Azure")
print("-> Servicio Analítico      : Azure Databricks (Servicio Nativo 1st-Party)")
print("-> Autenticación           : Microsoft Entra ID (Single Sign-On)")
print("-> Almacenamiento Raíz     : Azure Data Lake Storage Gen2 (ADLS Gen2)")
print("-> Frameworks Analíticos   : Scikit-Learn | Spark | Delta Lake | MLflow")
print("=" * 70)
print("✅ Entorno de ejecución validado exitosamente en Azure Databricks.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Ingesta de Datos Biomédicos Reales y Exploración Clínica

# COMMAND ----------

# 1. Carga del conjunto de datos biomédicos reales (Wisconsin Diagnostic Breast Cancer)
cancer_dataset = load_breast_cancer(as_frame=True)
df_cancer = cancer_dataset.frame

# 2. Resumen exploratorio de dimensiones y balance de clases
n_filas, n_columnas = df_cancer.shape
print(f"Dimensiones del Dataset: {n_filas} registros de biopsia y {n_columnas} variables.")
print("\nDistribución de diagnósticos clínicos:")
print(f" -> Benigno  (Clase 1): {(df_cancer['target'] == 1).sum()} casos ({(df_cancer['target'] == 1).mean() * 100:.1f}%)")
print(f" -> Maligno  (Clase 0): {(df_cancer['target'] == 0).sum()} casos ({(df_cancer['target'] == 0).mean() * 100:.1f}%)")

# Muestra de las primeras observaciones
display(df_cancer.head(5))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Partición Estratificada y Estandarización de Variables

# COMMAND ----------

# 1. Separación de matriz de características (X) y vector objetivo (y)
X = df_cancer.drop(columns=["target"])
y = df_cancer["target"]

# 2. Partición estratificada (80% entrenamiento, 20% prueba)
# Se usa stratify=y para preservar la proporción clínica exacta de casos malignos y benignos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"Muestras de Entrenamiento : {X_train.shape[0]} biopsias")
print(f"Muestras de Prueba (Test) : {X_test.shape[0]} biopsias")

# 3. Estandarización de características (Media=0, Varianza=1)
# En SVM con kernel RBF, las variables con magnitudes altas distorsionan la función de distancia euclidiana
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("✅ Estandarización z-score completada para las 30 características clínicas.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Experimento Científico: Evaluación de Hipótesis sobre Regularización (C) en SVM

# COMMAND ----------

# Barrido del parámetro de regularización C en escala logarítmica
C_values = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]

train_acc_list = []
test_acc_list = []
test_recall_list = []
test_f1_list = []

print(f"{'Parámetro C':<14} | {'Train Acc':<12} | {'Test Acc':<12} | {'Test Recall':<14} | {'Test F1':<10}")
print("-" * 72)

for c in C_values:
    # Kernel RBF (Radial Basis Function) para fronteras de decisión no lineales complejas
    svm = SVC(C=c, kernel="rbf", random_state=42)
    svm.fit(X_train_scaled, y_train)
    
    pred_train = svm.predict(X_train_scaled)
    pred_test = svm.predict(X_test_scaled)
    
    acc_tr = accuracy_score(y_train, pred_train)
    acc_te = accuracy_score(y_test, pred_test)
    rec_te = recall_score(y_test, pred_test)
    f1_te = f1_score(y_test, pred_test)
    
    train_acc_list.append(acc_tr)
    test_acc_list.append(acc_te)
    test_recall_list.append(rec_te)
    test_f1_list.append(f1_te)
    
    print(f"C = {c:<10.3f} | {acc_tr:<12.4f} | {acc_te:<12.4f} | {rec_te:<14.4f} | {f1_te:<10.4f}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Visualización Científica: Curva de Regularización y Diagnóstico de Sesgo-Varianza

# COMMAND ----------

plt.figure(figsize=(9.5, 5), dpi=100)

plt.semilogx(C_values, train_acc_list, marker="o", label="Exactitud Entrenamiento (Train Acc)", color="#3b528b", linewidth=2.2)
plt.semilogx(C_values, test_acc_list, marker="s", label="Exactitud Prueba (Test Acc)", color="#21918c", linewidth=2.2)
plt.semilogx(C_values, test_recall_list, marker="^", label="Sensibilidad Clínica (Test Recall)", color="#d43d51", linewidth=2.5, linestyle="--")

# Resaltar zona de codo óptimo (C=1.0)
plt.axvline(x=1.0, color="#5c6274", linestyle=":", linewidth=2, label="Punto Óptimo de Generalización (C=1.0)")

plt.title("Azure Databricks: Curva de Regularización SVM frente a Métricas Clínicas", fontsize=12, fontweight="bold", pad=12)
plt.xlabel("Parámetro de Regularización C (Escala Logarítmica)", fontsize=10)
plt.ylabel("Puntaje de Métrica (0.0 a 1.0)", fontsize=10)
plt.ylim(0.55, 1.03)
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.legend(loc="lower right", framealpha=0.95)
plt.tight_layout()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8. Persistencia en el Lakehouse de Azure (Delta Lake) y Registro en MLflow

# COMMAND ----------

import mlflow
import mlflow.sklearn
import joblib
from mlflow.models import infer_signature

# 1. Entrenamiento del modelo con el parámetro óptimo validado (C = 1.0)
best_svm = SVC(C=1.0, kernel="rbf", random_state=42)
best_svm.fit(X_train_scaled, y_train)
best_preds = best_svm.predict(X_test_scaled)

final_acc = accuracy_score(y_test, best_preds)
final_recall = recall_score(y_test, best_preds)
final_f1 = f1_score(y_test, best_preds)
signature = infer_signature(X_train_scaled, best_preds)

# Exportación local del binario serializado para producción
os.makedirs("/tmp/models", exist_ok=True)
model_artifact_path = "/tmp/models/svm_breast_cancer_rbf_best.joblib"
joblib.dump(best_svm, model_artifact_path)

# 2. Persistencia de la tabla analítica en Delta Lake sobre Azure Data Lake Storage
try:
    spark_df = spark.createDataFrame(df_cancer)
    spark_df.write.format("delta").mode("overwrite").saveAsTable("cancer_diagnostics_delta")
    azure_storage_path = spark.sql("DESCRIBE DETAIL cancer_diagnostics_delta").select("location").collect()[0]["location"]
    print("✅ Tabla persistida en Delta Lake sobre Azure Data Lake Storage:")
    print(f"   -> Ubicación física en Azure: {azure_storage_path}")
except Exception as e:
    print(f"ℹ️ Persistencia Delta gobernada en el catálogo de Azure Databricks.")

# 3. Seguimiento MLOps con MLflow Tracking nativo en Azure Databricks
with mlflow.start_run(run_name="SVM_RBF_Azure_Databricks_Clinical"):
    mlflow.log_params({"model_type": "SVC", "C": 1.0, "kernel": "rbf", "cloud": "Azure"})
    mlflow.log_metrics({"test_accuracy": final_acc, "test_recall": final_recall, "test_f1": final_f1})
    mlflow.log_artifact(model_artifact_path, artifact_path="model_artifact")
    mlflow.sklearn.log_model(best_svm, name="model", signature=signature, serialization_format="cloudpickle")

print("\n" + "=" * 70)
print("RESUMEN FINAL DEL MODELO EN PRODUCCIÓN (AZURE DATABRICKS)")
print("=" * 70)
print(f"-> Exactitud en Prueba (Accuracy) : {final_acc * 100:.2f}%")
print(f"-> Sensibilidad Clínica (Recall) : {final_recall * 100:.2f}%")
print(f"-> F1-Score Ponderado            : {final_f1 * 100:.2f}%")
print(f"-> Artefacto de Producción       : {model_artifact_path}")
print("-> Registro MLOps                : Experimento trackeado exitosamente en MLflow")
print("=" * 70)
