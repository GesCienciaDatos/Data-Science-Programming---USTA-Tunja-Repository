# 06_Temas_Avanzados_Numpy

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Temas Avanzados: Aleatoriedad, Únicos y Expansión en NumPy 🚀
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
        Módulo 02
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/06_Temas_Avanzados_Numpy.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Temas Avanzados: Aleatoriedad Moderna, Frecuencias y Expansión Dimensional 🎲

En este cuaderno final abordaremos técnicas avanzadas esenciales para simulación estocástica, Machine Learning y Deep Learning:

1. **Generador Pseudo-aleatorio Moderno (`default_rng`):** El generador BitGenerator de NumPy basado en el algoritmo PCG-64 (más rápido y estadísticamente superior a `np.random.seed`).
2. **Distribuciones Estadísticas:** Muestreo de distribuciones Uniforme, Normal (Gaussiana) y Binomial.
3. **Análisis de Frecuencias y Unicidad con `np.unique`:** Inspección de categorías y conteo de ocurrencias.
4. **Manipulación Dimensional (`expand_dims` y `squeeze`):** Inserción y eliminación de dimensiones unitarias para compatibilidad con tensores de modelos neuronales.

---
### 1. Generación Pseudo-aleatoria Moderna con `default_rng` 🎲

En versiones modernas de NumPy (1.17+), la API recomendada es instanciar un generador mediante **`np.random.default_rng(seed)`**:

```python
rng = np.random.default_rng(seed=42)
```

#### Ventajas del nuevo generador:
* **Algoritmo PCG-64:** Mucho más rápido y con mejores propiedades estadísticas que el antiguo generador *Mersenne Twister*.
* **Instancias Independientes:** Permite tener múltiples generadores aislados con distintas semillas sin efectos secundarios globales.

| Distribución | Método | Parámetros Clave |
|---|---|---|
| **Enteros Uniformes** | `rng.integers(low, high, size)` | Intervalo discreto $[low, high)$ |
| **Flotantes Uniformes** | `rng.uniform(low, high, size)` | Intervalo continuo $[low, high)$ |
| **Normal / Gaussiana** | `rng.normal(loc, scale, size)` | Media $\mu = loc$, Desviación $\sigma = scale$ |
| **Binomial** | `rng.binomial(n, p, size)` | Número de ensayos $n$, probabilidad de éxito $p$ |

```python
# Configuración interactiva segura
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"
except ImportError:
    pass
import numpy as np
```

---
#### 🛠️ Práctica 1: Aleatoriedad

Crea un generador aleatorio utilizando la semilla `42` (la más famosa en programación). 
1. Genera un vector de 5 números enteros aleatorios entre el `10` y el `20` (inclusivos).
2. Ejecuta la celda varias veces. ¿Cambian los números? ¿Por qué?

```python
# Escribe tu código aquí

# rng_practica = ...
# vector_aleatorio = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
rng_practica = np.random.default_rng(seed=42)
# Para que el 20 sea inclusivo, el 'high' debe ser 21. Opcionalmente puedes usar endpoint=True
vector_aleatorio = rng_practica.integers(low=10, high=21, size=5)
print(vector_aleatorio)
# Respuesta a la pregunta: Los números NO cambian al re-ejecutar porque la "semilla" 
# (42) ancla el algoritmo a una secuencia fija. Si cambias el 42 por 43, la secuencia será otra.
```
</details>

---
### 2. Elementos Únicos y Frecuencias (`np.unique`) 🔍

La función `np.unique()` identifica los valores distintos presentes en un array y permite calcular su frecuencia de aparición:

* `return_counts=True`: Retorna un array con el número de repeticiones de cada valor.
* `return_index=True`: Retorna los primeros índices donde aparece cada elemento único.
* `return_inverse=True`: Retorna los índices para reconstruir el array original (codificación entera/ordinal).

```python
# Imaginemos que este array representa las edades de un grupo de personas
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])

# Obtener solo los valores únicos
valores_unicos = np.unique(a)
print("Valores únicos ordenados:", valores_unicos)

# Obtener los únicos y sus índices en el array original (la primera vez que aparece cada número)
unicos, indices = np.unique(a, return_index=True)
print("\nÍndice donde aparece el número '12' por primera vez:", indices[1]) # '12' es el segundo valor único

# Obtener la FRECUENCIA (conteos) de cada elemento
unicos, conteos = np.unique(a, return_counts=True)
print("\nFrecuencia (veces que aparece cada edad):")
for u, c in zip(unicos, conteos):
    print(f"La edad {u} aparece {c} veces.")
```

---
#### 🛠️ Práctica 2: Frecuencias

Tienes un vector que representa el resultado de tirar un dado de 6 caras, 20 veces.
Usando `np.unique()`, descubre **cuántas veces cayó el número 6**.

```python
# Lanzamiento de dados (Semilla fijada para reproducibilidad)
dados = np.random.default_rng(seed=777).integers(1, 7, size=20)
print("Lanzamientos:", dados)

# Escribe tu código aquí

# ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
caras_unicas, frecuencias = np.unique(dados, return_counts=True)
print("Caras resultantes:", caras_unicas)
print("Frecuencia de caras:", frecuencias)

# Opcional (Programático):
# Buscamos en qué posición está el 6 en 'caras_unicas'
indice_seis = np.where(caras_unicas == 6)[0][0]
print(f"El número 6 cayó {frecuencias[indice_seis]} veces.")
```
</details>

---
### 3. Expandiendo y Comprimiendo Dimensiones (`expand_dims` y `squeeze`) 🗜️

En arquitecturas de Deep Learning (como CNNs o Transformers), los datos deben tener dimensiones específicas que representen el **tamaño de lote (*batch size*)** o los **canales (*channels*)**:

* **`np.expand_dims(arr, axis=...)`:** Inserta un nuevo eje de tamaño 1 en la posición indicada.
  * Ejemplo: `(128, 128)` $\xrightarrow{\text{axis=0}}$ `(1, 128, 128)` (añade dimensión de lote).
* **`np.squeeze(arr)`:** Elimina todos los ejes unidimensionales de tamaño 1 innecesarios.
  * Ejemplo: `(1, 128, 128, 1)` $\xrightarrow{\text{squeeze}}$ `(128, 128)`.

<div align="center">
  <img src="images/expand_squeeze.png" alt="Expand Dims y Squeeze en Tensores" width="700" style="border-radius: 6px; margin: 15px 0;"/>
</div>

```python
# Recordatorio: Un vector 1D no es ni "fila" ni "columna" matemáticamente. Es solo un vector.
arr = np.arange(5)
print("Forma original:", arr.shape)

# Podemos convertirlo artificialmente en un "Vector Fila" (1x5) o "Vector Columna" (5x1) usando reshape
print("Vector Fila:", arr.reshape(1, -1).shape)
print("Vector Columna:", arr.reshape(-1, 1).shape)
```

```python
# --- EXPANDIENDO (Añadiendo Dimensiones Falsas) ---
matriz_2d = np.arange(9).reshape(3, 3)
print("\nMatriz original:\n", matriz_2d)
print("Forma 2D:", matriz_2d.shape)

# Método 1: Usando reshape y agregando un '1'
expandida_res = np.reshape(matriz_2d, [3, 3, 1])
print("Expandida con reshape:", expandida_res.shape)

# Método 2: Usando np.expand_dims (El método explícito preferido)
# axis=-1 significa "agrega la dimensión vacía al final"
expandida = np.expand_dims(matriz_2d, axis=-1)
print("Expandida con expand_dims:", expandida.shape)


# --- COMPRIMIENDO (Eliminando Dimensiones Falsas) ---
# La función np.squeeze() destruye todas las dimensiones cuyo tamaño sea exactamente '1'
comprimida = np.squeeze(expandida, axis=-1)
print("\nComprimida con squeeze (Volvió a la normalidad):", comprimida.shape)
```

---
#### 🛠️ Práctica 3: Expand y Squeeze

Tienes un tensor 4D que representa un lote de procesamiento de una red neuronal: `[Tamaño_Lote, Alto, Ancho, Canales]`. 
Actualmente su forma es `(1, 128, 128, 1)` (Una sola imagen, 128x128, en blanco y negro).
Usa `np.squeeze()` sin especificar el `axis` para ver qué sucede cuando omites el eje explícito.

```python
tensor_red = np.zeros((1, 128, 128, 1))

# Escribe tu código aquí

# tensor_aplastado = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Si no especificamos el 'axis', np.squeeze destruirá TODOS los ejes que midan 1.
# Por lo tanto, destruirá el eje 0 (Tamaño de lote) y el eje 3 (Canales).
tensor_aplastado = np.squeeze(tensor_red)

print("Forma final:", tensor_aplastado.shape) # Debería ser simplemente (128, 128)
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
