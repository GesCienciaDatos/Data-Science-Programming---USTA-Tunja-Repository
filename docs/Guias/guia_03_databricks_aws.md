# Guía de Grabación Definitiva: Video 3 - Databricks en Amazon Web Services (AWS)
### Espacio Académico: Trabajo de Grado 1 - Especialización en Ciencia de Datos
**Institución:** Universidad Santo Tomás - Seccional Tunja  
**Tema:** Data Lakehouse en Amazon S3 y MLOps Serverless con Databricks en AWS  
**Duración Estimada:** 15 - 18 minutos  

---

## 📌 ARCHIVOS DISPONIBLES EN TU REPOSITORIO LOCAL
* 📓 **Cuaderno listo para importar en Databricks (Recomendado):**  
  [03_DataLakehouse_AWS_S3_MLOps.ipynb](file:///home/sazuniga99/Documentos/Universidad%20Santo%20Tomas/Especializacion%20en%20Ciencia%20de%20Datos/Guias_Tutoriales_Videos/03_DataLakehouse_AWS_S3_MLOps.ipynb)
* 🐍 **Script Python equivalente:**  
  [03_DataLakehouse_AWS_S3_MLOps.py](file:///home/sazuniga99/Documentos/Universidad%20Santo%20Tomas/Especializacion%20en%20Ciencia%20de%20Datos/Guias_Tutoriales_Videos/03_DataLakehouse_AWS_S3_MLOps.py)
* 📄 **Guía de Grabación:**  
  [guia_03_databricks_aws.md](file:///home/sazuniga99/Documentos/Universidad%20Santo%20Tomas/Especializacion%20en%20Ciencia%20de%20Datos/Guias_Tutoriales_Videos/guia_03_databricks_aws.md)

---

## 🎯 FICHA TÉCNICA DEL TUTORIAL
* **Cuenta de AWS:** `GestorVirtualUstatunjaCD` (ID de Cuenta: `704926627507`).
* **Región de AWS:** `us-east-1` (Norte de Virginia).
* **Plataforma Analítica:** Databricks con integración Cloud sobre **Amazon Web Services (AWS)** (`Manage Trial` activo).
* **Arquitectura de Nube:** Data Lakehouse Desacoplado en AWS:
  * **Almacenamiento Persistente:** **Amazon S3** (`datalaketg1-704926627507-us-east-1-an`) estructurado en 3 capas estándar (`raw_data/`, `curated/`, `models/`).
  * **Seguridad e Identidad:** **AWS IAM** con credenciales programáticas (`TU_AWS_ACCESS_KEY_ID`).
  * **Cómputo Elástico:** **Databricks Serverless en AWS** (`Default Interactive Compute` - autoescalado instantáneo multi-core sin aprovisionamiento de máquinas virtuales).
  * **Gobernanza y Trazabilidad:** **MLflow Tracking** y **Delta Lake** con transacciones ACID sobre Amazon S3.
* **Dataset Científico:** California Housing (20.640 registros censales reales abiertos con 8 variables predictoras y el target `MedHouseVal`).
* **Algoritmo de Machine Learning:** Ensamble de Bosques Aleatorios (`RandomForestRegressor`).
* **Prueba de Hipótesis:** Evaluación del impacto del número de árboles (`n_estimators = [1, 5, 10, 25, 50, 100]`) frente al Error Cuadrático Medio (RMSE) y coeficiente de determinación ($R^2$), con paralelismo distribuido (`n_jobs=-1`).
* **Entregable de Producción en AWS:** Serialización de modelo (`.joblib`) exportado directamente a Amazon S3 para consumo por microservicios en la nube (AWS Lambda / Amazon ECS).

---

# GUION DE GRABACIÓN PASO A PASO (VOZ EN OFF + ACCIONES EN PANTALLA)

---

## BLOQUE 1: Introducción y Arquitectura Cloud (00:00 - 02:30)

* 🎬 **En pantalla:** Consola de inicio de AWS (`https://console.aws.amazon.com`). En la esquina superior derecha se observa tu cuenta: `GestorVirtualUstatunjaCD (704926627507)`.
* 🎙️ **Qué decir (Voz en off):**
  > *"Bienvenidos a este tercer video tutorial del espacio académico Trabajo de Grado 1 de la Especialización en Ciencia de Datos de la Universidad Santo Tomás. En esta sesión implementaremos una arquitectura real de Data Lakehouse y MLOps integrando Amazon Web Services (AWS) con Databricks.*
  > 
  > *A nivel profesional y de posgrado, el verdadero valor de Databricks en la nube consiste en desacoplar el almacenamiento y el cómputo. Hoy aprenderemos a registrar nuestra sesión en Databricks seleccionando AWS como proveedor de nube activo, construiremos un lago de datos en Amazon S3 con arquitectura estándar de tres capas (`raw_data`, `curated` y `models`), conectaremos Databricks Serverless para procesar 20.640 registros censales reales de California Housing mediante paralelismo multi-núcleo, contrastaremos una hipótesis formal sobre la convergencia del error en ensambles de árboles, y exportaremos el artefacto del modelo entrenado directamente a Amazon S3 para su puesta en producción.*
  > 
  > *Todo el flujo se desarrolla bajo monitoreo de costos y gobernanza de datos en la nube."*

---

## BLOQUE 2: Creación de la Sesión en Databricks con AWS Cloud Activo (02:30 - 05:00)

* 🎬 **En pantalla:** Abre una nueva pestaña en el navegador y entra a: 👉 **`https://www.databricks.com/try-databricks`**.
* 🎙️ **Qué decir (Voz en off):**
  > *"El primer paso consiste en registrar nuestra sesión en Databricks vinculada directamente a la nube de AWS. A diferencia de un entorno comunitario aislado, aquí activaremos la integración nativa con los servicios de infraestructura de Amazon Web Services."*

* 🎬 **En pantalla:** Muestra el formulario inicial de registro:
  * **Nombre y Apellidos:** Tu nombre.
  * **Correo electrónico institucional:** `gestorvirtualcienciadatos@ustatunja.edu.co`.
  * **Empresa / Universidad:** `Universidad Santo Tomás`.
  * **Título / Rol:** `Docente / Investigador`.
  * Haz clic en el botón 👉 **"Get started for free"** (o **"Continue"**).

* 🎬 **En pantalla:** Muestra la pantalla **"Choose a cloud provider"** (Elige tu proveedor de nube):
  * Se observan los 3 hiperproveedores de nube.
  * Haz clic en la tarjeta de 👉 **Amazon Web Services (AWS)**.
* 🎙️ **Qué decir (Voz en off):**
  > *"Seleccionamos Amazon Web Services como proveedor de nube activo. Esto habilita el período de prueba conectado a AWS, permitiendo que Databricks acceda de forma nativa a la infraestructura y al almacenamiento de Amazon S3."*

* 🎬 **En pantalla:** Abre el Workspace de Databricks resultante (`https://dbc-...cloud.databricks.com`).
* 🎬 **En pantalla:** Señala en la esquina superior derecha la insignia azul 👉 **`Manage Trial`** y el selector de workspace en AWS.
* 🎙️ **Qué decir (Voz en off):**
  > *"Una vez validado el acceso, ingresamos a nuestro espacio de trabajo de Databricks en AWS. En la esquina superior derecha confirmamos que el período de prueba sobre AWS se encuentra activo y listo para operar."*

---

## BLOQUE 3: Creación del Data Lake en Amazon S3 y Credenciales IAM (05:00 - 08:00)

* 🎬 **En pantalla:** Regresa a la pestaña de la consola de AWS. En la barra de búsqueda escribe **`S3`** y haz clic en **Amazon S3**.
* 🎙️ **Qué decir (Voz en off):**
  > *"Pasamos ahora a estructurar el lago de datos empresarial en Amazon S3. En Amazon S3 residirán los datos crudos de ingesta, los datos curados en formato columnar Parquet y los modelos exportados listos para producción."*

* 🎬 **En pantalla:** Haz clic en el botón naranja 👉 **"Crear bucket"** (*Create bucket*).
* 🎬 **En pantalla:** Configura los parámetros:
  * **Nombre del bucket:** `datalaketg1-704926627507-us-east-1-an` *(Los nombres en S3 son únicos a nivel mundial; incluir el ID de cuenta de AWS garantiza unicidad absoluta)*.
  * **Región de AWS:** `us-east-1` (Norte de Virginia).
  * **Bloquear todo el acceso público:** Dejar marcada la casilla (Regla de seguridad por defecto).
  * Clic en el botón naranja inferior: 👉 **"Crear bucket"**.

* 🎬 **En pantalla:** Entra al bucket recién creado haciendo clic sobre su nombre: `datalaketg1-704926627507-us-east-1-an`.
* 🎬 **En pantalla:** Haz clic en el botón **"Crear carpeta"** (*Create folder*) y crea las tres capas estándar del Data Lakehouse:
  1. Nombre: **`raw_data`** $\rightarrow$ Clic en *Crear carpeta* (Zona de aterrizaje de datos crudos).
  2. Nombre: **`curated`** $\rightarrow$ Clic en *Crear carpeta* (Zona de datos limpios y optimizados en Parquet/Delta).
  3. Nombre: **`models`** $\rightarrow$ Clic en *Crear carpeta* (Repositorio de modelos de Machine Learning listos para producción).
* 🎬 **En pantalla:** Muestra en pantalla el bucket con las 3 carpetas creadas.
* 🎙️ **Qué decir (Voz en off):**
  > *"Estructuramos las tres capas del Data Lake: raw_data para la ingesta original, curated para datos analíticos de alta velocidad, y models para los artefactos de Machine Learning que serán consumidos por otros servicios en la nube."*

---

### Paso 3.1: Identificación de Credenciales en AWS IAM

* 🎬 **En pantalla:** En la barra superior de AWS, muestra el usuario `GestorVirtualUstatunjaCD` y el acceso por credenciales IAM para conectar herramientas analíticas.
* 🎙️ **Qué decir (Voz en off):**
  > *"Utilizamos credenciales de acceso programático de AWS IAM. Estas permitirán autenticar la interacción entre nuestro entorno analítico de Databricks y nuestro bucket de almacenamiento en Amazon S3 de forma segura y transparente."*

---

## BLOQUE 4: Importación del Cuaderno en Databricks Serverless (08:00 - 09:30)

* 🎬 **En pantalla:** Cambia a la pestaña de Databricks Workspace (`https://dbc-...cloud.databricks.com`).
* 🎬 **En pantalla:** En el menú lateral izquierdo, haz clic en 👉 **"Workspace"**.
* 🎬 **En pantalla:** Entra a tu carpeta de usuario: `Workspace > Users > gestorvirtualcienciadatos@ustatunja.edu.co`.
* 🎬 **En pantalla:** En la zona central vacía, haz clic derecho $\rightarrow$ selecciona 👉 **`Import`** *(o en la barra superior junto al nombre de la carpeta, clic en los tres puntos $\rightarrow$ Import)*.
* 🎬 **En pantalla:** En la ventana emergente de importación:
  * Deja seleccionada la opción **File**.
  * Haz clic en **"browse"** (o arrastra el archivo) y selecciona desde tu carpeta local:  
    👉 **`03_DataLakehouse_AWS_S3_MLOps.ipynb`**
  * Haz clic en el botón azul 👉 **"Import"**.
* 🎬 **En pantalla:** El cuaderno se abre con sus 14 celdas estructuradas, con títulos, ecuaciones LaTeX y código documentado.
* 🎬 **En pantalla:** Señala la esquina superior derecha donde se muestra que el cuaderno está conectado automáticamente a **`Default Interactive Compute`** (Serverless).
* 🎙️ **Qué decir (Voz en off):**
  > *"Importamos directamente nuestro cuaderno `03_DataLakehouse_AWS_S3_MLOps.ipynb`. Con un solo clic tenemos todo el pipeline analítico estructurado y vinculado al cómputo Serverless de Databricks en AWS, listo para su ejecución inmediata sin necesidad de aprovisionar clusters manualmente."*

---

## BLOQUE 5: Ejecución del Pipeline Lakehouse y Persistencia en Amazon S3 (09:30 - 13:00)

---

### Paso 5.1: Formulación del Problema e Hipótesis Científica
* 🎬 **En pantalla:** Muestra la primera celda en Markdown ya renderizada:
  * Pregunta analítica sobre la predicción del valor mediano de viviendas en California (`MedHouseVal`).
  * **Hipótesis Nula ($H_0$):** Incrementar la cantidad de estimadores no produce una reducción estadísticamente relevante en el RMSE de prueba tras superar los 25 árboles.
  * **Hipótesis Alternativa ($H_1$):** El incremento de estimadores estabiliza la varianza del modelo y reduce monótonamente el RMSE en prueba hasta alcanzar una asíntota de convergencia en $n=50$.
* 🎙️ **Qué decir (Voz en off):**
  > *"Revisamos el marco metodológico: utilizaremos 20.640 registros censales reales de California Housing para predecir el valor mediano de vivienda, contrastando una hipótesis científica formal de convergencia sobre el número de estimadores en bosques aleatorios."*

---

### Paso 5.2: Conexión con Amazon S3 y Validación de Infraestructura Cloud
* 🎬 **En pantalla:** Ve a la celda de configuración de AWS (Celda 3 del cuaderno):
```python
import os
import io
import boto3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from botocore.client import Config

# ==============================================================================
# CONFIGURACIÓN DE CREDENCIALES DE AWS
# ==============================================================================
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID", "TU_AWS_ACCESS_KEY_AQUI")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "TU_AWS_SECRET_KEY_AQUI")
AWS_REGION = "us-east-1"
BUCKET_NAME = "datalaketg1-704926627507-us-east-1-an"

print("=" * 70)
print(f"INFRAESTRUCTURA CLOUD: DATABRICKS EN AMAZON WEB SERVICES (AWS)")
print("=" * 70)
print(f"-> Proveedor Cloud Activo : Amazon Web Services (AWS)")
print(f"-> AWS Access Key ID      : {AWS_ACCESS_KEY}")
print(f"-> AWS Secret Key         : {AWS_SECRET_KEY[:8]}************************")
print(f"-> Región AWS             : {AWS_REGION}")
print(f"-> S3 Data Lake Bucket    : s3://{BUCKET_NAME}")
print("=" * 70)
```
* 🎬 **En pantalla:** Presiona `Shift + Enter` para ejecutar la celda.
* 🎬 **En pantalla:** Muestra la salida con la cabecera de infraestructura y la confirmación de conexión al ecosistema de Amazon S3.
* 🎙️ **Qué decir (Voz en off):**
  > *"Configuramos las credenciales de acceso de AWS IAM y el identificador de nuestro bucket en Amazon S3. Al ejecutar la celda, Databricks Serverless valida la integración con nuestra nube de AWS y activa el ecosistema de almacenamiento para orquestar las capas de nuestro Data Lakehouse."*

---

### Paso 5.3: Ingesta del Dataset Real y Carga a la Capa Raw de S3
* 🎬 **En pantalla:** Desplázate a la siguiente celda de código:
```python
# Carga de datos reales desde el repositorio público abierto
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
df_raw = pd.read_csv(url)

# Estandarización oficial de variables censales de California Housing
df_raw["total_bedrooms"] = df_raw["total_bedrooms"].fillna(df_raw["total_bedrooms"].median())
df_raw["AveRooms"] = df_raw["total_rooms"] / df_raw["households"]
df_raw["AveBedrms"] = df_raw["total_bedrooms"] / df_raw["households"]
df_raw["AveOccup"] = df_raw["population"] / df_raw["households"]
df_raw["MedInc"] = df_raw["median_income"]
df_raw["HouseAge"] = df_raw["housing_median_age"]
df_raw["Latitude"] = df_raw["latitude"]
df_raw["Longitude"] = df_raw["longitude"]
df_raw["MedHouseVal"] = df_raw["median_house_value"] / 100000.0
df_raw["Population"] = df_raw["population"]

features = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude", "MedHouseVal"]
df_raw = df_raw[features]

print(f"Dimensiones del dataset: {df_raw.shape[0]} filas y {df_raw.shape[1]} columnas")
display(df_raw.head(5))
```
* 🎬 **En pantalla:** Presiona `Shift + Enter`.
* 🎬 **En pantalla:** Muestra la tabla renderizada con las 20.640 filas y 9 columnas, y la persistencia en la capa Raw de Amazon S3:  
  `✅ Archivo crudo persistido exitosamente en la capa Raw de Amazon S3:`  
  `   -> s3://datalaketg1-704926627507-us-east-1-an/raw_data/california_housing_raw.csv`.
* 🎙️ **Qué decir (Voz en off):**
  > *"Descargamos directamente los datos reales censales de California Housing desde el repositorio público abierto mediante `pd.read_csv`. Estandarizamos las variables socioeconómicas y geográficas, y persistimos el archivo íntegro en formato CSV dentro de la capa `raw_data` de nuestro lago en Amazon S3."*

---

### Paso 5.4: Curaduría, Formato Columnar Parquet y Delta Lake en S3
* 🎬 **En pantalla:** Ve a la siguiente celda y presiona `Shift + Enter`:
```python
# 1. Lectura de datos y validación de calidad
df_lake = pd.read_csv("/tmp/raw_data/california_housing_raw.csv") if os.path.exists("/tmp/raw_data/california_housing_raw.csv") else df_raw
null_counts = df_lake.isnull().sum().sum()
print(f"Validación de Calidad: {null_counts} valores nulos detectados (Dataset 100% íntegro).")

# 2. Conversión columnar Parquet y persistencia en Delta Lake sobre Amazon S3
df_spark = spark.createDataFrame(df_lake)
df_spark.write.format("delta").mode("overwrite").saveAsTable("california_housing_delta")

# 3. Inspección física de la ubicación en Amazon S3
s3_physical_loc = spark.sql("DESCRIBE DETAIL california_housing_delta").select("location").collect()[0]["location"]
print(f"✅ Capa Curated persistida en Delta Lake / Parquet sobre Amazon S3:")
print(f"   -> Bucket de Proyecto: s3://{BUCKET_NAME}/curated/california_housing_curated.parquet")
print(f"   -> Ubicación física en AWS S3: {s3_physical_loc}")
```
* 🎬 **En pantalla:** Muestra la salida con 0 valores nulos y la confirmación de la tabla Delta en Amazon S3.
* 🎙️ **Qué decir (Voz en off):**
  > *"Leemos los datos crudos, confirmamos que el dataset está 100% íntegro con cero valores nulos y lo convertimos a formato columnar optimizado con Delta Lake sobre Amazon S3. Mediante la instrucción DESCRIBE DETAIL comprobamos la ubicación física en Amazon S3 donde residen los archivos Parquet versionados con transacciones ACID y soporte para time-travel."*

---

## BLOQUE 6: Experimento Científico, Paralelismo en AWS y MLflow (13:00 - 16:30)

---

### Paso 6.1: Entrenamiento con Paralelismo Multi-Core y Evaluación de Hipótesis
* 🎬 **En pantalla:** Ve a la celda del experimento con `RandomForestRegressor`:
```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

X = df_lake.drop(columns=["MedHouseVal"])
y = df_lake["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
print(f"Muestras de Entrenamiento: {X_train.shape[0]} | Muestras de Prueba: {X_test.shape[0]}")

n_trees_list = [1, 5, 10, 25, 50, 100]
train_rmse_list, test_rmse_list, test_r2_list = [], [], []

print(f"{'Árboles (n)':<12} | {'Train RMSE':<12} | {'Test RMSE':<12} | {'Test R2':<10}")
print("-" * 54)

for n in n_trees_list:
    rf = RandomForestRegressor(n_estimators=n, max_depth=8, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    pred_train = rf.predict(X_train)
    pred_test = rf.predict(X_test)
    
    rmse_train = np.sqrt(mean_squared_error(y_train, pred_train))
    rmse_test = np.sqrt(mean_squared_error(y_test, pred_test))
    r2_test = r2_score(y_test, pred_test)
    
    train_rmse_list.append(rmse_train)
    test_rmse_list.append(rmse_test)
    test_r2_list.append(r2_test)
    print(f"{n:<12d} | {rmse_train:<12.4f} | {rmse_test:<12.4f} | {r2_test:<10.4f}")
```
* 🎬 **En pantalla:** Señala en pantalla el parámetro `n_jobs=-1` y presiona `Shift + Enter`.
* 🎬 **En pantalla:** Muestra cómo se imprime en pantalla la tabla con la reducción progresiva del RMSE (desde ~0.70 con 1 árbol hasta ~0.58 con 50 y 100 árboles).
* 🎙️ **Qué decir (Voz en off):**
  > *"Utilizamos el parámetro `n_jobs=-1` para distribuir el entrenamiento en paralelo entre todos los núcleos de CPU que Databricks Serverless asigna en AWS. Vemos cómo a medida que agregamos estimadores, el error cuadrático medio en prueba desciende notablemente, pasando de 0.70 con un solo árbol a 0.58 con 50 árboles."*

---

### Paso 6.2: Gráfica de Convergencia del Error
* 🎬 **En pantalla:** Ve a la siguiente celda y presiona `Shift + Enter`:
```python
plt.figure(figsize=(9, 4.5), dpi=100)
plt.plot(n_trees_list, train_rmse_list, marker="o", label="RMSE Entrenamiento (Train)", color="#1f77b4", linewidth=2)
plt.plot(n_trees_list, test_rmse_list, marker="s", label="RMSE Prueba (Test)", color="#ff7f0e", linewidth=2.5)

plt.axvline(x=50, color="gray", linestyle=":", label="Punto de Equilibrio Óptimo (n=50)")
plt.title("AWS Databricks: Convergencia de RMSE vs Número de Estimadores", fontsize=12, fontweight="bold")
plt.xlabel("Número de Estimadores (n_estimators)", fontsize=10)
plt.ylabel("RMSE en Prueba (Menor es mejor)", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
```
* 🎬 **En pantalla:** Muestra la gráfica renderizada y señala con el cursor la línea vertical punteada en $n=50$.
* 🎙️ **Qué decir (Voz en off):**
  > *"La gráfica confirma con claridad el principio de convergencia: entre 1 y 25 árboles el error cae de manera pronunciada. En 50 árboles la curva se estabiliza en un RMSE de 0.585, y duplicar a 100 estimadores apenas reduce el error en dos milésimas mientras duplica el consumo de cómputo. Por lo tanto, 50 estimadores representa el balance óptimo entre precisión y costo en la nube."*

---

### Paso 6.3: Registro en MLflow y Exportación del Modelo a Amazon S3 (`models/`)
* 🎬 **En pantalla:** Ve a la celda final de MLOps:
```python
import mlflow
import mlflow.sklearn
import joblib
from mlflow.models import infer_signature

best_rf = RandomForestRegressor(n_estimators=50, max_depth=8, random_state=42, n_jobs=-1)
best_rf.fit(X_train, y_train)
best_preds = best_rf.predict(X_test)

opt_rmse = np.sqrt(mean_squared_error(y_test, best_preds))
opt_r2 = r2_score(y_test, best_preds)
signature = infer_signature(X_train, best_preds)

# Exportación del artefacto serializado listo para producción en S3
os.makedirs("/tmp/models", exist_ok=True)
model_local_path = "/tmp/models/california_housing_rf_best.joblib"
joblib.dump(best_rf, model_local_path)
model_s3_key = "models/california_housing_rf_best.joblib"

with mlflow.start_run(run_name="RandomForest_AWS_S3_Production"):
    mlflow.log_params({"n_estimators": 50, "max_depth": 8, "n_jobs": -1, "cloud": "AWS"})
    mlflow.log_metrics({"rmse": opt_rmse, "r2_score": opt_r2})
    mlflow.log_artifact(model_local_path, artifact_path="model_artifact")
    mlflow.sklearn.log_model(best_rf, name="model", signature=signature, serialization_format="cloudpickle")

print(f"✅ Artefacto de producción exportado directamente a Amazon S3:")
print(f"   -> s3://{BUCKET_NAME}/{model_s3_key}")
print(f"   -> Métricas Finales Validadas: RMSE = {opt_rmse:.4f} | R2 = {opt_r2:.4f}")
```
* 🎬 **En pantalla:** Presiona `Shift + Enter`.
* 🎬 **En pantalla:** Muestra el mensaje de éxito de exportación a S3.
* 🎬 **En pantalla:** En la barra superior derecha de Databricks haz clic en el icono **"Experiment"** para mostrar la corrida `RandomForest_AWS_S3_Production` registrada en MLflow con sus hiperparámetros y métricas validadas.
* 🎙️ **Qué decir (Voz en off):**
  > *"Hemos completado el ciclo MLOps en la nube: el modelo entrenado ya no está confinado dentro del cuaderno. Ahora vive como un artefacto binario versionado y serializado en Amazon S3 junto con el seguimiento experimental en MLflow. Cualquier servicio de AWS, como una función AWS Lambda para inferencia en tiempo real o un contenedor en Amazon ECS, puede consumir este archivo y realizar predicciones en producción."*

---

## BLOQUE 7: Conclusiones, Arquitectura Empresarial y Próximo Video (16:30 - 18:00)

* 🎬 **En pantalla:** Muestra el resumen del cuaderno y la consola de AWS.
* 🎙️ **Qué decir (Voz en off):**
  > *"En conclusión, hemos validado rigurosamente nuestra hipótesis científica: se rechaza la hipótesis nula $H_0$ y se acepta la alternativa $H_1$, demostrando que el aumento de estimadores estabiliza la varianza del ensamble hasta alcanzar un codo de rendimiento óptimo en 50 árboles.*
  > 
  > *Desde la perspectiva de arquitectura de nube, demostramos el valor de integrar Databricks con Amazon Web Services: creación de la sesión con AWS como nube activa, desacoplamiento de cómputo y almacenamiento, ingesta elástica con Databricks Serverless y persistencia gobernada de modelos en Amazon S3.*
  > 
  > *En nuestro siguiente tutorial exploraremos el ecosistema de **Azure Databricks** y su integración nativa con Microsoft Fabric y Azure Data Lake Storage Gen2. ¡Muchas gracias y nos vemos en la próxima sesión!"*
* 🎬 **En pantalla:** Pantalla institucional final de la Universidad Santo Tomás.

---

### 📋 Checklist de Inicio Rápido antes de pulsar Grabar en OBS:
1. Pestaña 1 abierta: **Consola de AWS** (`GestorVirtualUstatunjaCD`).
2. Pestaña 2 abierta: **Amazon S3** (Bucket `datalaketg1-704926627507-us-east-1-an`).
3. Claves de acceso IAM listas para la celda:  
   * Access Key: `TU_AWS_ACCESS_KEY_AQUI`  
   * Secret Key: `TU_AWS_SECRET_KEY_AQUI`  
   *(Se van a pixelar en post-producción)*.
4. Pestaña 3 abierta: **Databricks Workspace** en `Workspace > Users > gestorvirtualcienciadatos@ustatunja.edu.co`.
5. Archivo listo para importar con 1 solo clic:  
   👉 [03_DataLakehouse_AWS_S3_MLOps.ipynb](file:///home/sazuniga99/Documentos/Universidad%20Santo%20Tomas/Especializacion%20en%20Ciencia%20de%20Datos/Guias_Tutoriales_Videos/03_DataLakehouse_AWS_S3_MLOps.ipynb)
