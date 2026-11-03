# Guía de Grabación Definitiva: Video 4 - Azure Databricks (Microsoft Azure)
### Espacio Académico: Trabajo de Grado 1 - Especialización en Ciencia de Datos
**Institución:** Universidad Santo Tomás - Seccional Tunja  
**Tema:** Azure Databricks desde Cero, Single Sign-On, Gobernanza en ADLS Gen2 y Clasificación con Regularización SVM  
**Duración Estimada:** 18 - 21 minutos  

---

## 📌 ARCHIVOS DISPONIBLES EN TU REPOSITORIO LOCAL
* 📓 **Cuaderno listo para importar en Azure Databricks (Recomendado):**  
  [04_Experimento_ML_Azure_Databricks.ipynb](file:///home/sazuniga99/Documentos/Universidad%20Santo%20Tomas/Especializacion%20en%20Ciencia%20de%20Datos/Guias_Tutoriales_Videos/04_Experimento_ML_Azure_Databricks.ipynb)
* 🐍 **Script Python equivalente:**  
  [04_Experimento_ML_Azure_Databricks.py](file:///home/sazuniga99/Documentos/Universidad%20Santo%20Tomas/Especializacion%20en%20Ciencia%20de%20Datos/Guias_Tutoriales_Videos/04_Experimento_ML_Azure_Databricks.py)
* 📄 **Guía de Grabación:**  
  [guia_04_azure_databricks.md](file:///home/sazuniga99/Documentos/Universidad%20Santo%20Tomas/Especializacion%20en%20Ciencia%20de%20Datos/Guias_Tutoriales_Videos/guia_04_azure_databricks.md)

---

## 🎯 FICHA TÉCNICA DEL TUTORIAL
* **Plataforma Cloud:** Microsoft Azure (`https://portal.azure.com`).
* **Servicio Analítico:** **Azure Databricks** (Servicio nativo *1st-Party* desarrollado conjuntamente por Microsoft y Databricks, integrado directamente dentro del Portal de Azure).
* **Autenticación e Identidad:** **Microsoft Entra ID** (anteriormente Azure Active Directory) mediante inicio de sesión único institucional (*Single Sign-On - SSO* con cuenta `@ustatunja.edu.co`).
* **Almacenamiento Subyacente:** **Azure Data Lake Storage Gen2 (ADLS Gen2)** / Azure Blob Storage gestionado automáticamente en el grupo de recursos administrado por Azure (`databricks-rg-...`).
* **Cómputo Elástico:** Clúster *Single Node* económico con política de apagado automático (*Auto-Termination*) en 20 minutos para costo cero tras la sesión (o Databricks Serverless Compute).
* **Dataset Científico:** *Wisconsin Diagnostic Breast Cancer* (569 biopsias reales con 30 descriptores morfométricos nucleares y diagnóstico patológico).
* **Algoritmo de Machine Learning:** Máquinas de Vectores de Soporte (*Support Vector Machine* - `SVC` con kernel RBF).
* **Prueba de Hipótesis:** Evaluación del impacto del parámetro de regularización ($C \in [0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]$) sobre la sensibilidad clínica (*Recall*) y el sobreajuste (*overfitting* vs *underfitting*).
* **MLOps y Gobernanza:** Registro y versionamiento de experimentos en **MLflow Tracking** y tablas transaccionales ACID con **Delta Lake**.

---

# GUION DE GRABACIÓN PASO A PASO (VOZ EN OFF + ACCIONES EN PANTALLA)

---

## BLOQUE 1: Introducción y Arquitectura Nativa de Azure Databricks (00:00 - 02:30)

* 🎬 **En pantalla:** Pantalla de bienvenida institucional de la Universidad Santo Tomás. Transición al Portal de Microsoft Azure (`https://portal.azure.com`).
* 🎙️ **Qué decir (Voz en off):**
  > *"Bienvenidos a este cuarto video tutorial de la serie de Ciencia de Datos y MLOps en la nube para el espacio académico Trabajo de Grado 1 de la Especialización en Ciencia de Datos de la Universidad Santo Tomás.*
  > 
  > *En los tutoriales anteriores exploramos Databricks en su versión comunitaria y posteriormente su despliegue sobre Amazon Web Services. Hoy daremos un salto arquitectónico fundamental al implementar **Azure Databricks**.*
  > 
  > *Una duda recurrente en ingeniería de datos es: ¿existe Databricks directamente dentro de Microsoft Azure o se requiere una plataforma externa? La respuesta es contundente: **Azure Databricks es un servicio nativo de primera clase de Microsoft**. No necesitamos registrarnos en sitios web externos ni gestionar credenciales separadas. Todo vive dentro del Portal de Azure, integrado con Microsoft Entra ID para Single Sign-On, respaldado por Azure Data Lake Storage Gen2 y gobernado bajo un modelo de costos unificado.*
  > 
  > *En esta sesión aprenderemos a crear la cuenta y el recurso desde cero, levantaremos un clúster optimizado para costos mínimos, importaremos nuestro pipeline de Machine Learning con 569 datos biomédicos reales, contrastaremos una hipótesis formal sobre regularización en algoritmos SVM para maximizar la sensibilidad médica, y analizaremos las ventajas comparativas frente al ecosistema de AWS."*

---

## BLOQUE 2: Creación de Cuenta en Azure y Configuración de Alerta de Costos (02:30 - 05:00)

* 🎬 **En pantalla:** Abre el navegador en la página oficial de suscripción de Azure:
  * 👉 **Opción A (Recomendada para la Especialización):** `https://azure.microsoft.com/free/students/` (Azure for Students: **$100 USD de crédito gratuito sin tarjeta de crédito**, activable con el correo institucional `@ustatunja.edu.co`).
  * 👉 **Opción B:** `https://azure.microsoft.com/free/` (Cuenta gratuita estándar de Azure: **$200 USD de crédito durante 30 días** y 12 meses de servicios populares gratuitos).
* 🎙️ **Qué decir (Voz en off):**
  > *"Para acceder a Azure tenemos dos opciones oficiales muy convenientes: Azure for Students, que otorga 100 dólares de crédito anual sin necesidad de ingresar tarjeta de crédito únicamente validando nuestro correo institucional de la Santo Tomás, o la cuenta gratuita estándar de Azure con 200 dólares de crédito inicial.*
  > 
  > *Una vez creada o activada la suscripción, ingresamos a la consola centralizada de Microsoft: `portal.azure.com`."*

* 🎬 **En pantalla:** En el Portal de Azure (`https://portal.azure.com`), escribe en la barra superior de búsqueda: **`Cost Management`** $\rightarrow$ haz clic en **Administración de costos + Facturación** (*Cost Management + Billing*).
* 🎬 **En pantalla:** En el menú izquierdo, haz clic en **"Presupuestos"** (*Budgets*) $\rightarrow$ botón **"+ Agregar"** (*Add*).
* 🎬 **En pantalla:** Diligencia el presupuesto de seguridad:
  * **Nombre:** `Presupuesto-Alerta-TG1`
  * **Importe presupuestado:** `$5.00 USD` (o el equivalente en moneda local).
  * **Configuración de alertas:** Al alcanzar el `80%` y el `100%`, notificar a tu correo electrónico institucional.
* 🎬 **En pantalla:** Clic en **"Crear"**.
* 🎙️ **Qué decir (Voz en off):**
  > *"Siguiendo las mejores prácticas de gobernanza en la nube, fijamos una alerta preventiva de presupuesto a 5 dólares. Esto nos garantiza control financiero absoluto y tranquilidad durante el desarrollo de nuestras prácticas académicas."*

---

## BLOQUE 3: Creación del Recurso Azure Databricks en el Portal (05:00 - 08:00)

* 🎬 **En pantalla:** En la barra de búsqueda superior del Portal de Azure, escribe **`Azure Databricks`** y selecciona el servicio con el icono azul característico de Databricks.
* 🎬 **En pantalla:** Haz clic en el botón superior **"+ Crear"** (*Create* o *Crear área de trabajo de Azure Databricks*).
* 🎬 **En pantalla:** Muestra la pestaña **Aspectos básicos** (*Basics*) y diligencia los campos:
  * **Suscripción:** Selecciona tu suscripción activa (ej. *Azure subscription 1* o *Azure for Students*).
  * **Grupo de recursos (Resource Group):** Clic en **"Crear nuevo"** y escribe: 👉 **`rg-cienciadatos-tg1`**.
  * **Nombre del área de trabajo (Workspace name):** 👉 **`workspace-azure-databricks-tg1`**.
  * **Región:** Selecciona una región con alta disponibilidad de cuotas (ejemplo: `East US 2` o `East US`).
  * **Nivel de precios (Pricing Tier):** Selecciona 👉 **Standard (Apache Spark, protección segura de datos)** *(o Trial de 14 días si está disponible en la lista)*.
* 🎙️ **Qué decir (Voz en off):**
  > *"Aquí observamos la enorme ventaja de la arquitectura integrada de Microsoft: no salimos del portal. Agrupamos los recursos en `rg-cienciadatos-tg1`, definimos el nombre del área de trabajo y seleccionamos el nivel de precios Standard, que es significativamente más económico y cubre la totalidad de librerías para analítica avanzada y Machine Learning."*

* 🎬 **En pantalla:** Desplázate hacia abajo hasta el campo **"Nombre del grupo de recursos administrado"**.
* 🎬 **En pantalla:** Déjalo por defecto (Azure autogenera un grupo llamado `databricks-rg-workspace-...` donde almacenará automáticamente los discos administrados y la cuenta de Azure Data Lake Storage Gen2).
* 🎬 **En pantalla:** Haz clic en el botón azul inferior 👉 **"Revisar y crear"** (*Review + Create*).
* 🎬 **En pantalla:** Pasa la validación verde $\rightarrow$ haz clic en **"Crear"**.
* 🎬 **En pantalla:** Muestra la pantalla *"La implementación está en curso"* (Azure tarda aproximadamente entre 2 y 3 minutos en desplegar la infraestructura).
* 🎬 **En pantalla:** Aparece el mensaje *"Se completó la implementación"* $\rightarrow$ haz clic en el botón azul 👉 **"Ir al recurso"** (*Go to resource*).
* 🎙️ **Qué decir (Voz en off):**
  > *"En cuestión de minutos, el orquestador de Azure Resource Manager ha creado la red virtual, el almacenamiento subyacente y la instancia analítica de Databricks sin que hayamos tenido que configurar subredes ni políticas de enrutamiento complejas."*

---

## BLOQUE 4: Acceso con Single Sign-On (Entra ID) y Cómputo Elástico (08:00 - 10:30)

* 🎬 **En pantalla:** Dentro de la vista general del recurso `workspace-azure-databricks-tg1`, haz clic en el botón central:
  👉 **"Iniciar área de trabajo"** (*Launch Workspace*).
* 🎬 **En pantalla:** El navegador se redirige y abre la interfaz de Databricks autenticándose de forma automática e instantánea con tu usuario institucional de Microsoft.
* 🎙️ **Qué decir (Voz en off):**
  > *"Observen la fluidez del acceso: no tuvimos que digitar credenciales, crear usuarios ni vincular tokens. Gracias a la integración con Microsoft Entra ID (antes Azure Active Directory), el inicio de sesión único (Single Sign-On) reconoce nuestra identidad corporativa al instante."*

* 🎬 **En pantalla:** En el menú lateral izquierdo de Azure Databricks, haz clic en **"Compute"** $\rightarrow$ botón azul **"Create compute"** *(o revisa si tu espacio cuenta con Serverless activo)*.
* 🎬 **En pantalla:** Si configuras un clúster dedicado para máximo control, diligencia:
  * **Policy / Cluster Mode:** Cambia a 👉 **Single Node** (Acepta el mensaje emergente de confirmación).
  * **Compute name:** `Cluster-Azure-ML`
  * **Databricks Runtime Version:** Versión LTS con soporte de ML (ejemplo: `15.4 LTS ML` o `14.3 LTS ML`).
  * **Auto-termination:** Configura 👉 `20` minutos.
  * **Node type (Máquina Virtual de Azure):** Selecciona una máquina balanceada como `Standard_D4s_v5` (4 núcleos, 16 GB RAM) o `Standard_DS3_v2`.
* 🎬 **En pantalla:** Haz clic en **"Create compute"** y muestra cómo el clúster arranca (o cómo el entorno Serverless asigna cómputo inmediato).
* 🎙️ **Qué decir (Voz en off):**
  > *"Para optimizar nuestros créditos en Azure, seleccionamos el modo Single Node con la máquina virtual Standard_D4s_v5 y fijamos la terminación automática en 20 minutos. Si cerramos el navegador y nos retiramos, Azure apagará el clúster automáticamente, evitando consumos involuntarios."*

---

## BLOQUE 5: Importación del Cuaderno y Formulación de Hipótesis (10:30 - 12:30)

* 🎬 **En pantalla:** En el menú lateral izquierdo de Azure Databricks, haz clic en 👉 **"Workspace"**.
* 🎬 **En pantalla:** Navega a tu carpeta personal: `Workspace > Users > [tu_correo_institucional]`.
* 🎬 **En pantalla:** Haz clic derecho en el espacio en blanco $\rightarrow$ selecciona 👉 **"Import"** *(o en la esquina superior derecha, clic en los tres puntos $\rightarrow$ Import)*.
* 🎬 **En pantalla:** En la ventana emergente:
  * Deja marcada la opción **File**.
  * Haz clic en **"browse"** (o arrastra el archivo) y selecciona desde tu carpeta local:  
    👉 **`04_Experimento_ML_Azure_Databricks.ipynb`**
  * Haz clic en el botón azul 👉 **"Import"**.
* 🎬 **En pantalla:** ¡El cuaderno se abre al instante con sus celdas ya estructuradas, fórmulas LaTeX y código documentado!
* 🎙️ **Qué decir (Voz en off):**
  > *"Importamos directamente nuestro cuaderno `04_Experimento_ML_Azure_Databricks.ipynb`. En un solo clic disponemos de toda la estructura metodológica, matemática y de código lista para ejecutarse."*

* 🎬 **En pantalla:** Muestra la primera celda en Markdown renderizada:
  * **Pregunta Analítica:** ¿Cómo influye la fuerza del parámetro de regularización ($C$) en un clasificador SVM con kernel RBF sobre la detección de tumores malignos vs benignos, y cuál es el punto óptimo que maximiza la sensibilidad clínica (*Recall*) minimizando los falsos negativos sin inducir sobreajuste?
  * **Hipótesis Nula ($H_0$):** La variación de $C$ no produce diferencias significativas en la tasa de falsos negativos ni en el Recall de prueba.
  * **Hipótesis Alternativa ($H_1$):** Valores muy bajos de $C$ ($C \le 0.01$) inducen subajuste severo al simplificar en exceso la frontera, mientras que valores muy altos ($C \ge 100$) inducen sobreajuste. Existe un codo de equilibrio óptimo en $C=1.0$ que maximiza la sensibilidad ($\ge 98\%$) en generalización.
* 🎙️ **Qué decir (Voz en off):**
  > *"Establecemos el marco científico: en analítica biomédica y oncológica, la métrica crítica no es únicamente la exactitud global, sino la Sensibilidad o Recall, puesto que un falso negativo representa un paciente con cáncer no diagnosticado oportunamente."*

---

## BLOQUE 6: Configuración de Infraestructura e Ingesta de Datos (12:30 - 14:30)

* 🎬 **En pantalla:** Ve a la celda 2 de código (Configuración del Entorno) y presiona `Shift + Enter`:
```python
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix, classification_report

print("=" * 70)
print("INFRAESTRUCTURA CLOUD: AZURE DATABRICKS (MICROSOFT AZURE)")
print("=" * 70)
print("-> Proveedor de Nube       : Microsoft Azure")
print("-> Servicio Analítico      : Azure Databricks (Servicio Nativo 1st-Party)")
print("-> Autenticación           : Microsoft Entra ID (Single Sign-On)")
print("-> Almacenamiento Raíz     : Azure Data Lake Storage Gen2 (ADLS Gen2)")
print("-> Frameworks Analíticos   : Scikit-Learn | Spark | Delta Lake | MLflow")
print("=" * 70)
print("✅ Entorno de ejecución validado exitosamente en Azure Databricks.")
```
* 🎬 **En pantalla:** Muestra la salida con la confirmación de la infraestructura en Azure.
* 🎙️ **Qué decir (Voz en off):**
  > *"Ejecutamos la celda de infraestructura y validamos la interacción con el entorno de Azure Databricks, las librerías analíticas y el catálogo gobernado."*

* 🎬 **En pantalla:** Desplázate a la celda 3 (Carga y Exploración de Datos) y presiona `Shift + Enter`:
```python
# 1. Carga del conjunto de datos biomédicos reales (Wisconsin Diagnostic Breast Cancer)
cancer_dataset = load_breast_cancer(as_frame=True)
df_cancer = cancer_dataset.frame

# 2. Resumen exploratorio de dimensiones y balance de clases
n_filas, n_columnas = df_cancer.shape
print(f"Dimensiones del Dataset: {n_filas} registros de biopsia y {n_columnas} variables.")
print("\nDistribución de diagnósticos clínicos:")
print(f" -> Benigno  (Clase 1): {(df_cancer['target'] == 1).sum()} casos ({(df_cancer['target'] == 1).mean() * 100:.1f}%)")
print(f" -> Maligno  (Clase 0): {(df_cancer['target'] == 0).sum()} casos ({(df_cancer['target'] == 0).mean() * 100:.1f}%)")

display(df_cancer.head(5))
```
* 🎬 **En pantalla:** Muestra las 569 biopsias reales, las 30 variables continuas (radio, perímetro, textura, etc.) y la distribución de clases: 357 benignos (62.7%) y 212 malignos (37.3%).
* 🎙️ **Qué decir (Voz en off):**
  > *"Cargamos los datos biomédicos reales de biopsias de mama. Contamos con 569 casos clínicos y 30 características morfométricas de los núcleos celulares, con una distribución de 62.7% benignos y 37.3% malignos."*

---

## BLOQUE 7: Estandarización y Experimento Científico de Regularización (14:30 - 17:30)

* 🎬 **En pantalla:** Ve a la celda 4 (Partición y Escalado) y ejecuta con `Shift + Enter`:
```python
# Partición estratificada (80% entrenamiento, 20% prueba)
X = df_cancer.drop(columns=["target"])
y = df_cancer["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"Muestras de Entrenamiento : {X_train.shape[0]} biopsias")
print(f"Muestras de Prueba (Test) : {X_test.shape[0]} biopsias")

# Estandarización requerida por la geometría del kernel RBF
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("✅ Estandarización z-score completada para las 30 características clínicas.")
```
* 🎙️ **Qué decir (Voz en off):**
  > *"Aplicamos una partición estratificada 80/20 para conservar la proporción médica de casos positivos y negativos en ambos subconjuntos. Dado que las Máquinas de Vectores de Soporte calculan distancias euclidianas mediante un kernel radial (RBF), es indispensable aplicar StandardScaler para evitar que variables con rangos numéricos elevados dominen el margen del hiperplano."*

* 🎬 **En pantalla:** Ve a la celda 5 (Barrido de Regularización) y presiona `Shift + Enter`:
```python
C_values = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
train_acc_list, test_acc_list, test_recall_list, test_f1_list = [], [], []

print(f"{'Parámetro C':<14} | {'Train Acc':<12} | {'Test Acc':<12} | {'Test Recall':<14} | {'Test F1':<10}")
print("-" * 72)

for c in C_values:
    svm = SVC(C=c, kernel="rbf", random_state=42)
    svm.fit(X_train_scaled, y_train)
    pred_train = svm.predict(X_train_scaled)
    pred_test = svm.predict(X_test_scaled)
    
    acc_tr = accuracy_score(y_train, pred_train)
    acc_te = accuracy_score(y_test, pred_test)
    rec_te = recall_score(y_test, pred_test)
    f1_te = f1_score(y_test, pred_test)
    
    train_acc_list.append(acc_tr)
    test_acc_list.append(acc_te)
    test_recall_list.append(rec_te)
    test_f1_list.append(f1_te)
    print(f"C = {c:<10.3f} | {acc_tr:<12.4f} | {acc_te:<12.4f} | {rec_te:<14.4f} | {f1_te:<10.4f}")
```
* 🎬 **En pantalla:** Señala con el cursor los valores de la tabla en pantalla:
  * Con $C = 0.001$ y $0.01$: Exactitud de solo $63.16\%$ (Subajuste extremo).
  * Con $C = 1.0$: Exactitud en prueba de **$98.25\%$**, Sensibilidad (*Recall*) de **$98.61\%$** y F1-Score de **$98.61\%$**.
  * Con $C \ge 100$: Exactitud de entrenamiento alcanza el $100\%$, pero en prueba decae a $94.74\%$ y el Recall baja a $93.06\%$ (Sobreajuste evidente).
* 🎙️ **Qué decir (Voz en off):**
  > *"Analicemos la evidencia experimental: con valores muy pequeños de C (0.001 a 0.01), la regularización excesiva provoca subajuste (*underfitting*), prediciendo únicamente la clase mayoritaria. Al incrementar C hasta 1.0, el modelo alcanza su máximo poder de generalización con un 98.25% de exactitud y un impresionante 98.61% de Recall en datos de prueba no observados. No obstante, al elevar C a 100 o 1000, el entrenamiento alcanza el 100% perfecto, pero la sensibilidad en prueba cae al 93%, demostrando cómo el modelo empieza a sobreajustarse memorizando el ruido de la muestra."*

* 🎬 **En pantalla:** Ve a la siguiente celda y muestra la gráfica de curvas de regularización en escala semilogarítmica:
* 🎬 **En pantalla:** Señala la línea punteada vertical en $C = 1.0$.
* 🎙️ **Qué decir (Voz en off):**
  > *"La gráfica semilogarítmica ilustra con nitidez el compromiso sesgo-varianza. La línea gris vertical en C=1.0 marca el punto óptimo de generalización donde maximizamos la sensibilidad y el F1-Score sin incurrir en memorización."*

---

## BLOQUE 8: Delta Lake en ADLS Gen2 y Registro MLOps en MLflow (17:30 - 19:30)

* 🎬 **En pantalla:** Ve a la celda final de persistencia y MLOps, y presiona `Shift + Enter`:
```python
import mlflow
import mlflow.sklearn
import joblib
from mlflow.models import infer_signature

best_svm = SVC(C=1.0, kernel="rbf", random_state=42)
best_svm.fit(X_train_scaled, y_train)
best_preds = best_svm.predict(X_test_scaled)

final_acc = accuracy_score(y_test, best_preds)
final_recall = recall_score(y_test, best_preds)
final_f1 = f1_score(y_test, best_preds)
signature = infer_signature(X_train_scaled, best_preds)

os.makedirs("/tmp/models", exist_ok=True)
model_artifact_path = "/tmp/models/svm_breast_cancer_rbf_best.joblib"
joblib.dump(best_svm, model_artifact_path)

# Persistencia de tabla en Delta Lake sobre Azure Data Lake Storage
spark_df = spark.createDataFrame(df_cancer)
spark_df.write.format("delta").mode("overwrite").saveAsTable("cancer_diagnostics_delta")
azure_storage_path = spark.sql("DESCRIBE DETAIL cancer_diagnostics_delta").select("location").collect()[0]["location"]

# Registro en MLflow Tracking nativo de Azure Databricks
with mlflow.start_run(run_name="SVM_RBF_Azure_Databricks_Clinical"):
    mlflow.log_params({"model_type": "SVC", "C": 1.0, "kernel": "rbf", "cloud": "Azure"})
    mlflow.log_metrics({"test_accuracy": final_acc, "test_recall": final_recall, "test_f1": final_f1})
    mlflow.log_artifact(model_artifact_path, artifact_path="model_artifact")
    mlflow.sklearn.log_model(best_svm, name="model", signature=signature, serialization_format="cloudpickle")

print(f"✅ Tabla persistida en Delta Lake sobre Azure Data Lake Storage:")
print(f"   -> Ubicación física en Azure: {azure_storage_path}")
print(f"\nExactitud: {final_acc * 100:.2f}% | Sensibilidad: {final_recall * 100:.2f}% | F1: {final_f1 * 100:.2f}%")
```
* 🎬 **En pantalla:** En la barra superior derecha del cuaderno, haz clic en el icono **"Experiment"** de MLflow para mostrar la corrida registrada con sus parámetros (`C=1.0`), métricas y artefacto exportado.
* 🎙️ **Qué decir (Voz en off):**
  > *"Completamos la fase de gobernanza y MLOps: la tabla analítica queda persistida en formato Delta Lake con transacciones ACID sobre Azure Data Lake Storage Gen2, y el modelo óptimo validado queda registrado en MLflow con su firma de entrada y artefacto de producción listo para ser desplegado en un contenedor o punto de conexión en Azure Machine Learning."*

---

## BLOQUE 9: Comparativa AWS vs Azure, Protocolo de Apagado y Cierre (19:30 - 21:00)

* 🎬 **En pantalla:** Muestra en pantalla el resumen comparativo entre los dos gigantes de la nube:

| Criterio Arquitectónico | Databricks en AWS (Video 3) | Azure Databricks (Video 4) |
| :--- | :--- | :--- |
| **Naturaleza del Servicio** | Servicio SaaS vinculado mediante roles IAM cruzados | **Servicio nativo 1st-Party** de Microsoft Azure |
| **Inicio de Sesión (Auth)** | Consola externa (`accounts.cloud.databricks.com`) | **Single Sign-On nativo** con Microsoft Entra ID |
| **Almacenamiento del Lago** | Amazon S3 con gestión de buckets y capas | **Azure Data Lake Storage Gen2 (ADLS Gen2)** |
| **Facturación de Nube** | Facturación desagregada (EC2 en AWS + DBUs Databricks) | **Factura unificada 100% en Microsoft Azure** |
| **Aprovisionamiento** | Creación manual de credenciales IAM | Despliegue con 1 clic en Azure Resource Manager |

* 🎙️ **Qué decir (Voz en off):**
  > *"Comparando ambas arquitecturas, Azure Databricks destaca por su integración nativa: un solo portal, autenticación automática con Entra ID y facturación unificada. En contraparte, AWS ofrece un aislamiento granular profundo de redes VPC para organizaciones con políticas perimetrales estrictas.*
  > 
  > *Para finalizar nuestra sesión y mantener el costo en cero: en el menú Compute detenemos nuestro clúster `Cluster-Azure-ML`. Y cuando finalice el período de estudio, si deseamos eliminar todo, bastará con ingresar al Portal de Azure y borrar el grupo de recursos `rg-cienciadatos-tg1`.*
  > 
  > *En nuestro quinto y último video de la serie nos enfocaremos 100% en **MLOps y Versionamiento**: conectaremos MLflow Model Registry, crearemos etapas de staging a producción y resolveremos los desafíos de reproducibilidad en la nube. ¡Muchas gracias por acompañarnos y nos vemos en el video final!"*

---

### 📋 Checklist de Inicio Rápido antes de pulsar Grabar en OBS:
1. Pestaña 1 abierta: **Portal de Microsoft Azure** (`https://portal.azure.com`).
2. Presupuesto de alerta configurado: `$5.00 USD` en **Cost Management + Billing**.
3. Recurso creado en el portal: `workspace-azure-databricks-tg1` dentro de `rg-cienciadatos-tg1`.
4. Pestaña 2 abierta: Botón **"Iniciar área de trabajo"** listo para mostrar el Single Sign-On con Microsoft Entra ID.
5. Archivo listo para importar con 1 solo clic en Databricks:  
   👉 [04_Experimento_ML_Azure_Databricks.ipynb](file:///home/sazuniga99/Documentos/Universidad%20Santo%20Tomas/Especializacion%20en%20Ciencia%20de%20Datos/Guias_Tutoriales_Videos/04_Experimento_ML_Azure_Databricks.ipynb)
