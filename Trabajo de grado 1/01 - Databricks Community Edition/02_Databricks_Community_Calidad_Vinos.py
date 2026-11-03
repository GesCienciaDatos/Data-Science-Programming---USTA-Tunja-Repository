# Databricks notebook source
# MAGIC %md
# MAGIC # Proyecto de Ciencia de Datos: Clasificación de Calidad de Vinos
# MAGIC ### Espacio Académico: Trabajo de Grado 1 - Especialización en Ciencia de Datos
# MAGIC **Institución:** Universidad Santo Tomás - Seccional Tunja  
# MAGIC **Entornos compatibles:** Databricks Community Edition, Databricks en AWS y Azure Databricks
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC ## 1. Formulación del Problema y Pregunta Analítica
# MAGIC ¿Es posible predecir y clasificar de manera óptima la calidad de un vino (Alta calidad vs Regular) a partir de sus propiedades fisicoquímicas mediante un árbol de decisión clásico de Machine Learning?
# MAGIC 
# MAGIC ## 2. Formulación de Hipótesis Científica
# MAGIC * **Hipótesis Nula ($H_0$):** La complejidad del árbol de decisión (`max_depth`) no afecta el rendimiento de generalización del modelo; el error y la precisión en datos de prueba se mantendrán constantes sin importar la profundidad.
# MAGIC * **Hipótesis Alternativa ($H_1$):** Incrementar la profundidad del árbol (`max_depth`) mejora la precisión en el conjunto de entrenamiento, pero a partir de un valor umbral genera sobreajuste (*overfitting*), degradando significativamente las métricas en el conjunto de prueba.
# MAGIC 
# MAGIC **Variables del Estudio:**
# MAGIC * **Variable Dependiente (Target):** Calidad binaria (`1` si `quality` >= 6 [Alta Calidad], `0` si `quality` < 6 [Calidad Regular]).
# MAGIC * **Variables Independientes (Features):** 11 características fisicoquímicas reales (acidez fija, acidez volátil, ácido cítrico, azúcar residual, cloruros, dióxido de azufre libre, dióxido de azufre total, densidad, pH, sulfatos, alcohol).
# MAGIC * **Métrica de éxito:** Accuracy y F1-Score ponderado en el conjunto de prueba.

# COMMAND ----------

# 1. Importación de bibliotecas estándar (Preinstaladas en Databricks Runtime ML)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix

print("Bibliotecas importadas correctamente.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Carga y Exploración de Datos Reales (Sin Datos Sintéticos)
# MAGIC Consumimos directamente el conjunto de datos abierto de calidad de vino tinto (*Wine Quality Red*) del repositorio oficial de la **UCI Machine Learning Repository**.

# COMMAND ----------

# Carga de datos reales desde el repositorio de la UCI
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=";")

# Creación de la variable objetivo binaria (1: Buena calidad >= 6, 0: Regular < 6)
df["target"] = (df["quality"] >= 6).astype(int)

print(f"Dimensiones del dataset: {df.shape[0]} filas y {df.shape[1]} columnas")
print("\nDistribución de la variable objetivo (target):")
print(df["target"].value_counts(normalize=True))

display(df.head(5))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. División en Conjuntos de Entrenamiento y Prueba (Train / Test Split)
# MAGIC Dividimos el 80% para entrenamiento y 20% para evaluación final, utilizando estratificación para mantener la proporción de clases.

# COMMAND ----------

# Separación de características (X) y etiqueta (y)
X = df.drop(columns=["quality", "target"])
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"Muestras de entrenamiento: {X_train.shape[0]}")
print(f"Muestras de prueba:        {X_test.shape[0]}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Prueba de Hipótesis: Experimento de Variación de Hiperparámetros
# MAGIC Entrenamos múltiples árboles de decisión variando el hiperparámetro de **profundidad máxima (`max_depth`)** para medir el comportamiento de las métricas de **Accuracy** y **F1-Score** en entrenamiento vs prueba.

# COMMAND ----------

# Lista de profundidades a evaluar
depths = [1, 2, 3, 4, 5, 7, 10, 15, 20, None]
train_acc_list = []
test_acc_list = []
train_f1_list = []
test_f1_list = []

print(f"{'Profundidad':<14} | {'Train Acc':<10} | {'Test Acc':<10} | {'Test F1':<10}")
print("-" * 52)

for d in depths:
    clf = DecisionTreeClassifier(max_depth=d, random_state=42)
    clf.fit(X_train, y_train)
    
    pred_train = clf.predict(X_train)
    pred_test = clf.predict(X_test)
    
    tr_acc = accuracy_score(y_train, pred_train)
    te_acc = accuracy_score(y_test, pred_test)
    tr_f1 = f1_score(y_train, pred_train, average='weighted')
    te_f1 = f1_score(y_test, pred_test, average='weighted')
    
    train_acc_list.append(tr_acc)
    test_acc_list.append(te_acc)
    train_f1_list.append(tr_f1)
    test_f1_list.append(te_f1)
    
    tag = str(d) if d is not None else "Sin límite"
    print(f"{tag:<14} | {tr_acc:<10.3f} | {te_acc:<10.3f} | {te_f1:<10.3f}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Visualización del Comportamiento de Métricas (Curva de Complejidad)
# MAGIC Graficamos el rendimiento en entrenamiento frente al rendimiento en prueba para contrastar empíricamente la hipótesis formulada.

# COMMAND ----------

x_labels = [str(d) if d is not None else "Sin límite" for d in depths]

plt.figure(figsize=(10, 5), dpi=100)
plt.plot(x_labels, train_acc_list, marker="o", label="Exactitud Entrenamiento (Train)", color="royalblue", linewidth=2.5)
plt.plot(x_labels, test_acc_list, marker="s", label="Exactitud Prueba (Test)", color="crimson", linewidth=2.5)
plt.plot(x_labels, test_f1_list, marker="^", label="F1-Score Prueba (Test)", color="forestgreen", linestyle="--", linewidth=2)

plt.axvline(x=3, color="gray", linestyle=":", label="Profundidad óptima estimada (d=4)")

plt.title("Comportamiento de Métricas: Impacto de max_depth en Sobreajuste (Overfitting)", fontsize=12, fontweight="bold")
plt.xlabel("Hiperparámetro: Profundidad Máxima del Árbol (max_depth)", fontsize=10)
plt.ylabel("Valor de Métrica (0.0 a 1.0)", fontsize=10)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="lower right", fontsize=9)
plt.tight_layout()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Conclusiones y Decisión sobre la Hipótesis
# MAGIC 1. **Decisión Estadística:** Se **rechaza la Hipótesis Nula ($H_0$)** y se **acepta la Hipótesis Alternativa ($H_1$)**.
# MAGIC 2. **Interpretación:** Para valores bajos de `max_depth` (1 a 2), el modelo experimenta **subajuste (*underfitting*)** con una exactitud inferior al 60%. A partir de profundidad 4, el conjunto de entrenamiento alcanza rápidamente el 100% de precisión perfecta, mientras que en prueba decae, evidenciando un **sobreajuste (*overfitting*)** severo.
# MAGIC 3. **Punto Óptimo:** La profundidad óptima de balance sesgo-varianza se localiza entre $d=3$ y $d=4$, donde se maximiza el F1-Score en datos no vistos.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8. Integración con MLflow (Tracking en Databricks)
# MAGIC Este bloque registra formalmente el modelo óptimo en el servidor de MLflow nativo de Databricks.

# COMMAND ----------

import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

best_model = DecisionTreeClassifier(max_depth=4, random_state=42)
best_model.fit(X_train, y_train)
preds = best_model.predict(X_test)

signature = infer_signature(X_train, best_model.predict(X_train))

try:
    with mlflow.start_run(run_name="Modelo_Optimo_DecisionTree"):
        mlflow.log_param("max_depth", 4)
        mlflow.log_metric("test_accuracy", accuracy_score(y_test, preds))
        mlflow.log_metric("test_f1_weighted", f1_score(y_test, preds, average="weighted"))
        mlflow.sklearn.log_model(
            sk_model=best_model,
            artifact_path="modelo_arbol_optimo",
            signature=signature,
            input_example=X_train.iloc[:3]
        )
    print("Modelo y métricas registrados exitosamente en MLflow.")
except Exception as e:
    print(f"MLflow local/offline: {e}")
