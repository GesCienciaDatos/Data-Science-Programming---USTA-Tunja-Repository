# 00_Scikit_Learn_Para_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Scikit-Learn Para Dummies: La Fábrica de LEGO 💡
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
        Módulo: Scikit-Learn #00
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #d97706; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Mining/Sckit%20Learn/Para%20Dummies/00_Scikit_Learn_Para_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué es Scikit-Learn y por qué todos los Científicos de Datos lo aman? 💖

Imagina que eres un arquitecto y quieres construir una casa moderna. Tienes dos opciones:
1. **La opción difícil y dolorosa:** Fabricar tus propios ladrillos con arcilla, fundir tu propio acero y cortar cada árbol a mano. (Esto sería programar todas las fórmulas matemáticas y algoritmos desde cero en Python puro).
2. **La opción profesional e inteligente:** Ir a una tienda donde todos los bloques de construcción ya vienen perfectamente fabricados, certificados, probados y con medidas universales que encajan a la perfección.

**Scikit-Learn (`sklearn`)** es esa tienda de bloques universales para Inteligencia Artificial y Minería de Datos. Es la librería más utilizada del planeta porque permite hacer magia con datos utilizando solo unas pocas líneas de código limpio y ordenado.

---
## La Gran Analogía: Los 3 Tipos de Bloques LEGO 🧱

En Scikit-Learn existen miles de herramientas, pero **todas** pertenecen a una de estas tres familias de bloques:

```
  ┌─────────────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
  │     1. EL ESCÁNER       │      │     2. EL MOLDE         │      │     3. EL ORÁCULO       │
  │      (Estimador)        │      │    (Transformador)      │      │      (Predictor)        │
  │                         │      │                         │      │                         │
  │ Mide los datos y        │      │ Usa las medidas para    │      │ Aprende el pasado y     │
  │ aprende sus medidas     │      │ transformar los datos   │      │ adivina el futuro       │
  │                         │      │                         │      │                         │
  │ Verbo: .fit()           │      │ Verbo: .transform()     │      │ Verbo: .predict()       │
  └─────────────────────────┘      └─────────────────────────┘      └─────────────────────────┘
```

Vamos a ver cómo funciona cada uno con ejemplos de la vida real.

```python
# Configuración inicial y verificación de herramientas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

print("🎉 ¡Entorno listo! Tienes instalado Scikit-Learn versión:", sklearn.__version__)
```

---
## 1. El Bloque 1: El Escáner (`Estimator`) y el Verbo `.fit()` 📏

Imagina que compras un escáner láser. Para que el escáner sepa cuánto mide una habitación, primero tienes que dejarlo quieto midiendo las paredes.

En Scikit-Learn, el verbo **`.fit(datos)`** significa exactamente eso: **\"Estudia estos datos y memoriza sus medidas\"**.

* Si es un escalador de números, `.fit()` calcula el número más pequeño y el más grande.
* Si es un limpiador de huecos vacíos, `.fit()` calcula el promedio.
* Si es un modelo predictivo, `.fit()` aprende los patrones matemáticos.

> 🔑 **Regla de Oro:** `.fit()` **SOLO APRENDE**, no modifica tus datos originales.

---
## 2. El Bloque 2: El Molde (`Transformer`) y el Verbo `.transform()` 🔄

Una vez que el escáner aprendió las medidas con `.fit()`, entra en acción el **Molde (`Transformer`)**.

El verbo **`.transform(datos)`** toma los datos y los pasa por el molde para convertirlos al nuevo formato deseado.

* **Ejemplo de la vida real:** Si tienes las estaturas de un equipo de baloncesto en centímetros `[160, 180, 200]`, puedes pasarlas por un molde llamado `MinMaxScaler` para que las convierta a una escala sencilla del `0.0` al `1.0`.

¡Veámoslo en código real!

```python
from sklearn.preprocessing import MinMaxScaler

# Estaturas de 4 personas en centímetros
estaturas_cm = np.array([
    [150.0],  # La persona más bajita
    [170.0],
    [180.0],
    [200.0]   # La persona más alta
])

# 1. Traemos nuestro molde de la caja de LEGO
molde_escala = MinMaxScaler()

# 2. PASO 1: El escáner mide el mínimo (150) y el máximo (200)
molde_escala.fit(estaturas_cm)

# 3. PASO 2: El molde transforma las estaturas al rango de 0 a 1
estaturas_0_a_1 = molde_escala.transform(estaturas_cm)

print("📏 Estaturas Originales (cm):\n", estaturas_cm.ravel())
print("\n✨ Estaturas Transformadas (de 0.0 a 1.0):\n", estaturas_0_a_1.ravel())
```

---
## 3. El Atajo Mágico: `fit_transform()` ⚡

¿Por qué hacer dos pasos (`.fit()` y luego `.transform()`) si casi siempre queremos hacer las dos cosas seguidas?

Scikit-Learn inventó el verbo combinado: **`.fit_transform(datos)`**.

Hace exactamente lo mismo: escanea los datos en milisegundos y los transforma de inmediato en una sola instrucción elegante.

```python
# Haciendo lo mismo pero en una sola línea ultra rápida:
estaturas_rapidas = MinMaxScaler().fit_transform(estaturas_cm)
print("Resultado con fit_transform():", estaturas_rapidas.ravel())
```

---
## 4. El Secreto del Guion Bajo (`_`): ¿Qué aprendió el modelo? 🕵️

Cuando un niño aprende a montar en bicicleta, ese conocimiento se queda guardado en su cerebro.

En Scikit-Learn, cada vez que ejecutas `.fit()`, el objeto guarda todo lo que aprendió en atributos especiales que **SIEMPRE terminan con un guion bajo (`_`)**.

* `data_min_`: El número más pequeño que encontró.
* `data_max_`: El número más grande que encontró.
* `mean_`: El promedio que calculó.
* `scale_`: La desviación estándar que midió.

Si intentas ver estos atributos **antes** de llamar a `.fit()`, Python te dará un error porque el objeto todavía no ha visto ningún dato.

```python
# Inspeccionemos el cerebro de nuestro molde_escala
print("🧠 ¿Cuál fue la estatura mínima que aprendió?:", molde_escala.data_min_[0], "cm")
print("🧠 ¿Cuál fue la estatura máxima que aprendió?:", molde_escala.data_max_[0], "cm")
print("🧠 ¿Cuál fue el rango total (máximo - mínimo)? :", molde_escala.data_range_[0], "cm")
```

---
## 5. El Secreto de las Dimensiones: ¿Por qué la Matriz $X$ es una Tabla 2D? 📊

Scikit-Learn es muy estricto con una sola regla de oro:
1. **La Matriz de Características ($X$):** **SIEMPRE debe ser una tabla 2D** (Filas = Personas/Observaciones, Columnas = Atributos como Edad, Salario, Altura).
2. **El Vector Objetivo ($y$):** Es una sola lista 1D (lo que queremos adivinar, como el Precio o si Tiene Diabetes).

Si le pasas a Scikit-Learn una lista plana `[150, 170, 180]` para $X$, se quejará con un error diciendo que esperaba una tabla 2D `(n_muestras, n_columnas)`.

```python
# Demostración visual de dimensiones
X_tabla = np.array([
    [25, 3500], # Fila 1: Persona de 25 años, gana 3500 USD
    [40, 5200], # Fila 2: Persona de 40 años, gana 5200 USD
    [18, 1200]  # Fila 3: Persona de 18 años, gana 1200 USD
])

print("Forma de la matriz X:", X_tabla.shape, "-> (3 filas, 2 columnas)")
print("Número de dimensiones de X:", X_tabla.ndim, "D")
```

---
## 6. Actividades y Desafíos Prácticos Guiados 🧪

### 🛠️ Práctica 1.1: Escalar Precios de Teléfonos Celulares
Tienes los precios en dólares de 5 teléfonos móviles: `$150`, `$300`, `$600`, `$900`, `$1200`.
Usa `MinMaxScaler(feature_range=(-1, 1))` para escalar los precios para que el teléfono más barato valga `-1.0` y el más caro valga `1.0`.

> 💡 **Pista:** Recuerda que los datos deben tener forma de columna 2D usando `.reshape(-1, 1)` o corchetes dobles `[[150], [300], ...]`.

```python
# Escribe tu solución aquí
from sklearn.preprocessing import MinMaxScaler

precios_telefonos = np.array([[150.0], [300.0], [600.0], [900.0], [1200.0]])

# 1. Instanciar el escalador con feature_range=(-1, 1)
# 2. Ajustar y transformar con fit_transform()
# 3. Imprimir el resultado transformado
```

---
### 🛠️ Práctica 1.2: Inspeccionar las Medias con `StandardScaler`
Usa `StandardScaler` sobre la siguiente matriz de dos columnas (Edad y Salario). Imprime los promedios aprendidos (`mean_`) y la desviación estándar (`scale_`):

```python
from sklearn.preprocessing import StandardScaler

datos_empleados = np.array([
    [20.0, 1000.0],
    [30.0, 2000.0],
    [40.0, 3000.0],
    [50.0, 4000.0]
])

# 1. Instanciar StandardScaler
# 2. Ejecutar fit()
# 3. Imprimir scaler.mean_ y scaler.scale_
```

---
## 7. Preguntas de Autoevaluación 🧠

1. **¿Qué diferencia hay entre `.fit()` y `.transform()`?**  
   *Respuesta:* `.fit()` es el escáner (aprende las estadísticas como la media y el máximo pero no cambia los datos). `.transform()` es el molde (aplica el cambio a los datos usando lo aprendido).
2. **¿Por qué los atributos aprendidos llevan un guion bajo al final como `mean_` o `scale_`?**  
   *Respuesta:* Para que tú como programador sepas de un vistazo que ese valor fue calculado por el algoritmo con los datos, y no fue un parámetro que tú escribiste a mano.
3. **Si intento hacer `scaler.transform(X)` sin haber hecho `scaler.fit(X)` antes, ¿qué pasará?**  
   *Respuesta:* Python lanzará un error (`NotFittedError`) porque el molde no tiene las medidas necesarias para transformar nada.

---
## 📌 La Chuleta de Oro de Scikit-Learn

| Verbo | ¿Qué hace? | Analogía Sencilla |
|---|---|---|
| **`.fit(X)`** | Aprende los patrones o estadísticas de los datos. | El sastre toma tus medidas con la cinta métrica. |
| **`.transform(X)`** | Modifica los datos usando lo que aprendió. | El sastre corta la tela a tu medida exacta. |
| **`.fit_transform(X)`** | Mide y corta la tela al mismo tiempo. | Servicio exprés de sastrería en un solo paso. |
| **`.predict(X)`** | Genera una predicción sobre datos nuevos. | El médico te da un diagnóstico tras ver tus exámenes. |
| **`atributo_`** | Guarda lo que el modelo aprendió tras `.fit()`. | Las notas escritas en el cuaderno del sastre. |
