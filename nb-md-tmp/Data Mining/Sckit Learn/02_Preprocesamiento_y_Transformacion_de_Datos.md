# 02_Preprocesamiento_y_Transformacion_de_Datos

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Preprocesamiento y Transformación de Datos 🛠️
      </h1>
      <p style="margin: 6px 0 0 0; color: #1e3a8a; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Minería de Datos (Data Mining)
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #1e3a8a; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Módulo 02
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Mining/Sckit%20Learn/02_Preprocesamiento_y_Transformacion_de_Datos.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

```python
# Configuración del entorno interactivo
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"
except ImportError:
    pass

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

print(f"🚀 Entorno listo con Scikit-Learn versión: {sklearn.__version__}")
```

---
## Objetivos de Aprendizaje 🎯

En este cuaderno aprenderás a transformar y acondicionar datos tabulares mediante `sklearn.preprocessing` e `sklearn.impute`:

* **1. Escalamiento Numérico:** Fundamentos matemáticos de `StandardScaler`, `MinMaxScaler`, `RobustScaler` y `Normalizer`.
* **2. Imputación de Datos Faltantes:** Imputación univariada (`SimpleImputer`) y multivariada basada en distancias (`KNNImputer`).
* **3. Codificación Categórica:** Transformación con `OneHotEncoder` (manejo de categorías raras y desconocidas) y `OrdinalEncoder`.
* **4. Discretización y Polinomios:** Segmentación con `KBinsDiscretizer` e interacciones no lineales con `PolynomialFeatures`.
* **5. Funciones Arbitrarias:** Transformaciones personalizadas con `FunctionTransformer` (ej. logaritmos, raíces).

---
### 1. Escalamiento y Normalización de Variables 📏

$$\text{StandardScaler: } z = \frac{x - \mu}{\sigma}, \quad \text{MinMaxScaler: } x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}, \quad \text{RobustScaler: } x_{rob} = \frac{x - Q_2}{IQR}$$

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Generación de datos con presencia de Outliers severos
np.random.seed(42)
datos_base = np.random.normal(loc=50, scale=10, size=200)
outliers = np.array([180.0, 210.0, -30.0])
datos_crudos = np.concatenate([datos_base, outliers]).reshape(-1, 1)

scaler_std = StandardScaler().fit_transform(datos_crudos)
scaler_minmax = MinMaxScaler().fit_transform(datos_crudos)
scaler_robust = RobustScaler().fit_transform(datos_crudos)

fig, axes = plt.subplots(1, 4, figsize=(14, 3.5))
axes[0].hist(datos_crudos, bins=25, color='#475569', edgecolor='k')
axes[0].set_title("Original (con Outliers)", fontweight='bold')
axes[1].hist(scaler_std, bins=25, color='#2563eb', edgecolor='k')
axes[1].set_title(r"StandardScaler (\mu=0, \sigma=1)", fontweight='bold')
axes[2].hist(scaler_minmax, bins=25, color='#059669', edgecolor='k')
axes[2].set_title("MinMaxScaler ([0, 1])", fontweight='bold')
axes[3].hist(scaler_robust, bins=25, color='#d97706', edgecolor='k')
axes[3].set_title("RobustScaler (Mediana=0, IQR=1)", fontweight='bold')

for ax in axes:
    ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---
### 2. Imputación y Codificación Categórica 🧩

* **`SimpleImputer`:** Reemplaza valores nulos (`NaN`) por estadísticos (`mean`, `median`, `most_frequent`, `constant`).
* **`OneHotEncoder`:** Crea una columna indicadora binaria por categoría, con `handle_unknown='ignore'` para blindar producción.

```python
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

df_demo = pd.DataFrame({
    'Edad': [25.0, np.nan, 45.0, 32.0, np.nan],
    'Ciudad': ['Tunja', 'Bogotá', 'Tunja', 'Duitama', 'Bogotá'],
    'Ingresos': [2500.0, 3200.0, 5800.0, 4100.0, 2900.0]
})

# 1. Imputación de Edad con Mediana
imputer = SimpleImputer(strategy='median')
df_demo['Edad'] = imputer.fit_transform(df_demo[['Edad']])

# 2. Codificación One-Hot de Ciudad
ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
ciudades_ohe = ohe.fit_transform(df_demo[['Ciudad']])
df_ciudades = pd.DataFrame(ciudades_ohe, columns=ohe.get_feature_names_out(['Ciudad']))

print("DataFrame con Edad Imputada y Ciudad Codificada:")
display(pd.concat([df_demo[['Edad', 'Ingresos']], df_ciudades], axis=1))
```

---
#### 🛠️ Práctica: Preprocesamiento de Datos

**Ejercicio 1:**
Dado un dataset con la variable `Salario` contaminada con un valor extremo (`1_000_000`), aplica `RobustScaler` y `StandardScaler`. Muestra cómo la mediana permanece en 0.0 con `RobustScaler` mientras `StandardScaler` es distorsionado.

```python
# Ejercicio 1
# Escribe tu código aquí
salarios = np.array([[2000.0], [2200.0], [2500.0], [2100.0], [2400.0], [1_000_000.0]])

# std_res = ...
# rob_res = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Solución Ejercicio 1
std_res = StandardScaler().fit_transform(salarios)
rob_res = RobustScaler().fit_transform(salarios)

print("StandardScaler:\n", std_res.ravel().round(2))
print("\nRobustScaler:\n", rob_res.ravel().round(2))
print(f"Mediana con RobustScaler: {np.median(rob_res):.2f}")
```
</details>

**Ejercicio 2:**
Utiliza `FunctionTransformer` con `np.log1p` para aplicar una transformación logarítmica $\log(1+x)$ sobre ingresos asimétricos, estabilizando la varianza.

```python
# Ejercicio 2
# Escribe tu código aquí
from sklearn.preprocessing import FunctionTransformer

ingresos_asimetricos = np.array([[100.0], [500.0], [10000.0], [500000.0]])

# log_trans = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Solución Ejercicio 2
log_trans = FunctionTransformer(np.log1p, validate=True)
ingresos_log = log_trans.fit_transform(ingresos_asimetricos)

print("Ingresos Originales:\n", ingresos_asimetricos.ravel())
print("\nIngresos Transformados Log(1+x):\n", ingresos_log.ravel().round(2))
```
</details>

---
### Resumen y Preguntas de Autoevaluación 🧠

1. **¿Por qué `RobustScaler` es superior a `StandardScaler` en presencia de outliers?**  
   *Respuesta:* Porque utiliza la mediana y el rango intercuartílico ($IQR = Q_3 - Q_1$), los cuales no son afectados por valores extremos anormales.
2. **¿Qué previene el parámetro `handle_unknown='ignore'` en `OneHotEncoder`?**  
   *Respuesta:* Evita caídas del sistema cuando entran categorías no vistas en el entrenamiento durante la inferencia en producción, asignando ceros en todas las columnas indicadoras.
3. **¿Por qué `fit_transform` solo debe usarse en datos de entrenamiento?**  
   *Respuesta:* Para prevenir *Data Leakage*; los datos de prueba solo deben transformarse con las estadísticas aprendidas del entrenamiento (`transform`).

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Minería de Datos (Data Mining)</i>
  </p>
</div>
