# Big Data y Procesamiento Distribuido 🌐

> **Especialización en Ciencia de Datos**
> **Universidad Santo Tomás — Seccional Tunja**
> **Nivel Académico:** Semestre II
> **Docente / Gestor Virtual:** Santiago A. Zúñiga M.
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Big%20Data-f59e0b?style=for-the-badge&logo=apachespark&logoColor=white" alt="Big Data"/>
  <img src="https://img.shields.io/badge/Topics-Distribuido%20%7C%20DW%20%7C%20Lake%20%7C%20Gobernanza-0ea5e9?style=for-the-badge" alt="Temas"/>
  <img src="https://img.shields.io/badge/Course-Big%20Data-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

---

## 📌 Descripción de la Asignatura

Fundamentos y práctica del Big Data: las V (volumen, variedad, velocidad), su importancia actual, los tipos de datos (estructurados, semiestructurados y no estructurados) y el ciclo de vida de los datos; el procesamiento y almacenamiento distribuido (Hadoop, Spark, SQL y NoSQL, MapReduce y sus limitaciones, HDFS, Spark y HBase); el *Data Warehousing* y el *Data Lake* (esquema estrella, ETL, OLAP, Hive y Pig, y su comparación); la analítica y visualización a escala (ML, DL y NLP, Tableau, Power BI y D3, *storytelling*); la seguridad y gobernanza de los datos (amenazas, encriptación, control de acceso, auditoría, propiedad y transparencia); y los avances y tendencias emergentes (*stream* y *graph processing*, analíticas con IA, aprendizaje federado y blockchain).

Cada módulo sigue la misma filosofía: **conceptos implementados desde cero en Python** (MapReduce, HDFS y HBase simulados, esquema estrella, ventanas de *streaming*, PageRank, Pregel, cadena de bloques), **PySpark real** donde corresponde y **resultados honestos** (por ejemplo, con datos que caben en memoria, Spark local no le gana a DuckDB ni a pandas), con secciones «🛠️ Práctica» y solución desplegable.

---

## 📚 Estructura Curricular Oficial de la Asignatura

El curso sigue el índice del libro de la asignatura en dos capítulos y se desarrolla en **6 módulos** (00 a 05), cada uno con su ruta estándar, su ruta **Para Dummies** y un taller práctico evaluativo:

| # | Módulo | Secciones del libro | Temas Principales | Ruta Estándar | Ruta Para Dummies | Taller Práctico |
|:---:|:---|:---:|:---|:---:|:---:|:---:|
| **00** | **Fundamentos de Big Data** | 1.1 – 1.3 | Las V, importancia en el mundo actual, tipos de datos, ciclo de vida de los datos | [Ver Cuadernos](00%20-%20Fundamentos%20de%20Big%20Data/) | [Para Dummies](00%20-%20Fundamentos%20de%20Big%20Data/Para%20Dummies/) | [Hands-On](homeworks/00_Fundamentos_Big_Data_Hands_On.ipynb) |
| **01** | **Procesamiento y Almacenamiento Distribuido** | 1.4 | Hadoop, Spark, SQL y NoSQL, MapReduce desde cero y sus limitaciones, HDFS, Spark y HBase | [Ver Cuadernos](01%20-%20Procesamiento%20y%20Almacenamiento%20Distribuido/) | [Para Dummies](01%20-%20Procesamiento%20y%20Almacenamiento%20Distribuido/Para%20Dummies/) | [Hands-On](homeworks/01_Procesamiento_Almacenamiento_Hands_On.ipynb) |
| **02** | **Data Warehousing y Data Lake** | 1.5 | Esquema estrella, ETL y OLAP, Data Lake con Parquet particionado, Hive y Pig, comparación DW vs Lake — cierra el Capítulo 1 | [Ver Cuadernos](02%20-%20Data%20Warehousing%20y%20Data%20Lake/) | [Para Dummies](02%20-%20Data%20Warehousing%20y%20Data%20Lake/Para%20Dummies/) | [Hands-On](homeworks/02_Data_Warehouse_Data_Lake_Hands_On.ipynb) |
| **03** | **Analítica y Visualización en Big Data** | 2.1 – 2.3 | Algoritmos aproximados, ML/DL/NLP a escala, Tableau, Power BI y D3, *storytelling* con datos | [Ver Cuadernos](03%20-%20Analitica%20y%20Visualizacion%20en%20Big%20Data/) | [Para Dummies](03%20-%20Analitica%20y%20Visualizacion%20en%20Big%20Data/Para%20Dummies/) | [Hands-On](homeworks/03_Analitica_Visualizacion_Hands_On.ipynb) |
| **04** | **Seguridad y Gobernanza de Big Data** | 2.4 | Brechas, accesos no autorizados y *data leakage*, encriptación, control de acceso y auditoría, propiedad, responsabilidad y transparencia | [Ver Cuadernos](04%20-%20Seguridad%20y%20Gobernanza%20de%20Big%20Data/) | [Para Dummies](04%20-%20Seguridad%20y%20Gobernanza%20de%20Big%20Data/Para%20Dummies/) | [Hands-On](homeworks/04_Seguridad_Gobernanza_Hands_On.ipynb) |
| **05** | **Avances y Tendencias en Big Data** | 2.5 | *Stream processing* y *graph processing*, analíticas con IA, aprendizaje federado, blockchain; incluye Glosario y Referencias Bibliográficas | [Ver Cuadernos](05%20-%20Avances%20y%20Tendencias%20en%20Big%20Data/) | [Para Dummies](05%20-%20Avances%20y%20Tendencias%20en%20Big%20Data/Para%20Dummies/) | [Hands-On](homeworks/05_Streaming_Grafos_Tendencias_Hands_On.ipynb) |

---

## 📝 Talleres Prácticos Evaluativos (Hands-On)

Los talleres de los 6 módulos, con su versión guiada **Para Dummies**, están centralizados en [`homeworks/`](homeworks/). A diferencia de los cuadernos de clase, **no incluyen soluciones**: traen retos con autoverificación (`assert`), rúbrica de evaluación y checklist de entrega. Consulta [`homeworks/README.md`](homeworks/README.md) para el mapa completo.

---

## 💡 Edición «Para Dummies» y Prácticas

- **Para Dummies:** cada cuaderno estándar tiene su espejo en la subcarpeta `Para Dummies/` de su módulo, con analogías cotidianas, sin jerga ni fórmulas y sin requerir Spark ni Java.
- **Prácticas:** los cuadernos incluyen secciones «🛠️ Práctica» (enunciado, celda `# Escribe tu código aquí` y solución guiada desplegable), con el formato del curso *Data Science programming*.

---

## 🛠️ Tecnologías y Librerías Utilizadas

* **Python 3.10+** (Entorno base de ejecución)
* **NumPy, Pandas, SciPy, Scikit-Learn, Matplotlib** (Cálculo, datos, modelos y visualización)
* **DuckDB, SQLite, PyArrow/Parquet** (Almacenes analíticos y formatos columnares)
* **NetworkX** (Grafos)
* **PySpark 4.x en modo local** (módulos 01, 02, 03 y 05; requiere JDK 17 o superior; los cuadernos avisan si no está instalado)
* **`cryptography`** (solo el módulo 04)
* En Google Colab, instala PySpark con `!pip install -q pyspark` donde el cuaderno lo indique.

---

## 🎬 Masterclasses y Videos Tutoriales en YouTube

* ⚡ **Instalación y Configuración de WSL2 y Docker**: [Ver en YouTube](https://youtu.be/nPWZi9Plljo)
  > Guía técnica paso a paso para la habilitación del subsistema Linux (WSL2), despliegue de contenedores Docker y configuración del entorno de virtualización para herramientas de Big Data y computación distribuida.

* 📊 **Instalación y Configuración de Power BI**: [Ver en YouTube](https://youtu.be/8RifWTEWBOI)
  > Guía técnica paso a paso para la instalación y configuración de Microsoft Power BI Desktop para la analítica visual, creación de cuadros de mando y dashboards en Big Data.

---

## 📖 Bibliografía de Apoyo

Las lecturas complementarias del Capítulo 1 están al final del [README del módulo 02](02%20-%20Data%20Warehousing%20y%20Data%20Lake/README.md). Las del Capítulo 2, el **Glosario** del curso y las **Referencias Bibliográficas** consolidadas están en el [README del módulo 05](05%20-%20Avances%20y%20Tendencias%20en%20Big%20Data/README.md).

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Plataforma de Laboratorios Virtuales</i>
  </p>
</div>
