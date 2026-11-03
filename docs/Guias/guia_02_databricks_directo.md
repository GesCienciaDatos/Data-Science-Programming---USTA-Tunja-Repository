# Guía de Grabación Definitiva: Video 2 - Databricks Directo (Serverless MLOps)
### Espacio Académico: Trabajo de Grado 1 - Especialización en Ciencia de Datos
**Institución:** Universidad Santo Tomás - Seccional Tunja  
**Duración Estimada:** 12 - 15 minutos  
**Objetivo del Video:** Demostrar el flujo corporativo de Machine Learning en Databricks: desde la exploración de la plataforma Serverless y almacenamiento en Delta Lake, hasta el rastreo con MLflow, registro en Model Registry y despliegue como microservicio REST en tiempo real con Model Serving.

---

## ⚠️ SOLUCIÓN INMEDIATA AL ERROR DE MLFLOW (RestException)

Si obtuviste el error:
```text
RestException: NOT_FOUND: Parent directory does not exist: /Users/dbc-d425c61c-1edb.cloud.databricks.com
```

### ¿Por qué ocurrió?
La instrucción `spark.conf.get("spark.databricks.workspaceUrl")` devuelve el dominio web del workspace (`dbc-...`), pero la estructura de carpetas de Databricks no tiene una carpeta con ese nombre bajo `/Users/`. 

### La Solución:
En Databricks, **NO es necesario indicar la ruta con `set_experiment`**: Databricks vincula automáticamente todas las ejecuciones al **Experimento nativo del Cuaderno (Notebook Experiment)**. Si deseas nombrarlo globalmente, se utiliza la ruta compartida universal `/Shared/`.

En la **Celda 2 (MLflow Tracking)**, simplemente usa el código corregido que se detalla en el **Paso 3** de este guion.

---

# GUION DE GRABACIÓN PASO A PASO (VOZ EN OFF + ACCIONES EN PANTALLA)

---

## BLOQUE 1: Introducción y Presentación de la Plataforma Databricks (00:00 - 03:00)

* 🎬 **En pantalla:** Muestra la pantalla principal de Databricks (**Welcome to Databricks**). Pasa el cursor suavemente sobre las tarjetas de bienvenida y el panel central *"Your resources"*.
* 🎙️ **Qué decir (Voz en off):**
  > *"Bienvenidos a este segundo video tutorial del espacio de Trabajo de Grado 1 de la Especialización en Ciencia de Datos de la Universidad Santo Tomás. En esta sesión abordaremos la plataforma empresarial Databricks.*
  > 
  > *A diferencia de un entorno local o un cuaderno interactivo convencional, Databricks integra en un único lago de datos (Lakehouse) todas las capacidades para ingeniería de datos, analítica SQL y, especialmente, operaciones de Machine Learning (MLOps). En este video no solo entrenaremos un modelo, sino que recorreremos el ciclo completo: persistencia en Delta Lake, rastreo de experimentos con MLflow, gobernanza en Model Registry y despliegue de una API REST de inferencia en tiempo real con Model Serving."*

---

### Recorrido por la Interfaz de Databricks (Matching Exacto con tu Plataforma)

* 🎬 **En pantalla:** Haz clic en el botón **"Create v"** dentro de la tarjeta *"Your resources"* (o en el botón superior si aplica) para desplegar el menú de creación rápida.
* 🎙️ **Qué decir (Voz en off):**
  > *"Desde la pantalla de inicio, en la sección 'Your resources', contamos con el acceso directo 'Create', que nos permite generar de inmediato los principales artefactos del sistema: desde la carga de datos (`Add or upload data`) y cuadernos (`Notebook`), hasta consultas analíticas (`Query`), tableros (`Dashboard`), experimentos de MLflow (`Experiment`) y modelos (`Model`)."*

* 🎬 **En pantalla:** Dirige la atención y el cursor a la **barra de navegación izquierda** de Databricks, recorriendo de arriba a abajo las secciones principales:
  1. **Sección Superior (Core):**
     * Señala `Workspace`: *"Aquí gestionamos la estructura jerárquica de directorios, cuadernos y repositorios colaborativos de nuestro equipo."*
     * Señala `Catalog`: *"Representa la capa de Unity Catalog, el corazón de la gobernanza de datos donde residen nuestros esquemas, metadatos y tablas Delta Lake."*
     * Haz clic en 👉 `Compute`: Muestra la pantalla **Compute - Serverless**.
* 🎙️ **Qué decir (Voz en off):**
  > *"Un aspecto fundamental en la arquitectura actual de Databricks es el cómputo sin servidor (Serverless Compute). Como podemos observar en la sección Compute, contamos con 'Default Interactive Compute' y 'Default Automated Compute' preconfigurados por el sistema. Esto elimina por completo la necesidad de aprovisionar y esperar el encendido de clústeres basados en máquinas virtuales tradicionales: los recursos se escalan de manera instantánea, transparente y optimizada en costos para la ejecución de nuestras cargas analíticas."*

* 🎬 **En pantalla:** Regresa el cursor al menú lateral izquierdo y muestra las secciones especializadas:
  2. **Sección SQL:**
     * Señala `SQL Editor`, `Dashboards` y `SQL Warehouses`: *"Dedicada a la inteligencia de negocios, analistas de datos y visualización con almacenes SQL optimizados."*
  3. **Sección Data Engineering:**
     * Señala `Runs`, `Data Ingestion` y `Visual Data Prep`: *"Destinada a la orquestación y canalización de ingesta masiva de datos (ETL/ELT)."*
  4. **Sección AI/ML (Nuestro foco en este tutorial):**
     * Señala con énfasis:
       * `Experiments`: *"El servidor integrado de MLflow Tracking para registrar parámetros, métricas y artefactos de cada entrenamiento."*
       * `Models`: *"El Model Registry centralizado donde versionamos y promovemos los modelos a producción."*
       * `Serving`: *"El motor de Model Serving para exponer nuestros modelos como microservicios y endpoints REST de baja latencia."*

---

## BLOQUE 2: Creación del Cuaderno de Trabajo (03:00 - 04:30)

* 🎬 **En pantalla:** En el menú lateral izquierdo, haz clic en **Workspace** $\rightarrow$ ve a tu carpeta de usuario (o haz clic en el botón **Create $\rightarrow$ Notebook** desde Home).
* 🎬 **En pantalla:** Nombra el cuaderno como: `01_MLOps_Calidad_Vinos`.
* 🎬 **En pantalla:** En la barra superior del cuaderno, verifica que el cómputo asignado esté conectado a **"Serverless"** o **"Default Interactive Compute"**.
* 🎙️ **Qué decir (Voz en off):**
  > *"Creamos un nuevo cuaderno de trabajo al que titulamos '01_MLOps_Calidad_Vinos' y verificamos que esté conectado a nuestro cómputo interactivo Serverless. Procederemos a ejecutar el ciclo MLOps en 5 fases técnicas."*

---

## BLOQUE 3: Fase 1 - Persistencia y Gobernanza en Delta Lake (Catalog) (04:30 - 06:30)

* 🎬 **En pantalla:** En la primera celda del cuaderno, copia y pega el siguiente código:

```python
# ==============================================================================
# FASE 1: Ingesta de Datos Reales y Persistencia en Delta Lake (Catalog)
# ==============================================================================
import pandas as pd
from sklearn.datasets import load_wine

# 1. Carga del conjunto de datos real de vinos de la UCI (Wine recognition dataset)
wine = load_wine(as_frame=True)
df = wine.frame

# Definición del target binario (1: Vino Clase 0 / Alta Calidad, 0: Otras clases)
df["target"] = (wine.target == 0).astype(int)

# 2. Conversión a DataFrame distribuido de Apache Spark
spark_df = spark.createDataFrame(df)

# 3. Persistencia en formato Delta Lake dentro del Catálogo de Databricks
spark_df.write.format("delta").mode("overwrite").saveAsTable("default.calidad_vinos_uci")

print("Tabla Delta 'default.calidad_vinos_uci' creada exitosamente en el Catálogo.")

# 4. Verificación mediante consulta Spark SQL
display(spark.sql("SELECT * FROM default.calidad_vinos_uci LIMIT 5"))
```

* 🎬 **En pantalla:** Presiona `Shift + Enter` para ejecutar la celda. Muestra la tabla de resultados renderizada con `display(...)`.
* 🎬 **En pantalla:** *(Opcional)* En el menú lateral, abre **Catalog** $\rightarrow$ `default` $\rightarrow$ muestra la tabla `calidad_vinos_uci`.
* 🎙️ **Qué decir (Voz en off):**
  > *"El primer pilar empresarial de Databricks es Delta Lake. No trabajamos con archivos CSV sueltos o datos volátiles en memoria. Convertimos los datos en una tabla Delta registrada formalmente en el Catálogo de Databricks.*
  > 
  > *Esto proporciona soporte a transacciones ACID, versionamiento de datos con Time Travel y gobernanza de acceso para todo el equipo de ciencia de datos, garantizando reproducibilidad absoluta desde la capa de almacenamiento."*

---

## BLOQUE 4: Fase 2 - Experimentación con MLflow Tracking (Experiments) (06:30 - 09:30)

* 🎬 **En pantalla:** En la siguiente celda, copia y pega el código con la corrección del tracking:

```python
# ==============================================================================
# FASE 2: Experimentación Científica y Rastreo con MLflow Tracking
# ==============================================================================
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from mlflow.models import infer_signature

# 1. Lectura gobernada directamente desde la tabla Delta Lake
data = spark.table("default.calidad_vinos_uci").toPandas()
X = data.drop(columns=["target", "target_name"], errors="ignore")
y = data["target"]

# División estratificada 80% entrenamiento / 20% prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# 2. En Databricks, las ejecuciones se vinculan automáticamente al experimento del cuaderno.
# Opcionalmente se puede asociar a la carpeta pública universal:
try:
    mlflow.set_experiment("/Shared/Experimento_Vinos_MLOps")
except Exception:
    pass  # En caso de permisos restringidos, registra en el experimento local del cuaderno

# 3. Prueba de hipótesis evaluando el hiperparámetro de profundidad (max_depth)
depths = [2, 4, 8, None]

print(f"{'Profundidad':<14} | {'Test Accuracy':<15} | {'Test F1-Score':<15}")
print("-" * 50)

for d in depths:
    with mlflow.start_run(run_name=f"RandomForest_depth_{d}"):
        model = RandomForestClassifier(n_estimators=50, max_depth=d, random_state=42)
        model.fit(X_train, y_train)
        
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds, average="weighted")
        
        # Firma formal de datos (Schema de entradas y salidas para evitar fallos en producción)
        signature = infer_signature(X_train, model.predict(X_train))
        
        # Registro automático en MLflow: Hiperparámetros, Métricas y Binario del Modelo
        mlflow.log_param("max_depth", str(d))
        mlflow.log_metric("test_accuracy", acc)
        mlflow.log_metric("test_f1", f1)
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="modelo_rf",
            signature=signature,
            input_example=X_train.iloc[:2]
        )
        
        tag = str(d) if d is not None else "Sin limite"
        print(f"{tag:<14} | {acc:<15.4f} | {f1:<15.4f}")
```

* 🎬 **En pantalla:** Presiona `Shift + Enter` para ejecutar. Observa cómo imprime las 4 ejecuciones con sus métricas sin ningún error.
* 🎬 **En pantalla:** En la barra lateral derecha del cuaderno, haz clic en el icono de matraz de laboratorio (**Experiment**). Se desplegará la lista de ejecuciones (`RandomForest_depth_2`, `depth_4`, `depth_8`, `None`).
* 🎬 **En pantalla:** Abre una de las ejecuciones para mostrar en pantalla los parámetros (`max_depth`), las métricas (`test_accuracy`, `test_f1`) y el artefacto guardado con su firma de esquema de datos.
* 🎙️ **Qué decir (Voz en off):**
  > *"Aquí apreciamos la potencia de MLflow Tracking integrado en Databricks. Ningún modelo queda en el olvido: cada ejecución almacena de manera inmutable sus hiperparámetros, sus métricas de evaluación en el conjunto de prueba y el binario serializado del modelo.*
  > 
  > *Además, registramos la firma estricta de datos (schema signature). Esto garantiza que, cuando el modelo sea desplegado en producción, cualquier petición entrante que no coincida exactamente con las 13 variables fisicoquímicas esperadas sea rechazada antes de generar una predicción errónea."*

---

## BLOQUE 5: Fase 3 - Catálogo y Gobernanza en Model Registry (Models) (09:30 - 11:00)

* 🎬 **En pantalla:** En una nueva celda, copia y pega el código para registrar el modelo óptimo:

```python
# ==============================================================================
# FASE 3: Registro y Versionamiento en el Model Registry de Databricks
# ==============================================================================
model_name = "Clasificador_Vinos_Produccion"

# Recuperamos el ID de la última ejecución óptima registrada en MLflow
run_id = mlflow.last_active_run().info.run_id
model_uri = f"runs:/{run_id}/modelo_rf"

# Registro formal en el catálogo de modelos
registered_model = mlflow.register_model(model_uri=model_uri, name=model_name)

print(f"Modelo promovido al Model Registry con éxito:")
print(f" - Nombre del Modelo: {model_name}")
print(f" - Versión Asignada:  {registered_model.version}")
```

* 🎬 **En pantalla:** Ejecuta la celda. Verás el mensaje confirmando el registro con la `Versión 1`.
* 🎬 **En pantalla:** Ve al menú lateral izquierdo de Databricks y haz clic en 👉 **"Models"** (bajo la sección AI/ML).
* 🎬 **En pantalla:** Muestra en pantalla el modelo `Clasificador_Vinos_Produccion` listado en el registro corporativo, con su `Version 1` y el linaje hacia el Run de MLflow.
* 🎙️ **Qué decir (Voz en off):**
  > *"Una vez que identificamos el modelo con mejor desempeño analítico, lo promovemos formalmente al Model Registry de Databricks bajo el nombre 'Clasificador_Vinos_Produccion'.*
  > 
  > *El Model Registry centraliza el ciclo de vida del activo de inteligencia artificial. Aquí podemos auditar quién entrenó el modelo, cuál fue el código exacto, los datos fuente en Delta Lake y gobernar su transición hacia producción."*

---

## BLOQUE 6: Fase 4 - Despliegue de Endpoint REST en Tiempo Real (Serving) (11:00 - 13:00)

* 🎬 **En pantalla:** En el menú lateral izquierdo de Databricks, haz clic en 👉 **"Serving"** (en la sección AI/ML).
* 🎬 **En pantalla:** En la esquina superior derecha, haz clic en el botón azul **"Create serving endpoint"** (o *"Crear endpoint de servicio"*).
* 🎬 **En pantalla:** Configura el formulario del endpoint exactamente así:
  1. **Name (Nombre del endpoint):** `endpoint-vinos-mlops`
  2. En la sección **Served entities** (Entidad a servir):
     * Tipo: **Model** (Modelo)
     * Model name: Selecciona de la lista `Clasificador_Vinos_Produccion`
     * Model version: Selecciona `1`
  3. **Compute scale-out:** Selecciona `Small` (la opción básica recomendada para optimizar consumo).
* 🎬 **En pantalla:** Haz clic en el botón azul **"Create"** (Crear).
* 🎬 **En pantalla:** Muestra cómo el endpoint queda creado y entra en estado de aprovisionamiento (*Provisioning / Ready*).
* 🎙️ **Qué decir (Voz en off):**
  > *"Llegamos al clímax del flujo de MLOps: el despliegue productivo con Model Serving. En la sección Serving creamos un endpoint denominado 'endpoint-vinos-mlops' asociándole la versión 1 de nuestro modelo registrado.*
  > 
  > *Databricks se encarga automáticamente de encapsular el modelo en un contenedor seguro, aprovisionar la infraestructura elástica, generar la URL de consumo y gestionar el balanceo de carga sin que debamos configurar servidores web, Dockerfiles ni clústeres de Kubernetes manualmente."*

---

## BLOQUE 7: Fase 5 - Consumo e Inferencia en Vivo de la API REST (13:00 - 14:30)

* 🎬 **En pantalla:** Dentro de la misma vista del endpoint en **Serving**, haz clic en la pestaña o panel **"Use endpoint"** o en la herramienta interactiva **"Query endpoint"** (Consultar endpoint).
* 🎬 **En pantalla:** En el área de texto del cuerpo de la petición (**Request JSON Payload**), pega la siguiente muestra real con las 13 variables:

```json
{
  "dataframe_records": [
    {
      "alcohol": 14.23,
      "malic_acid": 1.71,
      "ash": 2.43,
      "alcalinity_of_ash": 15.6,
      "magnesium": 127.0,
      "total_phenols": 2.80,
      "flavanoids": 3.06,
      "nonflavanoid_phenols": 0.28,
      "proanthocyanins": 2.29,
      "color_intensity": 5.64,
      "hue": 1.04,
      "od280/od315_of_diluted_wines": 3.92,
      "proline": 1065.0
    }
  ]
}
```

* 🎬 **En pantalla:** Haz clic en el botón **"Send Request"** (Enviar petición).
* 🎬 **En pantalla:** Muestra en pantalla el panel de respuesta con el resultado de la inferencia en tiempo real:

```json
{
  "predictions": [1]
}
```

* 🎙️ **Qué decir (Voz en off):**
  > *"Observemos el resultado inmediato en pantalla: enviamos una muestra de laboratorio con las 13 características fisicoquímicas del vino en formato JSON y el endpoint nos devuelve la predicción en milisegundos: `predictions: [1]`, clasificándolo como vino de alta calidad.*
  > 
  > *Cualquier aplicación cliente —sea un frontend web, una aplicación móvil o un microservicio empresarial— puede ahora consumir este modelo de forma segura y autenticada mediante tokens de acceso."*

---

## BLOQUE 8: Conclusiones y Cierre del Video (14:30 - 15:30)

* 🎬 **En pantalla:** Vuelve a la pantalla principal o al cuaderno mostrando el flujo completo cerrado.
* 🎙️ **Qué decir (Voz en off final):**
  > *"De esta manera hemos completado con éxito el ciclo de vida completo de un proyecto de Machine Learning a nivel de posgrado sobre Databricks:
  > 
  > 1. Persistimos y gobernamos los datos transaccionales en tablas **Delta Lake** mediante el Catálogo.
  > 2. Rastreamos formalmente la experimentación de hiperparámetros con **MLflow Tracking**.
  > 3. Versionamos el mejor modelo en el **Model Registry**.
  > 4. Y expusimos el artefacto como un servicio REST escalable mediante **Model Serving**, validando su inferencia en tiempo real.
  > 
  > En el siguiente video de la serie aprenderemos a implementar esta misma arquitectura corporativa sobre la nube pública de Amazon Web Services (AWS), configurando el almacenamiento S3, los roles de seguridad IAM y el despliegue en Databricks E2. ¡Muchas gracias y nos vemos en la próxima sesión!"*
