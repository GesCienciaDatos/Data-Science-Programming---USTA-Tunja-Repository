# Módulo 05: Preparación y Limpieza de Datos (Data Preparation) 🧹

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción General

En el mundo real, los datos nunca vienen limpios ni listos para su uso directo. La **Preparación y Limpieza de Datos (*Data Preparation / Cleaning*)** representa típicamente entre el 60% y el 80% del tiempo de un científico de datos.

En este módulo aprenderás las metodologías estándar para diagnosticar y tratar datos faltantes mediante imputación univariada y multivariada con Scikit-Learn, transformar y reescalar atributos continuos (*Feature Scaling* con Min-Max y StandardScaler), manipular tipos temporales (`datetime`), y corregir inconsistencias en texto mediante algoritmos de coincidencia difusa (*Fuzzy Matching* con distancia de Levenshtein).

---

## 🗺️ Estructura del Módulo

| # | Cuaderno Interactivo | Temas Principales | Dificultad |
|:---:|---|---|:---:|
| **00** | [**Introducción a la Preparación de Datos**](00_Introduccion_Data_Preparation.ipynb) | El ciclo de vida de los datos, el principio *Garbage In - Garbage Out* y visión general del pipeline de preprocesamiento. | 🟢 Básico |
| **01** | [**Valores Faltantes (Missing Values)**](01_Valores_Faltantes_Data_Preparation.ipynb) | Tipos de datos faltantes (MCAR, MAR, MNAR), diagnóstico con mapas de calor, eliminación controlada, imputación simple (`SimpleImputer`), imputación avanzada y creación de indicadores booleanos. | 🟡 Intermedio |
| **02** | [**Escalado de Características (Feature Scaling)**](02_Escalado_Caracteristicas_Data_Preparation.ipynb) | Normalización (*Min-Max Scaling*), Estandarización (*StandardScaler / Z-score*), transformaciones robustas (*RobustScaler*) y su impacto crítico en algoritmos basados en distancia y gradiente. | 🟡 Intermedio |
| **03** | [**Fechas y Datos Inconsistentes**](03_Fechas_y_Datos_Inconsistentes_Data_Preparation.ipynb) | Parseo robusto de formatos de fecha con `pd.to_datetime`, extracción de atributos temporales (año, mes, día, hora, día de la semana) y resolución de inconsistencias tipográficas con *Fuzzy Matching* (`fuzzywuzzy`). | 🟡 Intermedio |

---

## 💡 Guías "Para Dummies" (Explicaciones Intuitivas Sin Jerga Compleja)

* [**00. Introducción a Data Preparation (Dummies)**](Para%20Dummies/00_Introduccion_Data_Preparation_Dummies.ipynb): Limpiar los ingredientes antes de cocinar para no dañar la receta.
* [**01. Datos Faltantes (Dummies)**](Para%20Dummies/01_Valores_Faltantes_Data_Preparation_Dummies.ipynb): ¿Qué hacemos con los huecos en la libreta? Rellenar con la media o borrar la hoja.
* [**02. Escalado de Variables (Dummies)**](Para%20Dummies/02_Escalado_Caracteristicas_Data_Preparation_Dummies.ipynb): Medir todo con la misma regla para no comparar elefantes con hormigas.
* [**03. Fechas y Errores de Escritura (Dummies)**](Para%20Dummies/03_Fechas_y_Datos_Inconsistentes_Data_Preparation_Dummies.ipynb): Traducir fechas enredadas y corregir nombres con errores de ortografía.

---

## 📂 Conjuntos de Datos (*Datasets*)

En este módulo se emplean los siguientes datasets ubicados en la carpeta `data/`:
- `hepatitis.csv`: Registros clínicos de pacientes con hepatitis (diagnóstico de valores nulos e imputación con Scikit-Learn).
- `landslide-events.csv`: Base de datos de eventos de deslizamientos de tierra a nivel global (parseo de fechas y análisis temporal).
- `pakistan_intellectual_capital.csv`: Registro académico con entradas de texto y nombres de países con errores tipográficos (*Fuzzy Matching* con distancia de Levenshtein).

---

## 📝 Talleres Prácticos Evaluativos (*Hands-On Homeworks*)

* 📝 [**05_Data_Preparation_Hands_On.ipynb**](../homeworks/05_Data_Preparation_Hands_On.ipynb): Taller integral de tratamiento de valores nulos, escalado comparativo y limpieza de texto y fechas.
* 💡 [**05_Data_Preparation_Hands_On_Dummies.ipynb**](../homeworks/Para%20Dummies/05_Data_Preparation_Hands_On_Dummies.ipynb): Taller guiado paso a paso para no ingenieros.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
