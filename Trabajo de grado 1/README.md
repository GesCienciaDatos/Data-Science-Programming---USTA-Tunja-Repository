# Trabajo de Grado 1 — Especialización en Ciencia de Datos
### Universidad Santo Tomás — Seccional Tunja

Bienvenido al espacio académico oficial de **Trabajo de Grado 1** de la Especialización en Ciencia de Datos. Este módulo está diseñado para guiar a los estudiantes en la estructuración, desarrollo, gobernanza y despliegue de soluciones analíticas integrales de alto impacto basadas en metodologías ágiles (**Scrum**), marcos de ciclo de vida analítico (**CRISP-DM**) y arquitectura moderna de **MLOps**.

---

## 🎬 Video Tutorial Oficial en YouTube

Como parte del material pedagógico del espacio académico, se encuentra disponible la serie de video tutoriales prácticos guiados paso a paso:

* **Enlace directo al tutorial:** [Ver Video Tutorial en YouTube (Databricks, MLflow y MLOps)](https://www.youtube.com/watch?v=B-8HK8GJfZM)

[![Tutorial Databricks Community Edition y MLOps](https://img.youtube.com/vi/B-8HK8GJfZM/maxresdefault.jpg)](https://www.youtube.com/watch?v=B-8HK8GJfZM)

> **Contenido del Video:** Creación de cuenta en Databricks Community Edition, configuración de clústeres serverless, ingesta en tablas Delta Lake con transacciones ACID, experiment tracking con MLflow, registro y versionamiento de modelos en el Model Registry y despliegue de endpoints de inferencia.

---

## 📚 Estructura de Módulos y Cuadernos Interactivos

El repositorio organiza el ciclo de vida del proyecto en tres módulos prácticos ejecutables:

### 🧱 Módulo 01: Databricks Standalone & MLOps
* **Cuaderno:** [`01 - Databricks Community Edition/02_Databricks_Community_Calidad_Vinos.ipynb`](./01%20-%20Databricks%20Community%20Edition/02_Databricks_Community_Calidad_Vinos.ipynb)
* **Script Python:** [`01 - Databricks Community Edition/02_Databricks_Community_Calidad_Vinos.py`](./01%20-%20Databricks%20Community%20Edition/02_Databricks_Community_Calidad_Vinos.py)
* **Objetivo:** Ingesta y persistencia en Delta Lake (formato Delta transaccional), formulación de hipótesis científicas, experimentación con modelos de ensamble Random Forest, tracking de métricas/artefactos en MLflow y registro formal en el Model Registry.

### ☁️ Módulo 02: Arquitectura Cloud AWS S3 y MLOps Serverless
* **Cuaderno:** [`02 - AWS Databricks y Lakehouse S3/03_DataLakehouse_AWS_S3_MLOps.ipynb`](./02%20-%20AWS%20Databricks%20y%20Lakehouse%20S3/03_DataLakehouse_AWS_S3_MLOps.ipynb)
* **Script Python:** [`02 - AWS Databricks y Lakehouse S3/03_DataLakehouse_AWS_S3_MLOps.py`](./02%20-%20AWS%20Databricks%20y%20Lakehouse%20S3/03_DataLakehouse_AWS_S3_MLOps.py)
* **Dataset:** [`02 - AWS Databricks y Lakehouse S3/data/california_housing_raw.csv`](./02%20-%20AWS%20Databricks%20y%20Lakehouse%20S3/data/california_housing_raw.csv)
* **Objetivo:** Conexión y persistencia en buckets de Amazon S3 como Data Lakehouse (capas raw, curated y models), orquestación en Databricks Serverless sobre AWS, evaluación de convergencia de hiperparámetros (`n_estimators`) frente a RMSE en el dataset California Housing.

### 🔷 Módulo 03: Microsoft Azure Databricks & Model Serving
* **Cuaderno:** [`03 - Azure Databricks y MLOps/04_Experimento_ML_Azure_Databricks.ipynb`](./03%20-%20Azure%20Databricks%20y%20MLOps/04_Experimento_ML_Azure_Databricks.ipynb)
* **Script Python:** [`03 - Azure Databricks y MLOps/04_Experimento_ML_Azure_Databricks.py`](./03%20-%20Azure%20Databricks%20y%20MLOps/04_Experimento_ML_Azure_Databricks.py)
* **Objetivo:** Despliegue de analítica en Azure Databricks (recurso 1st-party autenticado con Microsoft Entra ID), almacenamiento en Azure Data Lake Storage Gen2 (ADLS Gen2), regularización con Support Vector Machines (SVM con kernel RBF) para optimización de sensibilidad clínica (*Recall*) y control de falsos negativos.

---

## 📖 Guías Técnicas y Metodológicas Disponibles en `Guias/`

1. **Jira Software & Scrum:** `Guias/guia_01_jira_software.md` — Gobernanza ágil y roles duales (Product Owner / Data Owner, Scrum Master / Data Steward, Data Custodian, Data Consumer).
2. **Databricks Standalone:** `Guias/guia_02_databricks_directo.md` — Creación de clústeres, Delta tables y MLflow.
3. **AWS Databricks & S3:** `Guias/guia_03_databricks_aws.md` — Configuración IAM, buckets S3 y despliegue E2.
4. **Azure Databricks:** `Guias/guia_04_azure_databricks.md` — Creación del recurso en el portal Azure, clusters y conexión ADLS Gen2.
5. **MLflow & Versionamiento:** `Guias/guia_05_mlflow_versionamiento.md` — Métricas, parámetros, artefactos y solución de errores comunes.
