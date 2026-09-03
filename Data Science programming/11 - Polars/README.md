# Módulo 11 (Extra): Polars y Procesamiento de Alto Rendimiento 🐻‍❄️⚡

<p align="center">
  <img src="https://img.shields.io/badge/Polars-v1.x-0284c7?style=for-the-badge&logo=polars&logoColor=white" alt="Polars"/>
  <img src="https://img.shields.io/badge/Language-Rust%20%26%20Python-f97316?style=for-the-badge&logo=rust&logoColor=white" alt="Rust"/>
  <img src="https://img.shields.io/badge/Format-Apache%20Arrow-0ea5e9?style=for-the-badge&logo=apachearrow&logoColor=white" alt="Apache Arrow"/>
  <img src="https://img.shields.io/badge/Execution-Multithreaded%20%26%20Lazy-10b981?style=for-the-badge" alt="Lazy"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al **Módulo Extra de Polars y Procesamiento de Alto Rendimiento** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**.

---

## 🧭 ¿Por qué Polars?

En la era del Big Data, los DataFrames tradicionales enfrentan cuellos de botella severos debido al consumo de memoria y la ejecución monohilo. **Polars** resuelve estos desafíos mediante:
- **Rust Engine:** Rendimiento nativo cercano al metal y paralelismo multihilo sin GIL.
- **Apache Arrow:** Estructura columnar contigua en memoria con aceleración SIMD.
- **Lazy Evaluation:** Optimizador de consultas que aplica *Predicate Pushdown* y *Projection Pushdown* antes de leer datos del disco.
- **Streaming Out-of-Core:** Capacidad para procesar conjuntos de datos que superan la memoria RAM disponible.

---

## 📚 Estructura de Cuadernos

### 🎓 Ruta Académica Estándar:
1. [**00_Introduccion_Polars_y_Estructuras_de_Datos.ipynb**](00_Introduccion_Polars_y_Estructuras_de_Datos.ipynb): Fundamentos, pilares arquitectónicos, `Series`, `DataFrame`, tipos de datos y lectura CSV/Parquet.
2. [**01_Expresiones_Contextos_y_Transformaciones.ipynb**](01_Expresiones_Contextos_y_Transformaciones.ipynb): El corazón de Polars (`select`, `with_columns`, `filter`), expresiones `pl.col()`, lógica condicional `when-then`, strings y fechas.
3. [**02_Agrupaciones_Joins_y_Funciones_Ventana.ipynb**](02_Agrupaciones_Joins_y_Funciones_Ventana.ipynb): Agregaciones multihilo con `group_by()`, joins (`inner`, `left`, `semi`, `anti`) y funciones de ventana con `.over()`.
4. [**03_LazyFrame_Optimizador_de_Consultas_y_Streaming.ipynb**](03_LazyFrame_Optimizador_de_Consultas_y_Streaming.ipynb): Evaluación perezosa, auditoría del grafo con `.explain()`, optimizaciones pushdown y motor de streaming.
5. [**04_Interoperabilidad_Benchmark_Pandas_vs_Polars_y_Big_Data.ipynb**](04_Interoperabilidad_Benchmark_Pandas_vs_Polars_y_Big_Data.ipynb): Interoperabilidad Zero-Copy con Apache Arrow, gran benchmark comparativo de tiempos, y buenas prácticas.

---

### 🧸 Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/):
1. [**00_Introduccion_Polars_Dummies.ipynb**](Para%20Dummies/00_Introduccion_Polars_Dummies.ipynb): ¿Por qué Polars es un bólido de carreras y Pandas un camión pesado?
2. [**01_Expresiones_Contextos_Dummies.ipynb**](Para%20Dummies/01_Expresiones_Contextos_Dummies.ipynb): Los 3 contextos mágicos (`select`, `with_columns`, `filter`) explicados con analogías cotidianas.
3. [**02_Agrupaciones_Joins_Dummies.ipynb**](Para%20Dummies/02_Agrupaciones_Joins_Dummies.ipynb): Resumiendo datos y uniendo piezas sin que se congele tu computadora.
4. [**03_LazyFrame_Optimizador_Dummies.ipynb**](Para%20Dummies/03_LazyFrame_Optimizador_Dummies.ipynb): La pereza inteligente: planear todo antes de ejecutar para ser el más rápido de la clase.
5. [**04_Benchmark_Pandas_vs_Polars_Dummies.ipynb**](Para%20Dummies/04_Benchmark_Pandas_vs_Polars_Dummies.ipynb): La gran carrera en vivo con cronómetro y los 3 pecados capitales a evitar.

---

## 💾 Conjuntos de Datos Incluidos

En la carpeta [`data/`](data/) se encuentran generados los datasets de prueba:
* `ventas.csv` y `ventas.parquet`: 60,000 registros de ventas comerciales con fechas, productos y descuentos.
* `clientes.csv` y `clientes.parquet`: 1,500 clientes con datos demográficos y segmentos.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
