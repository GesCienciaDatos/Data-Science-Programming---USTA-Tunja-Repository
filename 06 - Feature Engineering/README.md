# Módulo 06: Feature Engineering (Ingeniería de Características) ⚙️

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción General

La **Ingeniería de Características (*Feature Engineering*)** es el arte y la disciplina técnica de transformar, enriquecer y seleccionar variables a partir de datos en bruto para construir representaciones matemáticas optimizadas que maximicen el poder predictivo, la estabilidad y la interpretabilidad de los modelos de Machine Learning.

En este módulo aprenderás las estrategias fundamentales y avanzadas del estado del arte:
* Codificación robusta de variables cualitativas y categóricas de alta cardinalidad.
* Regularización bayesiana mediante suavizado (*Smoothing / m-estimate*) para evitar el sobreajuste y la fuga de datos (*Data Leakage*).
* Creación estructurada de características numéricas mediante transformaciones matemáticas, conteos booleanos, ratios e interacciones grupales.
* Descubrimiento de relaciones latentes y descorrelación mediante **Análisis de Componentes Principales (PCA)**.
* Selección óptima de variables empleando **Información Mutua (Mutual Information)**, métodos de filtro, envoltura (*Wrapper*) y métodos embebidos (*Embedded / Regularización*).

---

## 🗺️ Estructura y Cuadernos del Módulo

| # | Cuaderno Interactivo | Temas Principales | Dificultad |
|:---:|---|---|:---:|
| **00** | [**Introducción a Feature Engineering**](00_Introduccion_Feature_Engineering.ipynb) | Fundamentos, ciclo de vida de las características, principio rector del modelado y hoja de ruta temática. | 🟢 Básico |
| **01** | [**Manejo de Variables Categóricas**](01_Variables_Categoricas_Feature_Engineering.ipynb) | Drop Variables, Ordinal Encoding, One-Hot Encoding, Mean Target Encoding y evaluación comparativa de MAE con Random Forest. | 🟢 Básico |
| **02** | [**Target Encoding y Suavizado (Smoothing)**](02_Target_Encoding_y_Suavizado_Feature_Engineering.ipynb) | Regularización bayesiana, estimador $m$ (*m-estimate*), curvas de peso, prevención de sobreajuste y caso de uso masivo con MovieLens 1M. | 🧗 Intermedio-Avanzado |
| **03** | [**Creación de Características (Creating Features)**](03_Creacion_de_Caracteristicas_Feature_Engineering.ipynb) | Transformaciones matemáticas, cocientes e interacciones, transformaciones logarítmicas, conteos booleanos, descomposición de cadenas y transformaciones agrupadas (*group transforms*) sin fuga de datos. | 🟡 Intermedio |
| **04** | [**Análisis de Componentes Principales (PCA)**](04_PCA_Feature_Engineering.ipynb) | Ejes de variación (*Abalone*), rotación ortogonal, análisis de cargas (*loadings*), varianza explicada, descubrimiento descriptivo guiado por MI y creación de variables derivadas. | 🧗 Intermedio-Avanzado |
| **05** | [**Selección de Características e Información Mutua**](05_Seleccion_Caracteristicas_y_Mutual_Information.ipynb) | La maldición de la dimensionalidad, métodos Filter, Wrapper y Embedded, entropía e Información Mutua (MI), ranking de utilidad y detección de efectos de interacción no lineales. | 🧗 Intermedio-Avanzado |

> 🧗 **Nota:** Los cuadernos identificados con el ícono de escalador abordan conceptos con mayor profundidad matemática, algorítmica y teórica.

---

## 📂 Conjuntos de Datos (*Datasets*)

Los cuadernos interactivos de este módulo emplean conjuntos de datos reales ubicados en la carpeta [`data/`](data/):

* **`autos.csv`**: Especificaciones mecánicas (potencia, peso, tamaño de motor, combustible) y precios de automóviles de 1985. Utilizado en PCA, transformaciones de ratios y selección de características con Información Mutua.
* **`melb_data.csv`**: Precios y atributos residenciales de viviendas en Melbourne (Australia). Empleado en la comparación de técnicas de codificación categórica.
* **`movielens1m.csv`**: 1 millón de calificaciones de películas con identificadores de usuarios, títulos y géneros. Empleado para Target Encoding de alta cardinalidad y suavizado $m$-estimate.
* **`accidents.csv`**: Registro de accidentes de tránsito y factores viales en EE.UU. Empleado para conteos de presencia y transformaciones espaciales.
* **`concrete.csv`**: Formulación de mezclas de concreto y su resistencia a la compresión. Utilizado para ratios físicos e interacciones numéricas.
* **`customer.csv`**: Historial de clientes, pólizas, reclamos y cobertura de seguros. Utilizado para transformaciones agrupadas (*group transforms*).

---

## 📚 Recursos y Lecturas Recomendadas

### 📖 Libros de Referencia
1. **[An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/)** — *Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani*.
2. **[Feature Engineering for Machine Learning](https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/)** — *Alice Zheng & Amanda Casari*.
3. **[The Kaggle Book: Data analysis and machine learning for competitive data science](https://www.packtpub.com/en-it/product/the-kaggle-book-9781801817479)** — *Konrad Banachewicz & Luca Massaron*.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
