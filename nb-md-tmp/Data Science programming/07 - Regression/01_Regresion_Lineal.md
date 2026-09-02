# 01_Regresion_Lineal

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Regresión Lineal 📐
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
        Módulo 07
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/07%20-%20Regression/01_Regresion_Lineal.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
### 1. ¿Qué es la Regresión Lineal? 🧠

La **Regresión Lineal** es un algoritmo de **Aprendizaje Supervisado** utilizado para predecir una variable cuantitativa continua objetivo (*target* o variable dependiente $y \in \mathbb{R}$). Aunque es un enfoque clásico frente a técnicas más complejas, sigue siendo uno de los métodos más sólidos, interpretables y fundamentales de la Ciencia de Datos. De hecho, muchas técnicas avanzadas son extensiones directas de la regresión lineal básica.

Utilizando la recta (o hiperplano) de mejor ajuste (*best fitting line*), establece la relación funcional entre la variable dependiente y una o más variables independientes. Funciona bajo el principio de **Mínimos Cuadrados Ordinarios (*Ordinary Least Squares - OLS*)**, cuyo objetivo estadístico es estimar los parámetros desconocidos minimizando la suma de los cuadrados de las diferencias entre los valores observados y las predicciones.

---
### 2. ¿Por qué utilizar Regresión Lineal? 💡

* **Modelo Simple y Computacionalmente Eficiente:** Rapidez de cálculo y escalabilidad a millones de registros.
* **Interpretabilidad Directa:** Proporciona una descripción clara y transparente de cómo las entradas afectan a la salida (esencial para inferencia y comités de negocio).
* **Excelente Capacidad Predictiva en Muestras Reducidas:** Supera frecuentemente a modelos no lineales complejos cuando la muestra de entrenamiento es pequeña, existe baja relación señal-ruido (*low signal-to-noise ratio*) o los datos son dispersos.
* **Facilidad de Comunicación:** Sencillo de explicar a audiencias interdisciplinarias.
* **Inferencia Estadística Rigurosa:** Permite calcular errores estándar, intervalos de confianza del 95% y pruebas de hipótesis ($p$-valores).

<div align="center">
  <img src="images/top_ml_algorithms.png" width="600" alt="Top 12 Machine Learning Algorithms - Kaggle Survey" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin: 15px 0;"/>
  <p style="font-size: 0.85em; color: #64748b;">
    <i>Figura: La regresión lineal y logística se mantiene como la familia de modelos más utilizada por científicos de datos en todo el mundo (<a href="https://www.kaggle.com/kaggle-survey-2022">Kaggle Annual Survey</a>).</i>
  </p>
</div>

---
### 3. ¿Cómo utilizar la Regresión Lineal: Inferencia vs Predicción? ⚖️

La regresión lineal se puede emplear bajo dos perspectivas fundamentales:

```
                           ┌──────────────────────────────┐
                           │    Objetivo del Modelado     │
                           └──────────────┬───────────────┘
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
      ┌───────────────────────┐                       ┌───────────────────────┐
      │  Inferencia (Explicar)│                       │ Predicción (Predecir) │
      └───────────────────────┘                       └───────────────────────┘
        • ¿Cómo se genera Y?                            • Estimar Y con mínimo error
        • Efecto de cada variable                       • Generalización sobre test
        • p-valores y confianza                         • Minimizar RMSE / Maximizar R²
```

* **Inferencia (*Inference*):** Dado un conjunto de datos, deseamos inferir cómo se genera la salida en función de las variables de entrada.  
  *Ejemplo Titanic:* Estimar el efecto de la Edad, la Clase de Pasajero y el Género sobre la probabilidad de supervivencia e interpretar sus coeficientes.
* **Predicción (*Prediction*):** Dada una nueva observación, queremos utilizar el modelo ajustado para predecir el resultado de forma precisa.  
  *Ejemplo Titanic:* Elegir si un pasajero sobrevive o fallece ({vive, muere}) maximizando la tasa de aciertos.

---
### 4. Ecuaciones Matemáticas de la Regresión Lineal 📐

Utilizaremos $x$ para denotar la variable independiente y $y$ para denotar la variable dependiente. Un par $(x^{(i)}, y^{(i)})$ se denomina **ejemplo de entrenamiento** en un conjunto de $m$ observaciones ($i = 1, 2, \dots, m$).

#### 4.1 Regresión Lineal Simple (Univariada):
El objetivo es aprender una función de hipótesis $h_\theta(x)$ para estimar $y$:

$$h_\theta(x) = \theta_0 + \theta_1 x$$

Donde $\theta_0$ y $\theta_1$ son los parámetros de la hipótesis (intercepto y pendiente).

#### 4.2 Formulación General para $n$ Variables Predictoras:
Si disponemos de $n$ variables predictoras $(x_1, x_2, \dots, x_n)$:

$$h_\theta(\mathbf{x}) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n = \theta_0 + \sum_{j=1}^n \theta_j x_j$$

Donde:
* $\theta_j$: Parámetros de la hipótesis.
* $m$: Número de ejemplos de entrenamiento.
* $n$: Número de variables independientes.
* $x_j^{(i)}$: Valor de la $j$-ésima característica en el $i$-ésimo ejemplo de entrenamiento.

---
### 5. Flujo de Trabajo con Scikit-Learn y Formato de Datos 🛠️

**Scikit-Learn** es uno de los marcos de Machine Learning más completos y eficientes en Python. Proporciona una API uniforme y coherente basada en arreglos de NumPy y DataFrames de Pandas:

* **Matriz de Características ($\mathbf{X}$):** Contiene todas las muestras del conjunto de entrenamiento. Su forma es `[n_samples, n_features]`. Las filas representan las observaciones y las columnas las diferentes características.
* **Arreglo Objetivo ($\mathbf{y}$):** Especifica el valor objetivo continuo a predecir. Su forma es `[n_samples]` (o `[n_samples, 1]`).

#### Pasos Estándar de la API:
1. **Selección del Modelo:** Importar la clase del estimador (e.g. `LinearRegression`).
2. **Selección de Hiperparámetros:** Instanciar el objeto configurando sus parámetros (e.g. `fit_intercept=True`).
3. **Procesamiento y Partición:** Organizar $\mathbf{X}$ e $\mathbf{y}$, dividiendo en entrenamiento y prueba (`train_test_split`).
4. **Ajuste del Modelo (*Fit*):** Entrenar el modelo mediante el método `estimator.fit(X, y)`.
5. **Predicción y Evaluación (*Predict*):** Generar predicciones con `estimator.predict(X_test)` y calcular métricas.

```python
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = 'all'
except Exception:
    pass
try:
    from IPython.display import display
except Exception:
    pass

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Modelado y evaluación con Scikit-Learn
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Inferencia y diagnóstico estadístico
from statsmodels.stats.stattools import durbin_watson

# Configuración visual
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)
plt.rcParams["font.size"] = 10

np.random.seed(0)
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 6)

print("✅ Bibliotecas importadas y entorno configurado correctamente.")
```

---
### 6. Carga y Exploración del Dataset de Inversión Publicitaria (*Advertising Dataset*) 📊

El dataset **`Advertising.csv`** registra los ingresos por ventas (`Sales`, en miles de unidades) generados a partir de los presupuestos invertidos en tres canales publicitarios: **TV**, **Radio** y **Newspaper** (en miles de dólares).

```python
import os
import urllib.parse
import urllib.request
import pandas as pd

# 🚀 Función de utilidad para cargar datasets de forma segura (Local o Google Colab)
def load_dataset(filename, module_name="07 - Regression"):
    candidates = [
        f"data/{filename}",
        f"{module_name}/data/{filename}",
        filename
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
            
    os.makedirs("data", exist_ok=True)
    target_path = f"data/{filename}"
    encoded_module = urllib.parse.quote(module_name)
    encoded_file = urllib.parse.quote(filename)
    url_main = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/{encoded_module}/data/{encoded_file}"
    url_master = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/master/{encoded_module}/data/{encoded_file}"
    
    print(f"📥 Descargando dataset '{filename}' desde el repositorio oficial...")
    try:
        urllib.request.urlretrieve(url_main, target_path)
    except Exception:
        urllib.request.urlretrieve(url_master, target_path)
    print(f"✅ Dataset '{filename}' cargado exitosamente.")
    return target_path

# 1. Carga del conjunto de datos Advertising
file_path = load_dataset('Advertising.csv', '07 - Regression')
adv_data = pd.read_csv(file_path)

# 2. Eliminamos la columna de índice si existe y seleccionamos las variables
if 'Unnamed: 0' in adv_data.columns:
    adv_data = adv_data[['TV', 'Radio', 'Newspaper', 'Sales']]

# 3. Primeras filas y dimensiones
display(adv_data.head())
print('\nNúmero de filas y columnas en el dataset:', adv_data.shape)
```

El dataset contiene $m = 200$ ejemplos de entrenamiento y $n = 3$ variables independientes (`TV`, `Radio`, `Newspaper`) con `Sales` como variable objetivo.

La función de hipótesis para este conjunto de datos se formula como:

$$h_\theta(\mathbf{x}_i) = \theta_0 + \theta_1 \text{TV} + \theta_2 \text{Radio} + \theta_3 \text{Newspaper}$$

Para ejemplos individuales observados:

$$\text{Si } i = 1 \implies h_\theta(\mathbf{x}_1) = \theta_0 + \theta_1 (230.1) + \theta_2 (37.8) + \theta_3 (69.2), \quad y_1 = 22.1$$

$$\text{Si } i = 3 \implies h_\theta(\mathbf{x}_3) = \theta_0 + \theta_1 (17.2) + \theta_2 (45.9) + \theta_3 (69.3), \quad y_3 = 9.3$$

Vectorialmente para una muestra $i$:
$$\mathbf{x}_i = (x_{i1}, x_{i2}, x_{i3}) = (\text{TV}_i, \text{Radio}_i, \text{Newspaper}_i)$$

#### Formulación Matricial Global:
Agrupando todos los vectores individuales en una matriz $\mathbf{X}$ de tamaño $(m, n)$ y los vectores de parámetros y respuestas:

$$\mathbf{X} = \begin{pmatrix} x_{11} & x_{12} & x_{13} \\ x_{21} & x_{22} & x_{23} \\ \vdots & \vdots & \vdots \\ x_{m1} & x_{m2} & x_{m3} \end{pmatrix}_{(m, n)}, \quad \boldsymbol{\theta} = \begin{pmatrix} \theta_0 \\ \theta_1 \\ \vdots \\ \theta_n \end{pmatrix}_{(n+1, 1)}, \quad \mathbf{y} = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_m \end{pmatrix}_{(m, 1)}$$

La función de hipótesis en forma vectorial se expresa como:
$$h_\theta(\mathbf{x}) = \mathbf{X}\boldsymbol{\theta}$$

```python
# Preparación de las matrices NumPy
X_features = ['TV', 'Radio', 'Newspaper']
X = adv_data[X_features].to_numpy() # X.shape = [200, 3]
y = adv_data['Sales'].to_numpy()      # y.shape = [200]

print("Dimensiones de X:", X.shape)
print("Dimensiones de y:", y.shape)

# Visualización de relaciones bivariadas
sns.pairplot(adv_data, height=2.3, diag_kind='kde', plot_kws={'alpha': 0.7, 'color': '#1e3a8a'})
plt.suptitle('Relaciones Bivariadas: Canales Publicitarios vs Ventas', y=1.02, fontsize=12, fontweight='bold')
plt.show()
```

---
### 7. El Método de Mínimos Cuadrados Ordinarios (*Least Squares Method*) ⚖️

#### 7.1 Función de Costo (*Cost Function*):
La función de costo mide el error cometido por el modelo al estimar la relación entre $\mathbf{x}$ y $y$:

$$J(\boldsymbol{\theta}) = \frac{1}{m} \sum_{i=1}^m (\hat{y}_i - y_i)^2 = \frac{1}{m} \sum_{i=1}^m \left(h_\theta(\mathbf{x}_i) - y_i\right)^2$$

Para implementar la regresión lineal, añadimos una columna adicional $x_0 = 1$ a cada muestra $(x_{10}, x_{20}, \dots, x_{m0} = 1)$, transformando la matriz de características en:

$$\mathbf{X} = \begin{pmatrix} x_{10} & x_{11} & x_{12} & \dots & x_{1n} \\ x_{20} & x_{21} & x_{22} & \dots & x_{2n} \\ x_{30} & x_{31} & x_{32} & \dots & x_{3n} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ x_{m0} & x_{m1} & x_{m2} & \dots & x_{mn} \end{pmatrix}_{(m, n+1)}$$

Reescribiendo la función de costo en notación matricial compacta:

$$J(\boldsymbol{\theta}) = \frac{1}{m} (\mathbf{X}\boldsymbol{\theta} - \mathbf{y})^T (\mathbf{X}\boldsymbol{\theta} - \mathbf{y})$$

> 💡 **Nota de Multiplicación Matricial:**  
> La matriz $\mathbf{X}$ es de tamaño $(m, n+1)$, el vector $\boldsymbol{\theta}$ es de tamaño $(n+1, 1)$ y $\mathbf{y}$ es de tamaño $(m, 1)$. El producto $\mathbf{X}_{(m, n+1)}\boldsymbol{\theta}_{(n+1, 1)}$ produce un vector de tamaño $(m, 1)$, y el producto cuadrático $(\mathbf{X}\boldsymbol{\theta} - \mathbf{y})^T_{(1, m)} (\mathbf{X}\boldsymbol{\theta} - \mathbf{y})_{(m, 1)}$ retorna un escalar.

#### 7.2 Ecuación Normal (*Normal Equation*):
La **Ecuación Normal** es la solución analítica exacta al problema de regresión lineal con función de costo OLS. Para minimizar el costo, tomamos la derivada parcial de $J(\boldsymbol{\theta})$ respecto a $\boldsymbol{\theta}$ e igualamos a cero:

$$\min_{\theta_0, \theta_1, \dots, \theta_n} J(\theta_0, \theta_1, \dots, \theta_n) \implies \frac{\partial J(\theta_j)}{\partial \theta_j} = 0 \quad \text{para } j = 0, 1, 2, \dots, n$$

$$\frac{\partial J(\boldsymbol{\theta})}{\partial \boldsymbol{\theta}} = \frac{\partial}{\partial \boldsymbol{\theta}} \left[ \frac{1}{m} (\mathbf{X}\boldsymbol{\theta} - \mathbf{y})^T (\mathbf{X}\boldsymbol{\theta} - \mathbf{y}) \right] = \mathbf{0}$$

Desarrollando el producto vectorial interno:

$$J(\boldsymbol{\theta}) = (\mathbf{X}\boldsymbol{\theta} - \mathbf{y})^T (\mathbf{X}\boldsymbol{\theta} - \mathbf{y}) = \left( (\mathbf{X}\boldsymbol{\theta})^T - \mathbf{y}^T \right) (\mathbf{X}\boldsymbol{\theta} - \mathbf{y})$$

$$= \left(\boldsymbol{\theta}^T \mathbf{X}^T - \mathbf{y}^T\right)(\mathbf{X}\boldsymbol{\theta} - \mathbf{y}) = \boldsymbol{\theta}^T \mathbf{X}^T \mathbf{X} \boldsymbol{\theta} - \mathbf{y}^T \mathbf{X} \boldsymbol{\theta} - \boldsymbol{\theta}^T \mathbf{X}^T \mathbf{y} + \mathbf{y}^T \mathbf{y}$$

Dado que $\mathbf{y}^T \mathbf{X} \boldsymbol{\theta} = \boldsymbol{\theta}^T \mathbf{X}^T \mathbf{y}$ (por ser cantidades escalares idénticas de dimensión $1 \times 1$):

$$J(\boldsymbol{\theta}) = \boldsymbol{\theta}^T \mathbf{X}^T \mathbf{X} \boldsymbol{\theta} - 2 \boldsymbol{\theta}^T \mathbf{X}^T \mathbf{y} + \mathbf{y}^T \mathbf{y}$$

Aplicando las reglas de cálculo matricial ($\frac{\partial (\mathbf{x}^T \mathbf{A} \mathbf{x})}{\partial \mathbf{x}} = 2 \mathbf{A}\mathbf{x}$, $\frac{\partial (\mathbf{a}^T \mathbf{x})}{\partial \mathbf{x}} = \mathbf{a}$ y $\frac{\partial \mathbf{C}}{\partial \mathbf{x}} = 0$):

$$\frac{\partial J(\boldsymbol{\theta})}{\partial \boldsymbol{\theta}} = 2 \mathbf{X}^T \mathbf{X} \boldsymbol{\theta} - 2 \mathbf{X}^T \mathbf{y} + \mathbf{0}$$

Igualando a cero:
$$\mathbf{0} = 2 \mathbf{X}^T \mathbf{X} \boldsymbol{\theta} - 2 \mathbf{X}^T \mathbf{y}$$
$$\mathbf{X}^T \mathbf{X} \boldsymbol{\theta} = \mathbf{X}^T \mathbf{y}$$

Multiplicando por la inversa $(\mathbf{X}^T \mathbf{X})^{-1}$:

$$\boldsymbol{\theta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$

Esta es la **Ecuación Normal** fundamental de la Regresión Lineal.

---
### 8. Construcción del Modelo: Train-Test Split y Comparativa Manual vs Scikit-Learn 🏗️

Dividimos los datos en subconjuntos:
* **Training Set:** Datos observados para estimar los parámetros del modelo.
* **Validation Set:** Para comparar modelos y ajustar hiperparámetros.
* **Test Set:** Para reportar el desempeño final sobre datos no vistos previamente.

```python
# Partición del conjunto de datos en Entrenamiento (70%) y Prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=23)

print("Tamaño Train:", X_train.shape[0])
print("Tamaño Test: ", X_test.shape[0])
```

```python
# =========================================================================
# 1. Solución Analítica con la Ecuación Normal (NumPy)
# =========================================================================

# Paso 1: Añadir la columna x_0 = 1
X_train_0 = np.c_[np.ones((X_train.shape[0], 1)), X_train]
X_test_0 = np.c_[np.ones((X_test.shape[0], 1)), X_test]

# Paso 2: theta = (X^T X)^(-1) X^T y
theta = np.matmul(np.linalg.inv(np.matmul(X_train_0.T, X_train_0)), np.matmul(X_train_0.T, y_train))

# DataFrame con los parámetros aprendidos
parameter = ['theta_' + str(i) for i in range(X_train_0.shape[1])]
columns = ['intercept'] + list(adv_data[X_features].columns.values)
parameter_df = pd.DataFrame({'Parameter': parameter, 'Columns': columns, 'theta': theta})

# =========================================================================
# 2. Modelo con el Módulo de Scikit-Learn
# =========================================================================
lin_reg = LinearRegression(fit_intercept=True)
lin_reg.fit(X_train, y_train)

sk_theta = [lin_reg.intercept_] + list(lin_reg.coef_)
parameters = parameter_df.join(pd.Series(sk_theta, name='Sklearn_theta'))
display(parameters)
```

---
### 9. Evaluación del Modelo de Regresión (*Model Evaluation*) 📏

#### 9.1 Error Cuadrático Medio (*Mean Squared Error - MSE*):
Prediciendo sobre el conjunto de test y comparando con los valores reales:

$$\text{MSE} = \frac{1}{m} \sum_{i=1}^m (\hat{y}_i - y_i)^2$$

#### 9.2 Coeficiente de Determinación ($R^2$ - *R-squared*):
Mide la proporción de la variabilidad total en la variable dependiente $y$ que es explicada por las variables independientes $\mathbf{X}$. Sus valores oscilan en $(-\infty, 1]$:

$$R^2 = 1 - \frac{\text{RSS}}{\text{TSS}}$$

$$\text{RSS} = \sum_{i=1}^m (\hat{y}_i - y_i)^2 \quad (\text{Residual Sum of Squares})$$

$$\text{TSS} = \sum_{i=1}^m (y_i - \bar{y})^2 \quad (\text{Total Sum of Squares})$$

Donde $\hat{y}_i$ es el valor predicho y $\bar{y}$ es la media observada de $y$.

#### 9.3 Otras Métricas Clave de Regresión:
* **Root Mean Squared Error (RMSE):** En la misma unidad original de $y$:
  $$\text{RMSE} = \sqrt{\frac{1}{m} \sum_{i=1}^m (\hat{y}_i - y_i)^2}$$
* **Mean Absolute Error (MAE):** Penaliza linealmente los errores, ofreciendo alta interpretabilidad:
  $$\text{MAE} = \frac{1}{m} \sum_{i=1}^m |\hat{y}_i - y_i|$$
* **Mean Squared Log Error (MSLE):** Para variables con crecimiento exponencial:
  $$\text{MSLE} = \frac{1}{m} \sum_{i=1}^m \left(\log(1 + \hat{y}_i) - \log(1 + y_i)\right)^2$$
* **Mean Absolute Percentage Error (MAPE):** Error porcentual relativo medio:
  $$\text{MAPE} = \frac{1}{m} \sum_{i=1}^m \left| \frac{y_i - \hat{y}_i}{y_i + \epsilon} \right| \times 100\%$$

```python
# Evaluación con la Ecuación Normal
y_pred_norm = np.matmul(X_test_0, theta)
mse_norm = np.sum((y_pred_norm - y_test)**2) / X_test_0.shape[0]
rss = np.sum((y_pred_norm - y_test)**2)
tss = np.sum((y_test - y_test.mean())**2)
R_squared_norm = 1 - (rss / tss)

print("=" * 55)
print("EVALUACIÓN: ECUACIÓN NORMAL (NUMPY)")
print("=" * 55)
print('The Mean Squared Error (MSE) is: ', mse_norm)
print('R squared obtained from the normal equation method is:', R_squared_norm)

# Evaluación con Scikit-Learn
y_pred_sk = lin_reg.predict(X_test)
mse_sk = mean_squared_error(y_pred_sk, y_test)
R_squared_sk = lin_reg.score(X_test, y_test)

print("\n" + "=" * 55)
print("EVALUACIÓN: SCIKIT-LEARN")
print("=" * 55)
print('The Mean Squared Error (MSE) is: ', mse_sk)
print('R squared obtained from scikit learn library is :', R_squared_sk)
print("=" * 55)
print(f"El modelo explica el {R_squared_sk*100:.2f}% de la variabilidad de las ventas.")
```

---
### 10. Diagnóstico de los Supuestos de la Regresión Lineal (*Linear Regression Assumptions*) 📋

Para que las estimaciones OLS sean óptimas e insesgadas, se deben verificar los supuestos estadísticos clásicos:

#### 1. Relación Lineal (*Linear Relationship*):
La relación entre las variables dependiente e independiente debe ser lineal. Se evalúa graficando los **residuos vs valores predichos**.

```python
# 1. Comprobación de Linealidad: Residuos vs Valores Predichos
residuals = y_test - y_pred_sk

plt.figure(figsize=(6, 5), dpi=100)
sns.scatterplot(x=y_pred_sk, y=residuals, color='red', alpha=0.8, s=50)
plt.axhline(0, color='black', linestyle='--', linewidth=1.2)
plt.title('Check for Linearity:\nResiduals vs Predicted values', fontweight='bold')
plt.xlabel('Predicted')
plt.ylabel('Residuals')
plt.tight_layout()
plt.show()

print("🔍 Se reconoce un patrón en forma de 'U' o 'V', lo que sugiere una relación no perfectamente lineal.")
```

#### 2. Normalidad de los Residuos (*Normality of the Error Terms*):
Los residuos deben distribuirse de manera aproximadamente normal con media igual o cercana a cero ($\mathbb{E}[\varepsilon] \approx 0$).

```python
# 2. Comprobación de Normalidad y Media de Residuos
sns.displot(data=residuals, kind='hist', kde=True, color='#1e3a8a', height=4, aspect=1.4)
plt.axvline(residuals.mean(), color='black', linestyle='--', linewidth=1.5, label=f'Media: {residuals.mean():.4f}')
plt.title('Check for residuals normality & mean:\n Distribution of residuals', fontweight='bold')
plt.xlabel('Residuals')
plt.legend()
plt.tight_layout()
plt.show()

print(f"Media de los residuos: {residuals.mean():.4f} (muy cercana a 0).")
```

#### 3. Independencia de las Observaciones (*No correlation of Error Terms*):
Los errores no deben estar autocorrelacionados ($\text{Cov}(\varepsilon_i, \varepsilon_j) = 0$). Se evalúa formalmente con el **Test de Durbin-Watson** ($d$):
* $d \approx 2$: Ausencia de autocorrelación.
* $1.5 < d < 2.5$: Rango aceptable de no autocorrelación.

```python
# 3. Test de Durbin-Watson para Autocorrelación
print('\nPerforming Durbin-Watson Test')
print('Values of 1.5 < d < 2.5 generally show that there is no autocorrelation in the data')
print('0 to 1.5 is positive autocorrelation')
print('2.5 to 4 is negative autocorrelation')
print('-------------------------------------')
durbinWatson = durbin_watson(residuals)
print('Durbin-Watson:', durbinWatson)

if durbinWatson < 1.5:
    print('Signs of positive autocorrelation\nAssumption not satisfied')
elif durbinWatson > 2.5:
    print('Signs of negative autocorrelation\nAssumption not satisfied')
else:
    print('Little to no autocorrelation\nAssumption satisfied')
```

#### 4. Homocedasticidad (*Homoscedasticity*):
La varianza de los residuos debe ser constante a lo largo de todo el rango de valores predichos ($\text{Var}(\varepsilon_i) = \sigma^2$).

```python
# 4. Comprobación de Homocedasticidad
plt.figure(figsize=(6, 5), dpi=100)
sns.scatterplot(x=y_pred_sk, y=residuals, color='red', alpha=0.8, s=50)
plt.axhline(0, color='black', linestyle='--', linewidth=1.2)
plt.title('Check for Homoscedasticity:\nResiduals Vs Predicted values', fontweight='bold')
plt.xlabel('Predicted')
plt.ylabel('Residuals')
plt.tight_layout()
plt.show()

print("🔍 Se observa cierta heterocedasticidad: la dispersión en el centro es mayor que en los extremos.")
```

---
##### 🛠️ Práctica 1: Solución a los Problemas del Modelo (Término de Interacción Radio × TV)

Al analizar los supuestos anteriores, observamos que el modelo presenta un patrón no lineal (forma de U) y heterocedasticidad. Además, la inversión en `Newspaper` tiene un coeficiente prácticamente nulo.

**¿Qué ocurre si eliminamos la variable `Newspaper` y agregamos un término de interacción sinérgico entre `Radio` y `TV` (`Radio * TV`)?**

**Instrucciones:**
1. Crea una copia de `adv_data` y genera la nueva columna: `df['Radio_TV'] = df['Radio'] * df['TV']`.
2. Define las variables predictoras: `X_inter = df[['TV', 'Radio', 'Radio_TV']].to_numpy()`.
3. Divide los datos en Train (70%) y Test (30%) con `random_state=23`.
4. Ajusta un nuevo modelo `LinearRegression()` y evalúa el nuevo $R^2$ y MSE en el conjunto de prueba.
5. Compara los resultados frente al modelo original.

```python
# =========================================================================
# TU SOLUCIÓN: Mejora del modelo con término de interacción
# =========================================================================

# 1. Crear copia y añadir interacción
# adv_inter = adv_data.copy()
# adv_inter['Radio_TV'] = ...

# 2. Definir X_inter e y_inter
# X_inter = ...
# y_inter = ...

# 3. Partición Train / Test
# X_tr, X_te, y_tr, y_te = ...

# 4. Ajuste del nuevo modelo
# modelo_inter = ...

# 5. Evaluación de R2 y MSE
# y_pred_inter = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# 1. Crear copia y añadir la interacción sinérgica
adv_inter = adv_data.copy()
adv_inter['Radio_TV'] = adv_inter['Radio'] * adv_inter['TV']

# 2. Definir matrices X e y (excluyendo Newspaper)
features = ['TV', 'Radio', 'Radio_TV']
X_inter = adv_inter[features].to_numpy()
y_inter = adv_inter['Sales'].to_numpy()

# 3. Partición idéntica Train (70%) / Test (30%)
X_tr, X_te, y_tr, y_te = train_test_split(X_inter, y_inter, test_size=0.3, random_state=23)

# 4. Ajuste del nuevo modelo
modelo_inter = LinearRegression(fit_intercept=True)
modelo_inter.fit(X_tr, y_tr)

# 5. Evaluación en el conjunto de prueba
y_pred_inter = modelo_inter.predict(X_te)
r2_inter = r2_score(y_te, y_pred_inter)
mse_inter = mean_squared_error(y_te, y_pred_inter)

print("=" * 55)
print("🚀 RESULTADOS DEL MODELO CON INTERACCIÓN (RADIO × TV):")
print("=" * 55)
print(f"• R² Original: 0.9267  ──►  R² Mejorado:  {r2_inter:.4f} (¡Sube al 98.7%!)")
print(f"• MSE Original: 2.5863 ──►  MSE Mejorado: {mse_inter:.4f} (¡Reducción masiva!)")
print("=" * 55)
print("Parámetros aprendidos:")
for col, coef in zip(features, modelo_inter.coef_):
    print(f" - {col:12s}: {coef:.6f}")
print(f" - Intercepto   : {modelo_inter.intercept_:.6f}")
```
</details>

---
### 11. Resumen y Conclusiones 📌

1. **Ecuación Normal de Mínimos Cuadrados:** Permite estimar analíticamente el vector de parámetros óptimo $\boldsymbol{\theta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$, coincidiendo con la implementación de Scikit-Learn.
2. **Evaluación Rigurosa:** Las métricas MSE y $R^2$ cuantifican la magnitud del error y la proporción de varianza explicada.
3. **Diagnóstico de Supuestos:** La inspección de residuos (Linealidad, Homocedasticidad, Normalidad e Independencia con Durbin-Watson) es indispensable antes de desplegar un modelo.
4. **Términos de Interacción:** La inclusión de relaciones cruzadas (como $\text{Radio} \times \text{TV}$) permite capturar efectos sinérgicos no lineales elevando el $R^2$ por encima del $98\%$.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
