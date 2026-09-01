# Módulo 08: Clasificación (Classification) 🎯

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción General

La **Clasificación (*Classification*)** es la rama central del Aprendizaje Automático Supervisado orientada a predecir variables cualitativas, discretas o categóricas ($y \in \{C_1, C_2, \dots, C_K\}$). A diferencia de la regresión, los modelos de clasificación estiman la **probabilidad condicional a posteriori** de pertenencia a una clase determinada y establecen **fronteras de decisión** en el espacio de características.

En este módulo aprenderás las metodologías fundamentales y avanzadas del modelado predictivo cualitativo:
* Fundamentos probabilísticos de la clasificación y por qué la Regresión Lineal OLS falla para variables discretas.
* Formulación analítica de la **Regresión Logística (*Logistic Regression*)**, razón de momios (*Odds Ratio* $e^\beta$), función de pérdida *Binary Cross-Entropy / Log-Loss* y optimización por Máxima Verosimilitud (MLE).
* Extensión multiclase mediante **One-vs-Rest (OvR)** y **Multinomial Softmax**.
* Visualización e interpretación geométrica de **Fronteras de Decisión (*Decision Boundaries*)** lineales y no lineales con expansiones polinomiales (`PolynomialFeatures`).
* Control del sobreajuste mediante regularización **Lasso ($L_1$)**, **Ridge ($L_2$)** y ajuste del parámetro de penalización inversa $C = \frac{1}{\lambda}$.
* Evaluación diagnóstica rigurosa más allá de la exactitud (*Accuracy*): **Matriz de Confusión**, **Precisión**, **Exhaustividad / Sensibilidad (*Recall*)**, **Especificidad**, **$F_1$-Score**, Curvas **ROC-AUC** y curvas **Precision-Recall (PR-AUC)** para conjuntos de datos desbalanceados.
* Algoritmo no paramétrico basado en instancias: **$k$-Nearest Neighbors ($k$-NN Classifier)** y la **importancia crítica del escalado de variables (`StandardScaler`)**.
* Validación Cruzada Estratificada (**`StratifiedKFold`**), construcción de **`Pipeline`** robustos y optimización de hiperparámetros con **`GridSearchCV`**.

---

## 🗺️ Estructura y Cuadernos del Módulo

| # | Cuaderno Interactivo | Temas Principales | Dificultad |
|:---:|---|---|:---:|
| **00** | [**Introducción a la Clasificación**](00_Introduccion_Classification.ipynb) | Paradigma cualitativo, probabilidades acotadas, función Sigmoide $\sigma(z)$, limitaciones de la regresión lineal en clasificación y hoja de ruta del módulo. | 🟢 Básico |
| **01** | [**Regresión Logística Simple y Múltiple**](01_Regresion_Logistica_Simple_y_Multiple.ipynb) | Formulación del Logit, Odds Ratio, interpretación clínica de coeficientes, estimación MLE, `predict_proba` vs `predict` y umbrales de decisión con `heart_disease.csv`. | 🟢 Básico-Intermedio |
| **02** | [**Clasificación Multiclase y Fronteras de Decisión**](02_Clasificacion_Multiclase_y_Fronteras_Decision.ipynb) | Softmax vs One-vs-Rest, mapas 2D de regiones de decisión con `Iris`, transformaciones polinomiales no lineales y regularización $L_1$/$L_2$ (parámetro $C$). | 🟡 Intermedio |
| **03** | [**Evaluación de Modelos y Métricas de Clasificación**](03_Evaluacion_de_Modelos_y_Metricas_Clasificacion.ipynb) | Matriz de Confusión (VP, VN, FP, FN), Precision, Recall, Especificidad, F1-Score, Curva ROC-AUC, Precision-Recall y ajuste óptimo de umbral con índice de Youden en `customer_churn.csv`. | 🧗 Intermedio-Avanzado |
| **04** | [**k-NN Clasificación y Selección de Modelos**](04_KNN_Clasificacion_y_Seleccion_Modelos.ipynb) | Modelo no paramétrico $k$-NN, métricas de distancia (Euclidiana, Manhattan), impacto crítico de `StandardScaler`, dilema Sesgo-Varianza, `StratifiedKFold`, `Pipeline` y optimización con `GridSearchCV`. | 🧗 Intermedio-Avanzado |

---

## 💡 Guías "Para Dummies" (Explicaciones Prácticas y Sin Fórmulas Complejas)

Para estudiantes que deseen afianzar los conceptos con analogías cotidianas e intuitivas:

* [**00. Introducción a la Clasificación (Dummies)**](Para%20Dummies/00_Introduccion_Classification_Dummies.ipynb): La analogía del semáforo, el clasificador de correo Spam y la curva mágica en 'S'.
* [**01. Regresión Logística (Dummies)**](Para%20Dummies/01_Regresion_Logistica_Simple_y_Multiple_Dummies.ipynb): La balanza de decisiones y el medidor de porcentaje de probabilidad.
* [**02. Clasificación Multiclase (Dummies)**](Para%20Dummies/02_Clasificacion_Multiclase_y_Fronteras_Decision_Dummies.ipynb): Cómo dibujar las cercas y parcelas en el mapa de las flores.
* [**03. Evaluación de Modelos (Dummies)**](Para%20Dummies/03_Evaluacion_de_Modelos_y_Metricas_Clasificacion_Dummies.ipynb): La prueba médica y la alarma contra incendios (falsas alarmas vs emergencias reales).
* [**04. Algoritmo k-NN (Dummies)**](Para%20Dummies/04_KNN_Clasificacion_y_Seleccion_Modelos_Dummies.ipynb): "Dime con quién andas y te diré quién eres" y la importancia de medir con la misma cinta métrica.

---

## 📝 Talleres Prácticos Evaluativos (*Hands-On Homeworks*)

* [**08_Classification_Hands_On.ipynb**](../homeworks/08_Classification_Hands_On.ipynb): Taller integral y autónomo con Regresión Logística, análisis de Odds Ratios, matriz de confusión, ROC-AUC, curva PR y optimización de $k$-NN con `GridSearchCV`.
* [**08_Classification_Hands_On_Dummies.ipynb**](../homeworks/Para%20Dummies/08_Classification_Hands_On_Dummies.ipynb): Taller guiado paso a paso con analogías y explicaciones sencillas para no ingenieros.

---

## 📂 Conjuntos de Datos (*Datasets*)

* **`iris.csv`**: Colección botánica de Fisher (150 observaciones, 4 variables métricas: sépalos y pétalos, 3 especies: *Setosa*, *Versicolor*, *Virginica*).
* **`heart_disease.csv`**: Indicadores clínicos y cardiovasculares (300 observaciones: edad, presión arterial, colesterol, frecuencia cardiaca máxima, diagnóstico de cardiopatía).
* **`customer_churn.csv`**: Retención y cancelación de clientes en telecomunicaciones (400 observaciones: antigüedad, cargos mensuales, tipo de contrato, llamadas a soporte, fuga de clientes).

---

## 📚 Recursos y Lecturas Recomendadas

1. **[An Introduction to Statistical Learning (ISLP)](https://www.statlearning.com/)** — *Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani (Capítulo 4: Classification)*.
2. **[Scikit-Learn Guide: Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)**.
3. **[Scikit-Learn Guide: Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html)**.
4. **[Scikit-Learn Guide: Model Evaluation & Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)**.
5. **[Harvard CS109-A: Introduction to Data Science](https://harvard-iacs.github.io/2021-CS109A/)**.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
