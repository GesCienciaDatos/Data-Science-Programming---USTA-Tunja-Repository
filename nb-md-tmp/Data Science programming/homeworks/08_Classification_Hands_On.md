# 08_Classification_Hands_On

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Taller 08: Clasificación y Selección de Modelos (Hands-On)
      </h1>
      <p style="margin: 6px 0 0 0; color: #1e3a8a; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Programación para Ciencia de Datos
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #1e3a8a; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Taller Práctico • Módulo 08
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/08_Classification_Hands_On.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🎯 Objetivo General del Taller

Desarrollar un pipeline integral de clasificación supervisada aplicando los modelos y técnicas vistos en el **Módulo 08: Clasificación**:
1. **Regresión Logística (Simple y Múltiple)** con análisis de probabilidad y cálculo de *Odds Ratios*.
2. **Evaluación Rigurosa de Rendimiento:** Matriz de Confusión, Precisión, Sensibilidad (*Recall*), $F_1$-Score, Curva ROC y AUC.
3. **Calibración de Umbrales:** Optimización del umbral de decisión según criterios de costo asimétrico del negocio.
4. **k-Nearest Neighbors ($k$-NN):** Escalado obligatorio con `StandardScaler`, búsqueda de hiperparámetros con `GridSearchCV` y validación cruzada estratificada (`StratifiedKFold`).
5. **Benchmark Comparativo:** Conclusiones justificadas sobre qué modelo desplegar en producción.

---
## 🛠️ Configuración Inicial del Entorno

Ejecuta la siguiente celda para cargar las librerías necesarias y configurar la función de descarga segura de datos.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os, urllib.request
import warnings
warnings.filterwarnings('ignore')

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (8, 4.5)
plt.rcParams['font.size'] = 10

def load_dataset(filename, module_folder="08 - Classification"):
    local_path = os.path.join(os.getcwd(), "data", filename)
    if os.path.exists(local_path):
        return local_path
    
    parent_path = os.path.join(os.getcwd(), "..", module_folder, "data", filename)
    if os.path.exists(parent_path):
        return parent_path

    raw_url = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/Data%20Science%20programming/{module_folder.replace(' ', '%20')}/data/{filename}"
    os.makedirs("data", exist_ok=True)
    target_path = os.path.join("data", filename)
    if not os.path.exists(target_path):
        urllib.request.urlretrieve(raw_url, target_path)
    return target_path

print("🚀 Entorno configurado correctamente para el Taller 08.")
```

---
### 📌 Parte 1: Carga y Exploración del Dataset de Retención de Clientes (`customer_churn.csv`)

**Ejercicio 1.1:** Carga el archivo `customer_churn.csv` utilizando la función `load_dataset('customer_churn.csv')`. Muestra las primeras 5 filas, la dimensión del DataFrame y la proporción exacta de la variable objetivo `churn` (0: No cancela, 1: Cancela).

```python
### TU CÓDIGO AQUÍ ###
```

**Ejercicio 1.2:** Aplica One-Hot Encoding a la columna categórica `contract` usando `pd.get_dummies(..., drop_first=True)` para evitar multicolinealidad. Define la matriz de características `X` (todas las columnas excepto `churn`) y el vector objetivo `y`.

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Parte 2: Regresión Logística y Razón de Momios (*Odds Ratios*)

**Ejercicio 2.1:** Divide el dataset en conjunto de entrenamiento (75%) y conjunto de prueba (25%) utilizando `train_test_split` con `random_state=42` y **estratificación** respecto a la variable `y`.

```python
### TU CÓDIGO AQUÍ ###
```

**Ejercicio 2.2:** Ajusta un modelo `LogisticRegression(max_iter=1000, random_state=42)` sobre `X_train` e `y_train`.
* Construye un DataFrame con los nombres de las variables, los coeficientes $(\beta)$ y los **Odds Ratios** ($e^\beta$).
* Ordena la tabla de mayor a menor según el Odds Ratio e interpreta: ¿Cuál es el factor de mayor riesgo de cancelación y cuál es el mayor factor de retención?

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Parte 3: Diagnóstico y Métricas de Clasificación

**Ejercicio 3.1:** Realiza las predicciones de clase (`y_pred`) y las probabilidades estimadas (`y_proba`) sobre el conjunto de prueba `X_test`.
* Genera y visualiza la **Matriz de Confusión** utilizando `ConfusionMatrixDisplay`.
* Imprime el reporte de clasificación completo (`classification_report`).

```python
### TU CÓDIGO AQUÍ ###
```

**Ejercicio 3.2:** Grafica la **Curva ROC** (*Receiver Operating Characteristic*) calculando la Tasa de Verdaderos Positivos (TPR) y la Tasa de Falsos Positivos (FPR). Calcula e incluye en la leyenda el Área Bajo la Curva (**AUC-ROC**).

```python
### TU CÓDIGO AQUÍ ###
```

**Ejercicio 3.3:** La empresa decide que retener clientes es prioritario y requiere que el modelo alcance una **Sensibilidad (*Recall*) mínima del 85%**.
* Utiliza `precision_recall_curve` para encontrar el umbral de decisión $\tau$ que cumple con este criterio.
* Calcula la nueva matriz de confusión con dicho umbral calibrado y explica qué impacto tuvo sobre los Falsos Negativos.

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Parte 4: Clasificación con $k$-NN, Pipelines y GridSearchCV

**Ejercicio 4.1:** Construye un `Pipeline` en Scikit-Learn que combine:
1. `StandardScaler()` para estandarizar las características numéricas.
2. `KNeighborsClassifier()` como estimador no paramétrico.

```python
### TU CÓDIGO AQUÍ ###
```

**Ejercicio 4.2:** Configura una búsqueda de hiperparámetros con `GridSearchCV`:
* Explora `n_neighbors` entre 3 y 21 (números impares).
* Explora `weights`: `['uniform', 'distance']`.
* Explora `metric`: `['euclidean', 'manhattan']`.
* Utiliza una validación cruzada estratificada `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` optimizando la métrica `roc_auc`.
* Imprime la mejor combinación de hiperparámetros y el mejor puntaje ROC-AUC obtenido.

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Parte 5: Benchmark Comparativo Final y Conclusiones

**Ejercicio 5.1:** Evalúa el mejor modelo de $k$-NN y el modelo de Regresión Logística en el conjunto de prueba independiente `X_test`.
Construye una tabla comparativa que presente:
* Exactitud (*Accuracy*)
* Precisión (Clase Churn)
* Sensibilidad / Recall (Clase Churn)
* $F_1$-Score
* ROC-AUC

```python
### TU CÓDIGO AQUÍ ###
```

**Ejercicio 5.2 (Pregunta de Análisis):** Redacta tu conclusión analítica (máximo 1 párrafo): ¿Cuál de los dos modelos recomendarías para producción en el departamento de retención de clientes y por qué?

```python
# Escribe tu respuesta en un comentario o celda markdown:
# Conclusión del Estudiante:
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
