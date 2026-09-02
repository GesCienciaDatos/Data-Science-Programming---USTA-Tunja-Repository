# 02_Pipelines_y_Validacion_Para_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Pipelines y Validación Para Dummies: La Banda Transportadora 💡
      </h1>
      <p style="margin: 6px 0 0 0; color: #f59e0b; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Minería de Datos (Data Mining) — Edición Para Dummies 💡
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #f59e0b; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Módulo: Scikit-Learn #02
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #d97706; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Mining/Sckit%20Learn/Para%20Dummies/02_Pipelines_y_Validacion_Para_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## La Fábrica Automática: ¿Qué es un Pipeline? 🏭

Imagina una fábrica embotelladora de gaseosas:
1. Llega la botella vacía.
2. La **Estación 1** lava la botella (`SimpleImputer`).
3. La **Estación 2** le pega la etiqueta de marca (`StandardScaler`).
4. La **Estación 3** la llena con la bebida y la sella.

Hacer todo esto a mano con baldes y tijeras para cada botella sería una locura, tomaría horas y cometerías errores todo el tiempo.

Un **`Pipeline` (Tubería o Banda Transportadora)** en Scikit-Learn conecta todas las estaciones en una sola línea de producción automática. Solo presionas un botón y procesa millones de datos en segundos.

```
  [ Datos Crudos ] ───> [ Estación 1: Imputar ] ───> [ Estación 2: Escalar ] ───> [ Producto Final ]
```

```python
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Creamos nuestra primera banda transportadora de 2 estaciones
fabrica = Pipeline([
    ('lavar_huecos', SimpleImputer(strategy='median')),
    ('estandarizar', StandardScaler())
])

# Datos con huecos vacíos
botellas = np.array([
    [10.0],
    [np.nan],
    [30.0],
    [40.0],
    [50.0]
])

# ¡Encendemos la fábrica con fit_transform!
botellas_listas = fabrica.fit_transform(botellas)

print("Botellas Crudas:\n", botellas.ravel())
print("\n✨ Botellas procesadas automáticamente por la banda:\n", botellas_listas.ravel().round(2))
```

---
## La Regla Sagrada: Cómo NO Hacer Trampa en los Exámenes (*Data Leakage*) 🚫

Imagina que un profesor te entrega el examen final con todas las respuestas marcadas **un día antes del examen**.

Obviamente sacarás un `10/10` en el examen de prueba, pero cuando vayas a la vida real no sabrás nada de verdad.

En Ciencia de Datos, esto se llama **Fuga de Información (*Data Leakage*)**:
* Ocurre cuando calculas el promedio o la escala usando **todos los datos juntos** antes de separar los datos de entrenamiento y de prueba.
* El `Pipeline` te protege al 100% contra esto porque se asegura de que la fábrica solo aprenda (`fit`) con los datos de entrenamiento y nunca haga trampa con los datos de prueba.

---
## El Banco con Dos Ventanillas: `ColumnTransformer` 🏦

¿Qué pasa si en tu base de datos tienes columnas de **números** (Edad, Salario) y columnas de **texto** (Ciudad, Género) mezcladas?

No puedes pasar el texto por `StandardScaler` (¡porque las palabras no tienen promedio matemático!).

La solución es **`ColumnTransformer`**:
Funciona como la entrada de un banco con dos filas:
* Los clientes con números van a la **Ventanilla 1** (Imputación + Escalamiento).
* Los clientes con texto van a la **Ventanilla 2** (Imputación + One-Hot Encoding).
* Al salir, se juntan ordenadamente en una sola tabla limpia.

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Dataset mixto realista
df_clientes = pd.DataFrame({
    'Edad': [25.0, np.nan, 45.0, 32.0],
    'Salario': [3000.0, 4500.0, 6000.0, np.nan],
    'Ciudad': ['Tunja', 'Bogotá', 'Tunja', 'Duitama']
})

# 1. Banda para los números
banda_numerica = Pipeline([
    ('imputar_mediana', SimpleImputer(strategy='median')),
    ('escalar', StandardScaler())
])

# 2. Banda para el texto
banda_texto = Pipeline([
    ('imputar_moda', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(sparse_output=False))
])

# 3. Ensamblador con dos ventanillas
banco_central = ColumnTransformer(transformers=[
    ('num', banda_numerica, ['Edad', 'Salario']),
    ('cat', banda_texto, ['Ciudad'])
])

# ¡Procesamos todo el dataset en una sola pasada!
datos_procesados = banco_central.fit_transform(df_clientes)
nombres_finales = banco_central.get_feature_names_out()

df_resultado = pd.DataFrame(datos_procesados, columns=nombres_finales)
print("Tabla Final Procesada y Ensamblada:")
display(df_resultado.round(2))
```

---
## Validación Cruzada: Los 5 Exámenes Sorpresa 📝

¿Cómo sabemos si nuestro modelo de verdad aprendió o solo tuvo suerte?

En lugar de hacer una sola prueba, usamos **Validación Cruzada ($K$-Fold con $K=5$)**:
1. Dividimos los datos en 5 pedazos iguales.
2. Hacemos 5 rondas: en cada ronda usamos 4 pedazos para estudiar y 1 pedazo para hacer el examen.
3. El promedio de las 5 notas es la verdadera calificación de calidad de nuestro trabajo.

```python
from sklearn.model_selection import KFold

datos_ejemplo = np.arange(10, 20) # 10 números del 10 al 19
kf = KFold(n_splits=5, shuffle=True, random_state=42)

print("Demostración de los 5 Folds de Validación Cruzada:")
for i, (train_index, test_index) in enumerate(kf.split(datos_ejemplo)):
    print(f"  Ronda {i+1}: Estudia con índices {train_index} -> Se examina con índices {test_index}")
```

---
## 4. Actividades y Desafíos Prácticos Guiados 🧪

### 🛠️ Práctica 3.1: Construir un Pipeline Completo
Crea un `Pipeline` que tenga los siguientes dos pasos sobre una matriz de 4 números con un valor faltante:
1. `SimpleImputer(strategy='mean')`
2. `MinMaxScaler(feature_range=(0, 100))` (escala de 0 a 100 puntos)

```python
# Escribe tu solución aquí
from sklearn.preprocessing import MinMaxScaler

datos_notas = np.array([[60.0], [np.nan], [80.0], [100.0]])

# mi_pipeline = Pipeline([...])
# notas_transformadas = mi_pipeline.fit_transform(datos_notas)
# print(notas_transformadas)
```

---
### 🛠️ Práctica 3.2: Guardar y Cargar la Fábrica en Disco con `joblib`
Utiliza `joblib.dump(fabrica, 'mi_fabrica.joblib')` para guardar tu pipeline en disco y luego recárgalo con `joblib.load()` para procesar una nueva botella con valor `[25.0]`.

```python
# Escribe tu solución aquí
import joblib

# joblib.dump(fabrica, 'mi_fabrica.joblib')
# fabrica_recargada = joblib.load('mi_fabrica.joblib')
# print(fabrica_recargada.transform([[25.0]]))
```

---
## 5. Preguntas de Autoevaluación 🧠

1. **¿Cuál es la principal ventaja de usar un `Pipeline` en lugar de aplicar las funciones una por una?**  
   *Respuesta:* Automatiza todo el flujo en un solo comando, evita errores humanos y previene por completo la fuga de datos (*Data Leakage*).
2. **¿Para qué sirve `ColumnTransformer`?**  
   *Respuesta:* Para aplicar transformaciones diferentes a columnas diferentes (por ejemplo, escalar números y hacer One-Hot al texto) al mismo tiempo.
3. **¿Por qué la Validación Cruzada es más confiable que una sola partición Train/Test?**  
   *Respuesta:* Porque evalúa el rendimiento del modelo en múltiples combinaciones de datos, asegurando que los resultados no fueron fruto de la casualidad.

---
## 📌 Los 5 Mandamientos de Scikit-Learn Para Dummies

1. **No harás transformaciones manuales:** Usa siempre un `Pipeline`.
2. **No mezclarás números y texto:** Usa `ColumnTransformer` para separarlos.
3. **No harás trampa en los exámenes:** Nunca apliques `.fit()` sobre los datos de prueba.
4. **No evaluarás con un solo intento:** Usa siempre Validación Cruzada ($K$-Fold).
5. **Guardarás tu fábrica al terminar:** Usa `joblib` para llevar tu modelo a producción.
