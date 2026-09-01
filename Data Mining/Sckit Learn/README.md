# Módulo: Scikit-Learn (Fundamentos, Arquitectura y Utilidades) ⚙️

> **Especialización en Ciencia de Datos**  
> **Asignatura:** Minería de Datos (*Data Mining*) — Semestre II  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente / Gestor Virtual:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción del Módulo

Este módulo constituye la base instrumental y metodológica de la biblioteca **Scikit-Learn** (`sklearn`) para la Minería de Datos y el Aprendizaje Automático. Se enfoca exhaustivamente en la arquitectura de software, el diseño de la API, las utilidades de carga de datos, técnicas avanzadas de preprocesamiento, esquemas de partición, validación cruzada, métricas de evaluación, ensamblaje de `Pipelines` y optimización de hiperparámetros.

> ⚠️ **Alcance Curricular:** En este módulo se abordan exclusivamente los fundamentos de la API, transformadores, validadores y selectores de características sin profundizar en modelos predictivos específicos (KNN, SVM, Árboles de Decisión, Redes Neuronales), los cuales se desarrollan en sus respectivos módulos temáticos independientes.

---

## 📓 Estructura de Cuadernos Interactivos

### 📘 Edición Estándar (Académica)
1. **[00_Introduccion_y_Arquitectura_Scikit_Learn.ipynb](00_Introduccion_y_Arquitectura_Scikit_Learn.ipynb):** Filosofía, principios de diseño, Estimators, Transformers y Predictors.
2. **[01_Carga_y_Generacion_de_Datasets.ipynb](01_Carga_y_Generacion_de_Datasets.ipynb):** Toy datasets (`load_iris`, `load_wine`), OpenML, generadores sintéticos (`make_classification`, `make_blobs`).
3. **[02_Preprocesamiento_y_Transformacion_de_Datos.ipynb](02_Preprocesamiento_y_Transformacion_de_Datos.ipynb):** Escalamiento (`StandardScaler`, `RobustScaler`), imputación (`SimpleImputer`, `KNNImputer`), codificación (`OneHotEncoder`).
4. **[03_Particion_y_Estrategias_de_Validacion.ipynb](03_Particion_y_Estrategias_de_Validacion.ipynb):** Partición Train/Test, `KFold`, `StratifiedKFold`, `TimeSeriesSplit` y catálogo de métricas.
5. **[04_Pipelines_y_ColumnTransformer.ipynb](04_Pipelines_y_ColumnTransformer.ipynb):** Ensamblaje modular, prevención de *Data Leakage*, `ColumnTransformer` y serialización con `joblib`.
6. **[05_Optimizacion_de_Hiperparametros_y_Model_Selection.ipynb](05_Optimizacion_de_Hiperparametros_y_Model_Selection.ipynb):** Búsqueda en grilla (`GridSearchCV`), búsqueda aleatoria (`RandomizedSearchCV`), curvas de validación y aprendizaje.

### 💡 Edición Para Dummies (Conceptos Intuitivos)
1. **[00_Scikit_Learn_Para_Dummies.ipynb](Para%20Dummies/00_Scikit_Learn_Para_Dummies.ipynb):** Scikit-Learn explicado como una fábrica de bloques LEGO.
2. **[01_Datasets_y_Preprocesamiento_Para_Dummies.ipynb](Para%20Dummies/01_Datasets_y_Preprocesamiento_Para_Dummies.ipynb):** Limpiar datos explicado con analogías de cocina y filtros.
3. **[02_Pipelines_y_Validacion_Para_Dummies.ipynb](Para%20Dummies/02_Pipelines_y_Validacion_Para_Dummies.ipynb):** Pipelines explicados como bandas transportadoras automáticas.

---

## 📚 Bibliografía de Referencia

1. **Garreta, R., & Moncecchi, G. (2013).** *Learning scikit-learn: Machine Learning in Python*. Packt Publishing.
2. **Buitinck, L., et al. (2013).** *API design for machine learning software: experiences from the scikit-learn project*. arXiv preprint arXiv:1309.0238.
3. **Pedregosa, F., et al. (2011).** *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825-2830.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Plataforma de Laboratorios Virtuales</i>
  </p>
</div>
