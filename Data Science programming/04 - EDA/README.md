# Módulo 04: Análisis Exploratorio de Datos (EDA) 📊

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción General

El **Análisis Exploratorio de Datos (*Exploratory Data Analysis - EDA*)** es la fase fundamental de investigación estadística y visual que precede a cualquier modelado de Machine Learning o analítica avanzada.

En este módulo aprenderás a formular hipótesis, identificar patrones ocultos, anomalías y relaciones multivariadas utilizando la sinergia de **Pandas**, **Matplotlib** y **Seaborn**. Descubrirás por qué la visualización es indispensable frente al resumen estadístico simple (a través del histórico *Cuarteto de Anscombe*) y cómo estructurar tableros y visualizaciones con estándares de diseño profesional.

---

## 🗺️ Estructura del Módulo

| # | Cuaderno | Temas Principales | Dificultad |
|---|---|---|:---:|
| **00** | [**Introducción al EDA**](00_Introduccion_EDA.ipynb) | Conceptos fundamentales, etapas del EDA, objetivos de negocio y flujo de trabajo estructurado. | 🟢 Básico |
| **01** | [**Exploración Preliminar de Datos**](01_Exploracion_Preliminar_EDA.ipynb) | Diagnóstico inicial de estructura, dimensionalidad, tipos de variables y detección de valores atípicos y nulos. | 🟢 Básico |
| **02** | [**Estadística Descriptiva para EDA**](02_Estadistica_Descriptiva_EDA.ipynb) | Medidas de tendencia central (media, mediana, moda), dispersión (varianza, desviación estándar, IQR), asimetría (*skewness*) y curtosis. | 🟡 Intermedio |
| **03** | [**Visualización de Datos y Cuarteto de Anscombe**](03_Visualizacion_de_Datos_EDA.ipynb) | El Cuarteto de Anscombe (por qué ver los datos es vital), gráficos de dispersión, histogramas y boxplots base. | 🟡 Intermedio |
| **04** | [**Librerías de Visualización Avanzadas (Seaborn)**](04_Librerias_de_Visualizacion_EDA.ipynb) | Gráficos relacionales (`scatterplot`, `lineplot`), categóricos (`boxplot`, `violinplot`, `countplot`) y multivariados (`pairplot`, `heatmap` de correlación). | 🟡 Intermedio |
| **05** | [**Comparación de Librerías de Visualización**](05_Comparacion_Librerias_Visualizacion.ipynb) | Comparativa directa entre Pandas Plotting, Matplotlib (control de bajo nivel) y Seaborn (estética estadística de alto nivel). | 🟡 Intermedio |
| **06** | [**Resumen de Funciones y Guía Rápida**](06_Resumen_de_Funciones_EDA.ipynb) | Glosario interactivo de funciones clave, matriz de decisión de gráficos según el tipo de variable y buenas prácticas de visualización. | 🟢 Básico |

---

## 📂 Conjuntos de Datos (*Datasets*)

En los cuadernos de este módulo se utilizan conjuntos de datos locales y de referencia:
- `StudentsPerformance.csv`: Rendimiento académico y factores demográficos de estudiantes (local en `data/`).
- `quartets.csv`: El famoso Cuarteto de Anscombe (local en `data/`) que demuestra la necesidad de visualizar distribuciones.
- `tips`, `iris`, `titanic`: Datasets estadísticos clásicos integrados vía Seaborn.

---

## 📂 Taller Práctico Evaluativo (*Homework*)

Al finalizar el módulo de EDA, el estudiante debe resolver el taller práctico correspondiente:
- 📝 **[04_EDA_Hands_On.ipynb](../homeworks/04_EDA_Hands_On.ipynb)**: Taller integral de análisis exploratorio, generación de hipótesis estadísticas y visualización multivariada con datos reales.
