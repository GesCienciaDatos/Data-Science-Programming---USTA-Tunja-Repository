# Módulo 06: Ingeniería de Características (Feature Engineering) ⚙️

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción General

La **Ingeniería de Características (*Feature Engineering*)** es el arte y la ciencia de extraer, transformar y seleccionar las variables más informativas a partir de datos crudos para maximizar la capacidad predictiva de los algoritmos de Machine Learning.

En este módulo aprenderás las técnicas fundamentales aplicadas por los mejores equipos de ciencia de datos del mundo: codificación de variables categóricas nominales y ordinales, **Target Encoding** con regularización bayesiana (*m-estimate smoothing*), creación de ratios e interacciones matemáticas, reducción de dimensionalidad no supervisada mediante **Análisis de Componentes Principales (PCA)** y selección rigurosa de características basada en **Información Mutua (*Mutual Information*)**.

---

## 🗺️ Estructura del Módulo

| # | Cuaderno Interactivo | Temas Principales | Dificultad |
|:---:|---|---|:---:|
| **00** | [**Introducción a Feature Engineering**](00_Introduccion_Feature_Engineering.ipynb) | Filosofía de la ingeniería de características, impacto en el rendimiento de los modelos y flujo de trabajo. | 🟢 Básico |
| **01** | [**Variables Categóricas**](01_Variables_Categoricas_Feature_Engineering.ipynb) | Codificación ordinal (`OrdinalEncoder`), One-Hot Encoding (`OneHotEncoder`), manejo de categorías raras o no vistas y la maldición de la dimensionalidad. | 🟡 Intermedio |
| **02** | [**Target Encoding y Suavizado**](02_Target_Encoding_y_Suavizado_Feature_Engineering.ipynb) | Codificación por variable objetivo para categorías de alta cardinalidad, riesgo de fuga de datos (*Data Leakage*) y suavizado bayesiano con parámetro $m$. | 🧗 Avanzado |
| **03** | [**Creación de Características**](03_Creacion_de_Caracteristicas_Feature_Engineering.ipynb) | Ratios numéricos, combinaciones matemáticas, conteos de ocurrencias, transformaciones logarítmicas/Box-Cox y agregaciones grupales (*Group Transforms*). | 🟡 Intermedio |
| **04** | [**Análisis de Componentes Principales (PCA)**](04_PCA_Feature_Engineering.ipynb) | Reducción de dimensionalidad, proyecciones ortogonales, varianza explicada, matriz de covarianza y extracción de componentes no correlacionados. | 🧗 Avanzado |
| **05** | [**Selección de Características e Información Mutua**](05_Seleccion_Caracteristicas_y_Mutual_Information.ipynb) | Filtro univariado basado en entropía e Información Mutua (MI), detección de relaciones no lineales y selección de variables informativas. | 🟡 Intermedio |

---

## 💡 Guías "Para Dummies" (Explicaciones Intuitivas Sin Jerga Compleja)

* [**00. Introducción a Feature Engineering (Dummies)**](Para%20Dummies/00_Introduccion_Feature_Engineering_Dummies.ipynb): Cómo pulir el diamante en bruto para que el algoritmo aprenda mejor.
* [**01. Variables Categóricas (Dummies)**](Para%20Dummies/01_Variables_Categoricas_Feature_Engineering_Dummies.ipynb): Convertir palabras (ciudades, colores) en números que la máquina entienda.
* [**02. Target Encoding (Dummies)**](Para%20Dummies/02_Target_Encoding_y_Suavizado_Feature_Engineering_Dummies.ipynb): Reemplazar cada barrio por el precio promedio de sus casas sin hacer trampa.
* [**03. Creación de Variables (Dummies)**](Para%20Dummies/03_Creacion_de_Caracteristicas_Feature_Engineering_Dummies.ipynb): Inventar nuevas medidas útiles (como precio por metro cuadrado).
* [**04. PCA y Sombras 3D (Dummies)**](Para%20Dummies/04_PCA_Feature_Engineering_Dummies.ipynb): Proyectar una estatua 3D en su mejor sombra 2D sin perder los detalles clave.
* [**05. Información Mutua (Dummies)**](Para%20Dummies/05_Seleccion_Caracteristicas_y_Mutual_Information_Dummies.ipynb): El detector de pistas que te dice cuáles datos son oro y cuáles son basura.

---

## 📂 Conjuntos de Datos (*Datasets*)

En este módulo se emplean los siguientes datasets ubicados en la carpeta `data/`:
- `melb_data.csv`: Precios de viviendas y características inmobiliarias en Melbourne.
- `autos.csv`: Especificaciones técnicas y precios de automóviles.
- `concrete.csv`: Formulación de mezclas de concreto y su resistencia a la compresión.
- `accidents.csv`: Registro de accidentes viales en Estados Unidos.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
