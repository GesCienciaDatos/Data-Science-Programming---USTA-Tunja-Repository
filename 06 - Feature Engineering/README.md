# Módulo 06: Feature Engineering (Ingeniería de Características) ⚙️

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción General

La **Ingeniería de Características (*Feature Engineering*)** es el arte y la ciencia de transformar datos sin procesar en representaciones matemáticas y estadísticas optimizadas para maximizar el poder predictivo y la interpretabilidad de los modelos de Machine Learning.

En este módulo aprenderás las técnicas fundamentales y avanzadas para codificar variables cualitativas, regularizar codificaciones de alta cardinalidad mediante suavizado bayesiano, detectar y tratar valores atípicos (*outliers*), generar nuevas características derivadas y aplicar métodos de reducción de dimensionalidad y selección de variables.

---

## 🗺️ Estructura del Módulo

| # | Cuaderno | Temas Principales | Dificultad |
|---|---|---|:---:|
| **00** | [**Introducción a Feature Engineering**](00_Introduccion_Feature_Engineering.ipynb) | Fundamentos, ciclo de vida, principios de transformación y selección. | 🟢 Básico |
| **01** | [**Manejo de Variables Categóricas**](01_Variables_Categoricas_Feature_Engineering.ipynb) | Drop Variables, Ordinal Encoding, One-Hot Encoding, Mean Target Encoding y evaluación de modelos. | 🟢 Básico |
| **02** | [**Target Encoding y Suavizado (Smoothing)**](02_Target_Encoding_y_Suavizado_Feature_Engineering.ipynb) | Regularización bayesiana, estimador $m$ (*m-estimate*), curvas de peso, casos de uso y caso práctico masivo con MovieLens 1M. | 🧗 Intermedio-Avanzado |
| **03** | [**Tratamiento de Outliers y Creación de Características**](03_Outliers_y_Creacion_Caracteristicas.ipynb) | Detección estadística (IQR, Z-score, Isolation Forest), *winsorizing*, transformaciones matemáticas y ratios. | 🟡 Intermedio |
| **04** | [**Análisis de Componentes Principales (PCA)**](04_PCA_Feature_Engineering.ipynb) | Reducción de dimensionalidad, proyecciones ortogonales, varianza explicada y extracción de componentes. | 🧗 Intermedio-Avanzado |
| **05** | [**Selección de Características e Información Mutua**](05_Seleccion_Caracteristicas_y_Mutual_Information.ipynb) | Información mutua (*Mutual Information*), métodos de filtro, wrapper y regularización L1/L2. | 🧗 Intermedio-Avanzado |

---

## 📂 Conjuntos de Datos (*Datasets*)

Los cuadernos de este módulo emplean los siguientes conjuntos de datos ubicados en la carpeta `data/`:
- `melb_data.csv`: Precios y características de viviendas en Melbourne (Australia).
- `autos.csv`: Especificaciones técnicas y precios de automóviles de 1985.
- `movielens1m.csv`: 1 millón de calificaciones de películas con metadatos de usuarios y géneros.
