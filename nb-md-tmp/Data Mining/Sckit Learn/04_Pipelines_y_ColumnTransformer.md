# 04_Pipelines_y_ColumnTransformer

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Pipelines y ColumnTransformer en Scikit-Learn ⛓️
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
        Módulo 04
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Mining/Sckit%20Learn/04_Pipelines_y_ColumnTransformer.ipynb" target="_parent">
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

En este cuaderno aprenderás a construir flujos de minería de datos profesionales, reproducibles y blindados contra fugas de información:

* **1. Prevención de Data Leakage:** Encapsulamiento de transformaciones con `Pipeline`.
* **2. Procesamiento Heterogéneo:** Ensamblado de columnas numéricas y categóricas con `ColumnTransformer`.
* **3. Inspección Interna:** Acceso a etapas intermedias mediante `.named_steps` y extracción de nombres con `get_feature_names_out()`.
* **4. Persistencia en Producción:** Serialización y carga de pipelines en disco con `joblib`.

---
### 1. Ensamblaje Heterogéneo con `ColumnTransformer` ⚙️

Permite aplicar sub-pipelines específicos a subconjuntos de columnas en paralelo:

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

df_clientes = pd.DataFrame({
    'Edad': [25.0, np.nan, 45.0, 35.0, 52.0],
    'Salario': [3200.0, 4800.0, np.nan, 5100.0, 8900.0],
    'Ciudad': ['Tunja', 'Bogotá', 'Tunja', 'Duitama', 'Bogotá']
})

pipe_num = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

pipe_cat = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocesador = ColumnTransformer(transformers=[
    ('num', pipe_num, ['Edad', 'Salario']),
    ('cat', pipe_cat, ['Ciudad'])
])

X_proc = preprocesador.fit_transform(df_clientes)
cols_out = preprocesador.get_feature_names_out()

df_proc = pd.DataFrame(X_proc, columns=cols_out)
print("Matriz procesada final:")
display(df_proc.round(2))
```

---
#### 🛠️ Práctica: Pipelines y Persistencia

**Ejercicio 1:**
Construye un pipeline rápido utilizando `make_pipeline` y `make_column_transformer` que aplique `MinMaxScaler` a variables numéricas y `OneHotEncoder` a categóricas.

```python
# Ejercicio 1
# Escribe tu código aquí
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler

# pipe_rapido = make_column_transformer(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Solución Ejercicio 1
pipe_rapido = make_column_transformer(
    (make_pipeline(SimpleImputer(strategy='mean'), MinMaxScaler()), ['Edad', 'Salario']),
    (OneHotEncoder(sparse_output=False), ['Ciudad'])
)

X_rapido = pipe_rapido.fit_transform(df_clientes)
print("Resultado con make_column_transformer:\n", X_rapido.round(2))
```
</details>

**Ejercicio 2:**
Serializa el objeto `preprocesador` en un archivo binario `pipeline_clientes.joblib` usando `joblib.dump` y recárgalo con `joblib.load` para transformar un cliente nuevo `{'Edad': [30.0], 'Salario': [4000.0], 'Ciudad': ['Tunja']}`.

```python
# Ejercicio 2
# Escribe tu código aquí
import joblib

# joblib.dump(...)
# loaded_pipe = joblib.load(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Solución Ejercicio 2
import tempfile

ruta_tmp = os.path.join(tempfile.gettempdir(), "pipeline_clientes.joblib")
joblib.dump(preprocesador, ruta_tmp)

pipe_cargado = joblib.load(ruta_tmp)
nuevo_cliente = pd.DataFrame({'Edad': [30.0], 'Salario': [4000.0], 'Ciudad': ['Tunja']})
cliente_transformado = pipe_cargado.transform(nuevo_cliente)

print("Inferencia sobre nuevo cliente en producción:\n", cliente_transformado.round(2))
```
</details>

---
### Resumen y Preguntas de Autoevaluación 🧠

1. **¿Cómo previene `Pipeline` el Data Leakage en validación cruzada?**  
   *Respuesta:* Re-ejecuta `fit()` en cada fold exclusivamente con el subconjunto de entrenamiento correspondiente.
2. **¿Cómo se extrae un paso intermedio de un pipeline?**  
   *Respuesta:* Mediante el atributo `pipeline.named_steps['nombre_paso']`.
3. **¿Por qué `joblib` es preferido sobre `pickle` en Scikit-Learn?**  
   *Respuesta:* Porque optimiza la compresión y serialización rápida de grandes arrays de NumPy en memoria compartida.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Minería de Datos (Data Mining)</i>
  </p>
</div>
