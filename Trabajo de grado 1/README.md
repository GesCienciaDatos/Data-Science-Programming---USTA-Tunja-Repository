# Trabajo de Grado 1 — Especialización en Ciencia de Datos 🎓🚀

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Nivel Académico:** Semestre II  
> **Docente / Gestor Virtual:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-MLOps%20%26%20Cloud%20Architecture-0284c7?style=for-the-badge&logo=databricks&logoColor=white" alt="Databricks & MLOps"/>
  <img src="https://img.shields.io/badge/Topics-AWS%20S3%20%7C%20Azure%20%7C%20Delta%20Lake%20%7C%20MLflow-0ea5e9?style=for-the-badge" alt="Temas"/>
  <img src="https://img.shields.io/badge/Course-Trabajo%20de%20Grado%201-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/📚%20Biblioteca-28%20Libros%20de%20Referencia-10b981?style=for-the-badge&logo=gitbook&logoColor=white" alt="28 Libros"/>
  <img src="https://img.shields.io/badge/📖%20Guías%20PDF-2%20Documentos%20Oficiales-f59e0b?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Guías PDF"/>
  <img src="https://img.shields.io/badge/🎬%20YouTube-Video%20Clases-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube"/>
</p>

---

## 📌 Descripción de la Asignatura

Bienvenido al espacio académico oficial de **Trabajo de Grado 1** de la Especialización en Ciencia de Datos. Este módulo está diseñado para guiar a los estudiantes en la estructuración, desarrollo, gobernanza y despliegue de soluciones analíticas integrales de alto impacto basadas en:
- Metodologías ágiles de proyectos analíticos (**Scrum**) y marcos de ciclo de vida de minería de datos (**CRISP-DM**).
- Arquitecturas modernas de **Data Lakehouse** y almacenamiento transaccional **Delta Lake** (con garantías ACID).
- Prácticas de ingeniería de **MLOps** para trazabilidad de experimentos (*experiment tracking* con **MLflow**), versionamiento de modelos en el **Model Registry** y despliegue de inferencia.
- Entornos multi-nube en las plataformas líderes de la industria: **Databricks Community Edition**, **Amazon Web Services (AWS S3 & IAM)** y **Microsoft Azure (Azure Databricks & ADLS Gen2)**.
- Rigor metodológico en el **Diseño y Análisis de Experimentos Científicos** para la formulación de hipótesis, evaluación controlada y verificación empírica.

---

## 🎬 Video Tutorial Oficial en YouTube

Como parte del material pedagógico del espacio académico, se encuentra disponible la serie de video tutoriales prácticos guiados paso a paso:

* **Enlace directo al tutorial:** [Ver Video Tutorial en YouTube (Databricks, MLflow y MLOps)](https://www.youtube.com/watch?v=B-8HK8GJfZM)

[![Tutorial Databricks Community Edition y MLOps](https://img.youtube.com/vi/B-8HK8GJfZM/maxresdefault.jpg)](https://www.youtube.com/watch?v=B-8HK8GJfZM)

> **Contenido del Video:**
> 1. Acceso y aprovisionamiento en Databricks Community Edition sin costo ni tarjeta de crédito.
> 2. Configuración de clústeres serverless e inicialización del espacio de trabajo.
> 3. Ingesta y persistencia en tablas Delta Lake con transacciones ACID.
> 4. Experiment tracking sistemático de métricas, parámetros y artefactos con MLflow.
> 5. Registro y versionamiento formal de modelos en el Model Registry de Databricks.
> 6. Despliegue de modelos para inferencia y gobierno del ciclo de vida analítico.

---

## 📚 Estructura de Módulos y Cuadernos Interactivos

El repositorio organiza el ciclo de vida del proyecto en tres módulos prácticos ejecutables:

### 🧱 Módulo 01: Databricks Standalone & MLOps
* **Cuaderno Interactivo:** [`01 - Databricks Community Edition/02_Databricks_Community_Calidad_Vinos.ipynb`](./01%20-%20Databricks%20Community%20Edition/02_Databricks_Community_Calidad_Vinos.ipynb)
* **Script de Producción:** [`01 - Databricks Community Edition/02_Databricks_Community_Calidad_Vinos.py`](./01%20-%20Databricks%20Community%20Edition/02_Databricks_Community_Calidad_Vinos.py)
* **Guía de Apoyo:** [`Guias/guia_databricks_free_edition.pdf`](./Guias/guia_databricks_free_edition.pdf) (3.7 MB)
* **Objetivo:** Ingesta y persistencia en Delta Lake (formato Delta transaccional), formulación de hipótesis científicas, experimentación con modelos de ensamble Random Forest, tracking de métricas/artefactos en MLflow y registro formal en el Model Registry.

### ☁️ Módulo 02: Arquitectura Cloud AWS S3 y MLOps Serverless
* **Cuaderno Interactivo:** [`02 - AWS Databricks y Lakehouse S3/03_DataLakehouse_AWS_S3_MLOps.ipynb`](./02%20-%20AWS%20Databricks%20y%20Lakehouse%20S3/03_DataLakehouse_AWS_S3_MLOps.ipynb)
* **Script de Producción:** [`02 - AWS Databricks y Lakehouse S3/03_DataLakehouse_AWS_S3_MLOps.py`](./02%20-%20AWS%20Databricks%20y%20Lakehouse%20S3/03_DataLakehouse_AWS_S3_MLOps.py)
* **Dataset de Práctica:** [`02 - AWS Databricks y Lakehouse S3/data/california_housing_raw.csv`](./02%20-%20AWS%20Databricks%20y%20Lakehouse%20S3/data/california_housing_raw.csv)
* **Guía de Apoyo:** [`Guias/guia_databricks_aws.pdf`](./Guias/guia_databricks_aws.pdf) (6.3 MB)
* **Objetivo:** Conexión y persistencia en buckets de Amazon S3 como Data Lakehouse (capas raw, curated y models), orquestación en Databricks Serverless sobre AWS, evaluación de convergencia de hiperparámetros (`n_estimators`) frente a RMSE en el dataset California Housing.

### 🔷 Módulo 03: Microsoft Azure Databricks & Model Serving
* **Cuaderno Interactivo:** [`03 - Azure Databricks y MLOps/04_Experimento_ML_Azure_Databricks.ipynb`](./03%20-%20Azure%20Databricks%20y%20MLOps/04_Experimento_ML_Azure_Databricks.ipynb)
* **Script de Producción:** [`03 - Azure Databricks y MLOps/04_Experimento_ML_Azure_Databricks.py`](./03%20-%20Azure%20Databricks%20y%20MLOps/04_Experimento_ML_Azure_Databricks.py)
* **Objetivo:** Despliegue de analítica en Azure Databricks (recurso 1st-party autenticado con Microsoft Entra ID), almacenamiento en Azure Data Lake Storage Gen2 (ADLS Gen2), regularización con Support Vector Machines (SVM con kernel RBF) para optimización de sensibilidad clínica (*Recall*) y control de falsos negativos.

---

## 📖 Guías Prácticas Oficiales en PDF (`Guias/`)

El espacio académico cuenta con **documentos técnicos oficiales en formato PDF** de alta fidelidad, con diagramas arquitectónicos, flujos paso a paso y códigos listos para producción:

| Documento | Título Oficial | Tamaño | Temas Tratados | Enlace Directo |
|---|---|:---:|---|:---:|
| 🧱 `guia_databricks_free_edition.pdf` | **Guía Práctica: Databricks Community Edition y Calidad de Vinos** | 3.7 MB | Creación de cuenta Community, configuración de clústeres serverless, persistencia en Delta Lake, experiment tracking con MLflow, registro en Model Registry. | [📄 Abrir PDF](./Guias/guia_databricks_free_edition.pdf) |
| ☁️ `guia_databricks_aws.pdf` | **Guía Práctica: Databricks en AWS y Data Lakehouse S3** | 6.3 MB | Arquitectura AWS S3 por capas (raw/curated/models), roles y políticas IAM de seguridad, conexión Databricks-S3, orquestación serverless y monitoreo MLOps. | [📄 Abrir PDF](./Guias/guia_databricks_aws.pdf) |

> 💡 **Visor Web Integrado:** Ambas guías cuentan con visor PDF interactivo incorporado en la [Plataforma Web del Laboratorio Virtual](https://sazuniga06.github.io/Data-Science-Programming---USTA-Tunja-Repository/), permitiendo lectura en línea, zoom y descarga directa.

---

## 📚 Biblioteca Digital de Referencia (28 Libros con Portadas Oficiales)

Sección integrada en la plataforma web con **28 textos especializados de referencia internacional** orientados a proyectos de grado, computación en la nube, ingeniería de datos y MLOps. Todos los libros disponen de su respectiva portada oficial digitalizada, metadatos enriquecidos, visor integrado y descarga directa:

### ☁️ 1. Amazon Web Services (AWS) & Cloud Infrastructure (8 Libros)
1. **AWS Certified AI Practitioner Study Guide** — *Tom Taull*
2. **AWS Certified Cloud Practitioner All-in-One** — *Daniel Carter*
3. **AWS Certified Cloud Practitioner Practice Tests 2023** — *Neal Davis*
4. **AWS Certified Cloud Practitioner Study Guide 2nd Edition** — *Ben Piper*
5. **AWS Certified SysOps Administrator Associate Training Notes** — *Neal Davis*
6. **Agents on AWS: Beginner's Guide** — *Bunny Kaushik*
7. **Data Wrangling on AWS** — *Navnit Shukla, Sankar M. & Sam Palani*
8. **Implementing Cloud Design Patterns for AWS** — *Marcus Young*

### 🔷 2. Microsoft Azure & Cloud Data Science (4 Libros)
1. **Data Engineering with Azure** — *Dharmendra Pratap Singh*
2. **Data Engineering with Azure Databricks** — *Dmitry Foshin*
3. **Data Science Solutions on Azure** — *Julian Soh*
4. **Hands-On MLOps on Azure** — *Banibrata De*

### 🧱 3. Databricks, Delta Lake & Apache Spark (8 Libros)
1. **Data Engineering with Databricks** — *Sumit Verma*
2. **Databricks Certified Data Engineer Associate** — *Derar Alhussein*
3. **Databricks Certified Generative AI Engineer** — *Rajaniesh Kaushikk*
4. **Databricks Data Intelligence Platform 2nd Edition** — *Jason Yip*
5. **Databricks ML in Action** — *Packt Publishing*
6. **Practical Machine Learning on Databricks** — *Debu Sinha*
7. **Ultimate Data Engineering with Databricks** — *Mayank Malhotra*
8. **Advanced Data Engineering with Databricks** — *Databricks Technical Publications*
9. **Big Book of Data Engineering** — *Databricks Editorial*
10. **The Data Lakehouse for Dummies 2nd Edition** — *Databricks Special Edition*

### 🔄 4. MLOps, Producción y Patrones de Machine Learning (4 Libros)
1. **Implementing MLOps in the Enterprise** — *Yaron Haviv*
2. **Machine Learning Design Patterns** — *Valliappa Lakshmanan*
3. **Machine Learning Engineering with Python 2nd Edition** — *Andrew P. McMahon*
4. **Machine Learning Upgrade** — *Kristen Kehrer*

### 🧪 5. Diseño y Análisis de Experimentos Científicos (2 Libros)
1. **Design and Analysis of Experiments, Volume 2: Advanced Experimental Design** — *Klaus Hinkelmann & Oscar Kempthorne (Wiley-Interscience)*
2. **Experimental Design for Data Science** — *V. Roshan Joseph*

---

## 🌐 Acceso al Laboratorio Virtual en GitHub Pages

Todos los recursos de este espacio académico (cuadernos interactivos, guías PDF, visor de video clases y biblioteca digital) están disponibles a través del portal web oficial:

👉 **[https://sazuniga06.github.io/Data-Science-Programming---USTA-Tunja-Repository/](https://sazuniga06.github.io/Data-Science-Programming---USTA-Tunja-Repository/)**

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Trabajo de Grado 1</i>
  </p>
</div>
