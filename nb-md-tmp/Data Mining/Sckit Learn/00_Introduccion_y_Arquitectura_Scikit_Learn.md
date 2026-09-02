# 00_Introduccion_y_Arquitectura_Scikit_Learn

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Introducción y Arquitectura de Scikit-Learn ⚙️
      </h1>
      <p style="margin: 6px 0 0 0; color: #1e3a8a; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Minería de Datos (Data Mining) — Edición Estándar (Académica) 📘
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #1e3a8a; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Módulo: Scikit-Learn #00
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Mining/Sckit%20Learn/00_Introduccion_y_Arquitectura_Scikit_Learn.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Objetivos de Aprendizaje 🎯

En este cuaderno inaugural de la asignatura **Minería de Datos (Data Mining)**, exploraremos la arquitectura de ingeniería de software, los principios de diseño y la interfaz unificada de **Scikit-Learn** (`sklearn`), el marco de trabajo de código abierto líder en la industria para el aprendizaje automático y la minería de datos en Python.

Al finalizar este cuaderno, serás capaz de:
1. **Comprender la filosofía de diseño** y la posición de Scikit-Learn dentro de la pila científica de Python (`NumPy`, `SciPy`, `Pandas`, `Matplotlib`).
2. **Dominar los 4 Principios de Diseño de la API** formalizados por Buitinck et al. (2013): *Consistencia*, *Inspección*, *No proliferación de clases* y *Composición*.
3. **Identificar y utilizar las 3 clases principales de objetos**: *Estimators* (Estimadores), *Transformers* (Transformadores) y *Predictors* (Predictores).
4. **Respetar las convenciones de datos bidimensionales**: Matriz de características $\\mathbf{X} \\in \\mathbb{R}^{n \\times p}$ y vector de etiquetas $\\mathbf{y} \\in \\mathbb{R}^n$.
5. **Inspeccionar atributos aprendidos** diferenciándolos de los hiperparámetros mediante la convención del sufijo guion bajo (`_`).
6. **Construir un estimador/transformador personalizado** conforme a la interfaz estándar de Scikit-Learn mediante herencia de `BaseEstimator` y `TransformerMixin`.

> ⚠️ **Alcance Curricular:** Este módulo sienta las bases de ingeniería de software, carga de datos, transformadores y tuberías de Scikit-Learn. Los modelos predictivos específicos (KNN, SVM, Árboles de Decisión, Redes Neuronales) se desarrollan en sus respectivos módulos temáticos independientes.

---
## 1. El Ecosistema Científico y el Rol de Scikit-Learn 🌍

En el flujo metodológico de Minería de Datos (**KDD / CRISP-DM**), Scikit-Learn actúa como el motor central de transformación y modelado:

```
           ┌─────────────────────────────────────────┐
           │        Scikit-Learn (sklearn)           │
           │  (Estimadores, Transformadores, Flujos) │
           └────────────────────┬────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
 ┌──────▼──────┐         ┌──────▼──────┐         ┌──────▼──────┐
 │    NumPy    │         │    SciPy    │         │   Pandas    │
 │ (ndarrays)  │         │ (Matrices)  │         │ (DataFrames)│
 └─────────────┘         └─────────────┘         └─────────────┘
```

### 📦 Verificación del Entorno y Versiones
Ejecutemos la siguiente celda para verificar la disponibilidad y versión de las librerías científicas instaladas:

```python
import sys
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

print(f"🐍 Intérprete Python : {sys.version.split()[0]}")
print(f"🔢 NumPy Versión     : {np.__version__}")
print(f"🔬 SciPy Versión     : {sp.__version__}")
print(f"🐼 Pandas Versión    : {pd.__version__}")
print(f"⚙️ Scikit-Learn Vers : {sklearn.__version__}")
```

---
## 2. Los 4 Principios de Diseño de la API de Scikit-Learn 📐

La consistencia y elegancia de Scikit-Learn radica en su estricto apego a cuatro principios fundamentales:

### 2.1 Consistencia (*Consistency*)
Todos los objetos comparten una interfaz común con un vocabulario de métodos altamente reducido:
* **`fit(X, [y])`**: Ajusta el estimador a partir de los datos de entrenamiento. En transformadores calcula estadísticas ($\mu, \sigma, min, max$); en modelos aprende los pesos/parámetros óptimos.
* **`transform(X)`**: Aplica la transformación aprendida a una matriz $X$.
* **`fit_transform(X, [y])`**: Método optimizado que combina el ajuste y la transformación en una sola pasada eficiente.
* **`predict(X)`**: Genera predicciones para nuevas observaciones.
* **`predict_proba(X)`**: Estima probabilidades condicionales $P(Y=k \mid X)$ (en clasificación).
* **`score(X, y)`**: Devuelve una métrica escalar por defecto (ej. $R^2$ en regresión, *Accuracy* en clasificación).

### 2.2 Inspección (*Inspection*)
* **Hiperparámetros de Entrada:** Se configuran en el constructor `__init__()` y se exponen como atributos públicos con el mismo nombre (ej. `scaler.with_mean`).
* **Parámetros Aprendidos:** Se generan exclusivamente tras ejecutar `.fit()` y **siempre terminan en guion bajo (`_`)** (ej. `scaler.mean_`, `scaler.scale_`, `scaler.var_`).

### 2.3 No Proliferación de Clases (*Non-proliferation of classes*)
Los datos de entrada y salida siempre se representan como arrays estándar de NumPy, matrices dispersas de SciPy (`scipy.sparse`) o DataFrames de Pandas. Nunca se crean clases propietarias contenedoras de datos.

### 2.4 Composición Modular (*Composition*)
Las secuencias de transformaciones y estimadores se combinan en cadenas reutilizables mediante `Pipeline` y `FeatureUnion`.

```python
from sklearn.preprocessing import StandardScaler

# 1. Matriz de características sintética (5 observaciones, 2 variables)
X_ejemplo = np.array([
    [10.0, 200.0],
    [20.0, 300.0],
    [30.0, 400.0],
    [40.0, 500.0],
    [50.0, 600.0]
])

# 2. Instanciación (Configuración de hiperparámetros)
scaler = StandardScaler(with_mean=True, with_std=True)
print("📌 Hiperparámetros configurados en constructor:", scaler.get_params())

# 3. Ajuste: Aprende estadísticas de los datos
scaler.fit(X_ejemplo)

# 4. Inspección de parámetros aprendidos (sufijo '_')
print(f"📊 Medias aprendidas (mean_)       : {scaler.mean_}")
print(f"📊 Varianzas aprendidas (var_)     : {scaler.var_}")
print(f"📊 Escalas / Desv. Std (scale_)   : {scaler.scale_}")
print(f"📊 Muestras procesadas (n_samples_): {scaler.n_samples_seen_}")

# 5. Transformación: z = (x - mean) / scale
X_estandarizado = scaler.transform(X_ejemplo)
print("\n✨ Matriz transformada (Media=0, Varianza=1):\n", X_estandarizado)
```

---
## 3. Tipología Fundamental de Objetos: Estimator, Transformer y Predictor 🧱

```
                     ┌──────────────────┐
                     │    Estimator     │
                     │  Método: fit()   │
                     └────────┬─────────┘
                              │
              ┌───────────────┴───────────────┐
              │                               │
    ┌─────────▼─────────┐           ┌─────────▼─────────┐
    │    Transformer    │           │     Predictor     │
    │ Método:transform()│           │ Método: predict() │
    └───────────────────┘           └───────────────────┘
```

| Tipo de Objeto | Método Principal | Entrada | Salida | Ejemplo Clave |
|---|---|---|---|---|
| **Estimador (`Estimator`)** | `.fit(X, [y])` | Datos $X$, etiquetas $y$ (opcional) | `self` (el objeto ajustado) | Cualquier transformador o modelo |
| **Transformador (`Transformer`)** | `.transform(X)` | Datos $X$ | Matriz transformada $X_{trans}$ | `StandardScaler`, `OneHotEncoder` |
| **Predictor (`Predictor`)** | `.predict(X)` | Datos $X$ no vistos | Vector de predicciones $\hat{y}$ | Modelos de clasificación y regresión |

---
## 4. Convenciones de Formas Matriciales ($X$ e $y$) 📊

$$\\mathbf{X} = \\begin{pmatrix} 
x_{11} & x_{12} & \\cdots & x_{1p} \\\\ 
x_{21} & x_{22} & \\cdots & x_{2p} \\\\ 
\\vdots & \\vdots & \\ddots & \\vdots \\\\ 
x_{n1} & x_{n2} & \\cdots & x_{np} 
\\end{pmatrix} \\in \\mathbb{R}^{n \\times p}, \\quad
\\mathbf{y} = \\begin{pmatrix} y_1 \\\\ y_2 \\\\ \\vdots \\\\ y_n \\end{pmatrix} \\in \\mathbb{R}^n$$

* **$n$ (Filas / `n_samples`):** Número de observaciones independientes (clientes, transacciones, registros).
* **$p$ (Columnas / `n_features`):** Número de variables predictoras o atributos numéricos/categóricos.
* **$y$ (Vector / `n_targets`):** Array unidimensional de longitud $n$ con las etiquetas de clase o valores continuos.

```python
# Validación rigurosa de dimensiones
print(f"Forma de X_ejemplo: {X_ejemplo.shape} -> ({X_ejemplo.shape[0]} muestras, {X_ejemplo.shape[1]} variables)")
assert X_ejemplo.ndim == 2, "La matriz X DEBE ser estrictamente 2D"

y_ejemplo = np.array([0, 1, 0, 1, 1])
print(f"Forma de y_ejemplo: {y_ejemplo.shape} -> ({len(y_ejemplo)} etiquetas)")
assert y_ejemplo.ndim == 1, "El vector y común DEBE ser 1D"
assert len(X_ejemplo) == len(y_ejemplo), "El número de muestras en X e y debe coincidir exactamente"
print("✅ Convenciones dimensionales validadas con éxito.")
```

---
## 5. Práctica Guiada: Creación de un Transformador Personalizado 🛠️

En proyectos reales de minería de datos, con frecuencia necesitamos transformaciones específicas de negocio. Podemos crear transformadores 100% compatibles con Scikit-Learn heredando de:
* `BaseEstimator`: Proporciona métodos gratuitos de gestión de hiperparámetros (`get_params()`, `set_params()`).
* `TransformerMixin`: Proporciona automáticamente el método optimizado `fit_transform()`.

A continuación, implementaremos un transformador que realiza un recorte de valores atípicos (*Winsorization / Clipping*) entre los percentiles $p_{low}$ y $p_{high}$ de cada columna:

```python
from sklearn.base import BaseEstimator, TransformerMixin

class PercentileClipper(BaseEstimator, TransformerMixin):
    """
    Transformador personalizado que recorta valores extremos 
    según percentiles calculados en el conjunto de entrenamiento.
    """
    def __init__(self, lower_percentile=5.0, upper_percentile=95.0):
        self.lower_percentile = lower_percentile
        self.upper_percentile = upper_percentile
        
    def fit(self, X, y=None):
        X_arr = np.asarray(X)
        # Aprender los umbrales inferior y superior por columna
        self.lower_bounds_ = np.percentile(X_arr, self.lower_percentile, axis=0)
        self.upper_bounds_ = np.percentile(X_arr, self.upper_percentile, axis=0)
        self.n_features_in_ = X_arr.shape[1]
        return self  # Siempre retornar self para permitir encadenamiento
        
    def transform(self, X):
        # Validar que fit haya sido ejecutado
        if not hasattr(self, 'lower_bounds_'):
            raise RuntimeError("El transformador debe ser ajustado con fit() antes de transform()")
        X_arr = np.asarray(X)
        # Aplicar recorte por columna
        return np.clip(X_arr, self.lower_bounds_, self.upper_bounds_)

# Prueba del transformador personalizado
np.random.seed(42)
datos_contaminados = np.array([
    [10.0], [12.0], [14.0], [11.0], [13.0], [15.0], [12.0], [100.0], [-50.0] # Outliers
])

clipper = PercentileClipper(lower_percentile=10.0, upper_percentile=90.0)
datos_recortados = clipper.fit_transform(datos_contaminados)

print("📌 Límite inferior aprendido (lower_bounds_):", clipper.lower_bounds_)
print("📌 Límite superior aprendido (upper_bounds_):", clipper.upper_bounds_)
print("\nDatos Originales vs Recortados:")
for orig, rec in zip(datos_contaminados.ravel(), datos_recortados.ravel()):
    print(f"  Original: {orig:6.1f}  ->  Recortado: {rec:6.1f}")
```

---
## 6. Actividades y Desafíos Prácticos 🧪

### 🛠️ Práctica 1.1: Inspección de MinMaxScaler
Instancia un objeto `MinMaxScaler` con `feature_range=(-1, 1)`. Ajusta el transformador sobre `X_ejemplo` y extrae mediante código los siguientes atributos aprendidos:
1. `data_min_` (Mínimos por columna).
2. `data_max_` (Máximos por columna).
3. `data_range_` (Rango de cada columna).

```python
# Escribe tu solución aquí
from sklearn.preprocessing import MinMaxScaler

# 1. Instanciar scaler con feature_range=(-1, 1)
# 2. Ajustar con fit()
# 3. Imprimir atributos aprendidos
# minmax_custom = ...
```

---
### 🛠️ Práctica 1.2: Transformador de Estandarización Manual
Completa el siguiente transformador `CustomStandardizer` implementando los métodos `fit` y `transform` desde cero utilizando solo operaciones vectoriales de NumPy:

```python
class CustomStandardizer(BaseEstimator, TransformerMixin):
    def __init__(self, with_mean=True, with_std=True):
        self.with_mean = with_mean
        self.with_std = with_std
        
    def fit(self, X, y=None):
        X_arr = np.asarray(X)
        # TODO: Calcular media (mean_) y desviación estándar (scale_) por columna
        # self.mean_ = ...
        # self.scale_ = ...
        return self
        
    def transform(self, X):
        X_arr = np.asarray(X)
        # TODO: Aplicar z = (x - mean) / scale según los hiperparámetros
        return X_arr

# Comprueba tu implementación:
# custom_std = CustomStandardizer()
# X_res = custom_std.fit_transform(X_ejemplo)
# print(X_res)
```

---
## 7. Preguntas de Autoevaluación 🧠

1. **¿Por qué Scikit-Learn no utiliza métodos como `scaler.compute_statistics()` o `model.train()`?**  
   *R:* Para mantener el principio de **Consistencia**; todos los objetos que aprenden parámetros usan unívocamente el método `fit()`.
2. **¿Cuál es la diferencia entre un hiperparámetro y un parámetro estimado?**  
   *R:* El hiperparámetro lo define el científico de datos en el constructor `__init__`, mientras que el parámetro estimado lo calcula el algoritmo automáticamente durante `fit()` y se identifica con el sufijo `_`.
3. **¿Qué sucede si intentas ejecutar `.transform()` antes de `.fit()`?**  
   *R:* Se genera una excepción (típicamente `NotFittedError`) porque las estadísticas necesarias para transformar los datos no han sido calculadas.

---
## Resumen del Módulo & Referencias 📚

| Concepto | Definición Clave |
|---|---|
| **Estimador (`Estimator`)** | Objeto que aprende de los datos mediante `fit(X, [y])`. |
| **Transformador (`Transformer`)** | Estimador que modifica datos mediante `transform(X)` o `fit_transform(X)`. |
| **Predictor (`Predictor`)** | Estimador capaz de inferir etiquetas mediante `predict(X)`. |
| **Atributo Aprendido** | Variable interna generada tras `fit()`, identificada con sufijo `_` (ej. `scaler.mean_`). |

### 📖 Bibliografía de Referencia:
1. **Buitinck, L. et al. (2013).** *API design for machine learning software: experiences from the scikit-learn project*. arXiv:1309.0238.
2. **Garreta, R., & Moncecchi, G. (2013).** *Learning scikit-learn: Machine Learning in Python*. Packt Publishing.
3. **Pedregosa, F. et al. (2011).** *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825-2830.
