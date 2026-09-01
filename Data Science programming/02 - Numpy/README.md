# Módulo 02: Computación Científica con NumPy 🔢

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción General

**NumPy (*Numerical Python*)** es la biblioteca fundamental sobre la que se construye todo el ecosistema de computación científica, análisis de datos y Machine Learning en Python (incluyendo Pandas, Scipy, Scikit-Learn y TensorFlow/PyTorch).

En este módulo aprenderás a dominar la estructura de datos `ndarray` (arreglos $N$-dimensionales homogéneos almacenados en bloques contiguos de memoria en C), las operaciones vectorizadas sin bucles tradicionales, el álgebra de matrices y las reglas fundamentales de **Broadcasting** para procesar millones de registros con máxima eficiencia computacional.

---

## 🗺️ Estructura del Módulo

| # | Cuaderno Interactivo | Temas Principales | Dificultad |
|:---:|---|---|:---:|
| **00** | [**Introducción a NumPy**](00_Introduccion_Numpy.ipynb) | Arquitectura de memoria contigua en C, comparación de rendimiento NumPy vs Listas nativas de Python y concepto de `ndarray`. | 🟢 Básico |
| **01** | [**Creación de Arrays en NumPy**](01_Creacion_de_Arrays_Numpy.ipynb) | Métodos de inicialización (`zeros`, `ones`, `full`, `arange`, `linspace`), atributos (`ndim`, `shape`, `size`, `dtype`) y tipos de datos numéricos. | 🟢 Básico |
| **02** | [**Operaciones con Arrays y Broadcasting**](02_Operaciones_con_Arrays_Numpy.ipynb) | Operaciones aritméticas vectorizadas, funciones universales (`ufuncs`), agregaciones (`sum`, `mean`, `std`, `min`, `max`) y reglas de *Broadcasting*. | 🟡 Intermedio |
| **03** | [**Indexación y Slicing Multidimensional**](03_Indexacion_y_Slicing_Numpy.ipynb) | Indexación básica por coordenadas, segmentación por rangos (*slicing*), vistas vs copias en memoria, máscaras booleanas y *Fancy Indexing*. | 🟡 Intermedio |
| **04** | [**Remodelación de Arrays (Reshaping)**](04_Reshaping_Numpy.ipynb) | Modificación dimensional con `.reshape()`, aplanado de arreglos (`flatten` vs `ravel`), transposición (`.T`) y el uso del comodín dimensional `-1`. | 🟡 Intermedio |
| **05** | [**Concatenación y Apilamiento**](05_Concatenacion_Numpy.ipynb) | Unión de matrices a lo largo de ejes con `np.concatenate`, apilamiento horizontal (`np.hstack`), vertical (`np.vstack`) y en profundidad (`np.dstack`). | 🟡 Intermedio |
| **06** | [**Temas Avanzados: Aleatorios, Únicos y Dimensiones**](06_Temas_Avanzados_Numpy.ipynb) | Generador pseudo-aleatorio moderno (`np.random.default_rng`), análisis de frecuencias con `np.unique` y manipulación de ejes (`np.expand_dims`, `np.squeeze`). | 🧗 Avanzado |

---

## 💡 Guías "Para Dummies" (Explicaciones Intuitivas Sin Jerga Compleja)

* [**00. Introducción a NumPy (Dummies)**](Para%20Dummies/00_Introduccion_Numpy_Dummies.ipynb): La autopista de alta velocidad frente al camino de tierra.
* [**01. Creación de Arrays (Dummies)**](Para%20Dummies/01_Creacion_de_Arrays_Numpy_Dummies.ipynb): La bandeja de huevos y las cuadrículas ordenadas.
* [**02. Operaciones y Broadcasting (Dummies)**](Para%20Dummies/02_Operaciones_con_Arrays_Numpy_Dummies.ipynb): Sumar a todos al mismo tiempo con la varita mágica.
* [**03. Indexación y Slicing (Dummies)**](Para%20Dummies/03_Indexacion_y_Slicing_Numpy_Dummies.ipynb): La batalla naval y cortar porciones de pastel.
* [**04. Reshaping (Dummies)**](Para%20Dummies/04_Reshaping_Numpy_Dummies.ipynb): Reacomodar las fichas de Lego sin perder ninguna.
* [**05. Concatenación (Dummies)**](Para%20Dummies/05_Concatenacion_Numpy_Dummies.ipynb): Pegar baldosas una al lado de la otra o una sobre otra.
* [**06. Temas Avanzados (Dummies)**](Para%20Dummies/06_Temas_Avanzados_Numpy_Dummies.ipynb): Tirar los dados y contar elementos únicos en el baúl.

---

## 📝 Talleres Prácticos Evaluativos (*Hands-On Homeworks*)

* 📝 [**02_NumPy_Hands_On.ipynb](../homeworks/02_NumPy_Hands_On.ipynb)**: Taller integral de cálculo numérico, álgebra lineal y manipulación vectorial con NumPy.
* 💡 [**02_NumPy_Hands_On_Dummies.ipynb](../homeworks/Para%20Dummies/02_NumPy_Hands_On_Dummies.ipynb)**: Taller guiado paso a paso para no ingenieros.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
