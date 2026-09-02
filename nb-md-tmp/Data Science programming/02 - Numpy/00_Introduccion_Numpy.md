# 00_Introduccion_Numpy

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Introducción a NumPy y Computación Científica 🔢
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/02%20-%20Numpy/00_Introduccion_Numpy.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Objetivos de Aprendizaje 🔎

En este segundo módulo nos adentraremos en **NumPy (*Numerical Python*)**, el paquete medular sobre el cual se construye casi la totalidad del ecosistema científico y de Machine Learning en Python. El material está organizado progresivamente en los siguientes cuadernos interactivos:

1. **[Introducción a NumPy](00_Introduccion_Numpy.ipynb)** *(Este cuaderno)*: ¿Qué es NumPy, cómo funciona su memoria contigua y por qué es órdenes de magnitud más rápido que las listas estándar?
2. **[Creación de Arrays en NumPy](01_Creacion_de_Arrays_Numpy.ipynb)**: Funciones de inicialización (`zeros`, `ones`, `arange`, `linspace`), tipos de datos numéricos (`dtype`) y atributos estructurales (`ndim`, `shape`, `size`).
3. **[Operaciones con Arrays](02_Operaciones_con_Arrays_Numpy.ipynb)**: Vectorización elemento a elemento, funciones universales (`ufuncs`), reglas de difusión (*Broadcasting*) y álgebra lineal.
4. **[Indexación y Slicing](03_Indexacion_y_Slicing_Numpy.ipynb)**: Rebanado multidimensional (*slicing*), vistas vs copias, máscaras booleanas e indexación elegante (*Fancy Indexing*).
5. **[Remodelación de Arrays (Reshaping)](04_Reshaping_Numpy.ipynb)**: Modificación de dimensiones en memoria (`reshape`), aplanado (`ravel` vs `flatten`) y comodines dimensionales (`-1`).
6. **[Concatenación y Apilamiento](05_Concatenacion_Numpy.ipynb)**: Fusión y apilamiento a lo largo de ejes existentes o nuevos (`concatenate`, `vstack`, `hstack`, `stack`).
7. **[Temas Avanzados: Aleatorios, Únicos y Dimensiones](06_Temas_Avanzados_Numpy.ipynb)** 🧗: Generación pseudo-aleatoria moderna con `Generator`, conteo de frecuencias con `np.unique` y manipulación de dimensiones (`expand_dims` / `squeeze`).

> 🧗 **Nota:** Los temas con mayor nivel de abstracción y complejidad están identificados con el ícono de escalador.

---
## Recursos Recomendados 📚

### 📖 Libros de Referencia:
- [Python Data Science Handbook: Essential Tools for Working with Data](https://jakevdp.github.io/PythonDataScienceHandbook/) — *Jake VanderPlas*
- [Guide to NumPy (2nd Edition)](https://web.mit.edu/dvp/Public/numpybook.pdf) — *Travis E. Oliphant (creador de NumPy)*
- [NumPy Illustrated: The Visual Guide to NumPy](https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d) — *Lev Maximov*

### 🌐 Enlaces y Documentación Oficial:
- [Guía de Usuario Oficial de NumPy](https://numpy.org/doc/stable/user/index.html)
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [Broadcasting en NumPy: Guía Visual y Conceptual](https://numpy.org/doc/stable/user/basics.broadcasting.html)

---
## 1. ¿Qué es NumPy y por qué es la Base de la Ciencia de Datos? 🔢

**NumPy (*Numerical Python*)** es la biblioteca fundamental para la computación científica y matricial en Python. Proporciona una estructura de datos de alto rendimiento llamada **`ndarray`** (*N-dimensional array*) junto con una vasta colección de rutinas matemáticas para operar sobre estas estructuras a velocidades cercanas a C/Fortran.

### ¿Por qué no usar listas nativas de Python para cálculo numérico?

1. **Memoria Contigua vs Punteros Dispersos:**  
   * Las **listas de Python** almacenan punteros a objetos genéricos dispersos por la memoria RAM (*overhead* de empaquetado/boxeo de tipos).
   * Los **`ndarray` de NumPy** almacenan datos homogéneos en un **bloque contiguo de memoria**, lo que maximiza el aprovechamiento de la memoria caché del procesador (*CPU Cache Locality*).
2. **Vectorización y Computación SIMD:**  
   * NumPy reemplaza los bucles explícitos de Python por operaciones vectorizadas compiladas en C que aprovechan instrucciones vectoriales modernas del hardware (**SIMD**: *Single Instruction, Multiple Data*).

> 📌 **Concepto Clave:** En Ciencia de Datos y Machine Learning, prácticamente todas las librerías líderes (`Pandas`, `Scikit-Learn`, `SciPy`, `TensorFlow`, `PyTorch`) utilizan arrays de NumPy por debajo como su formato de intercambio numérico estándar.

---
## ¿Por qué NumPy es tan rápido comparado con las listas nativas? ⚡

Las listas estándar de Python son colecciones dinámicas y heterogéneas. Cada elemento de una lista es en realidad un **puntero** a un objeto independiente en memoria, lo que genera:
- **Fragmentación de memoria**: Los elementos están dispersos en distintas direcciones de RAM.
- **Sobrecarga de tipo (*Type Overhead*)**: Python debe verificar el tipo de dato de cada elemento en cada ciclo del bucle.
- **Pérdida de Caché de CPU**: El procesador no puede precargar bloques contiguos eficientemente.

En contraste, un `ndarray` de NumPy almacena sus elementos en un **bloque contiguo de memoria continua de tamaño fijo en C**:
- **Homogeneidad**: Todos los elementos comparten exactamente el mismo tipo de dato (ej. `float64`, `int32`).
- **Vectorización**: Las operaciones se delegan a rutinas compiladas en C/Fortran y aprovechan instrucciones SIMD (*Single Instruction, Multiple Data*) a nivel de CPU, eliminando los lentos bucles `for` de Python.

---
## 2. Comparación de Rendimiento: Listas vs NumPy ⚡

Para dimensionar la diferencia computacional, midamos el tiempo que toma sumar dos vectores de 1,000,000 de elementos utilizando bucles de Python vs la vectorización de NumPy:

```
  ┌────────────────────────────────────────────────────────┐
  │  Bucle Python: O(n) llamadas al intérprete en CPython │ ──► ~100 ms
  └────────────────────────────────────────────────────────┘
                             vs
  ┌────────────────────────────────────────────────────────┐
  │  NumPy Vectorizado: 1 llamada a kernel C contiguo      │ ──► ~1 ms (100x más rápido)
  └────────────────────────────────────────────────────────┘
```

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
### Demostración Rápida de Vectorización

Creemos un array unidimensional y apliquemos una operación matemática directamente sin necesidad de iterar:

```python
# Creación de un array simple
arr = np.array([10, 20, 30, 40, 50])
print("Array original:", arr)

# Operación vectorizada (multiplicación por escalar y suma)
resultado = arr * 2 + 5
print("Array transformado:", resultado)
print(f"Dimensiones: {arr.ndim}D | Forma: {arr.shape} | Tipo: {arr.dtype}")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
