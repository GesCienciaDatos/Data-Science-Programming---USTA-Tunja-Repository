# Módulo 09: Árboles de Decisión y Métodos de Ensamble (Decision Trees & Ensembles) 🌲🌳

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción del Módulo

Este módulo aborda de manera integral los **Modelos Basados en Árboles (*Tree-Based Methods*)** y los **Métodos de Ensamble (*Ensemble Methods*)**, fundamentales para la minería de datos y el modelado predictivo de alto rendimiento en problemas tabulares:
* **Árboles de Clasificación y Regresión (CART):** Métodos de división voraz (*Top-down induction*), criterios de impureza (**Índice de Gini** vs **Entropía / Ganancia de Información**), partición del espacio en hiper-rectángulos ortogonales.
* **Regularización y Poda (*Pruning*):** Control de complejidad, hiperparámetros (`max_depth`, `min_samples_leaf`, `min_samples_split`) y algoritmo formal de **Poda por Complejidad de Costo Mínimo (*Minimal Cost-Complexity Pruning / ccp_alpha*)**.
* **Bootstrap Aggregating (Bagging):** Reducción de varianza por remuestreo con reemplazo y estimación de error *Out-of-Bag (OOB)*.
* **Random Forests (Bosques Aleatorios):** Descorrelación de árboles mediante subespacios aleatorios de características e importancia relativa de variables (*Feature Importance*).
* **Boosting y Desbalance:** Aprendizaje secuencial sobre residuos (AdaBoost, Gradient Boosting, XGBoost) y estrategias de ponderación para clases desbalanceadas (`class_weight='balanced'`).

---

## 📓 Cuadernos de Clase (Notebooks)

El módulo se compone de **5 cuadernos interactivos estándar** y **5 guías complementarias *Para Dummies***:

| Cuaderno Estándar | Guía Para Dummies | Temáticas Principales |
|---|---|---|
| [**00_Introduccion_Decision_Trees.ipynb**](00_Introduccion_Decision_Trees.ipynb) | [**00_Introduccion_Decision_Trees_Dummies.ipynb**](Para%20Dummies/00_Introduccion_Decision_Trees_Dummies.ipynb) | Fundamentos de árboles CART, analogía de 20 preguntas, anatomía de nodos (raíz, internos, hojas) y visualización gráfica. |
| [**01_Criterios_Division_y_Arboles_Clasificacion.ipynb**](01_Criterios_Division_y_Arboles_Clasificacion.ipynb) | [**01_Criterios_Division_y_Arboles_Clasificacion_Dummies.ipynb**](Para%20Dummies/01_Criterios_Division_y_Arboles_Clasificacion_Dummies.ipynb) | Criterios matemáticos de impureza (Gini vs Entropía), Ganancia de Información (IG), fronteras ortogonales 2D y clasificación en `spam.csv`. |
| [**02_Arboles_Regresion_y_Poda_Cost_Complexity.ipynb**](02_Arboles_Regresion_y_Poda_Cost_Complexity.ipynb) | [**02_Arboles_Regresion_y_Poda_Cost_Complexity_Dummies.ipynb**](Para%20Dummies/02_Arboles_Regresion_y_Poda_Cost_Complexity_Dummies.ipynb) | Árboles continuos (`DecisionTreeRegressor`), criterios MSE/MAE, sobreajuste (*overfitting*) y poda formal por costo-complejidad (`ccp_alpha`). |
| [**03_Metodos_Ensamble_Bagging_y_Random_Forests.ipynb**](03_Metodos_Ensamble_Bagging_y_Random_Forests.ipynb) | [**03_Metodos_Ensamble_Bagging_y_Random_Forests_Dummies.ipynb**](Para%20Dummies/03_Metodos_Ensamble_Bagging_y_Random_Forests_Dummies.ipynb) | Principio de ensamble (*Wisdom of Crowds*), Bagging con error OOB, Random Forests con subespacios aleatorios e importancia de variables. |
| [**04_Boosting_y_Casos_Estudio_Desbalanceados.ipynb**](04_Boosting_y_Casos_Estudio_Desbalanceados.ipynb) | [**04_Boosting_y_Casos_Estudio_Desbalanceados_Dummies.ipynb**](Para%20Dummies/04_Boosting_y_Casos_Estudio_Desbalanceados_Dummies.ipynb) | Boosting secuencial, AdaBoost, Gradient Boosting, ajuste de clases desbalanceadas y benchmark comparativo integral. |

---

## 📂 Conjuntos de Datos (*Datasets*)

* **`data/spam.csv`:** Conjunto de datos real de detección de spam (4,601 observaciones, 57 predictores continuos de frecuencias de palabras/caracteres y variable binaria `Spam`).

---

## 📝 Talleres Prácticos Evaluativos (*Homeworks*)

* [**09_Decision_Trees_Hands_On.ipynb**](../homeworks/09_Decision_Trees_Hands_On.ipynb) — Taller evaluativo de 5 partes (Carga, selección de profundidad con CV, poda con `ccp_alpha`, Random Forest con OOB y optimización de Gradient Boosting con `GridSearchCV`).
* [**09_Decision_Trees_Hands_On_Dummies.ipynb**](../homeworks/Para%20Dummies/09_Decision_Trees_Hands_On_Dummies.ipynb) — Taller guiado paso a paso con analogías médicas y lenguaje intuitivo.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Plataforma de Laboratorios Virtuales</i>
  </p>
</div>
