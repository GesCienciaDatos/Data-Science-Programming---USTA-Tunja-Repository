# Guía de Grabación Completa: JIRA Software desde Cero para Ciencia de Datos

Esta guía está redactada como un guion técnico paso a paso, lineal y continuo. Contiene exactamente **qué hacer en pantalla (🎬)** y **qué decir palabra por palabra (🎙️)** desde que abres el navegador en blanco hasta que el proyecto queda 100% configurado, teniendo en cuenta el comportamiento real de las plantillas de Jira.

---

## FICHA TÉCNICA DEL VIDEO
* **Título sugerido:** *"JIRA Software desde Cero para Ciencia de Datos: Metodología Scrum, Roles de Gobernanza y Gestión de Sprints"*.
* **Duración estimada:** 15 a 18 minutos.
* **Herramientas:** Navegador web y cuenta gratuita de Jira Cloud.

---

## PASO 1: Registro en Jira Cloud y Creación del Espacio (Minuto 0 a 3)

### 1.1. Registro en la plataforma gratuita
* 🎬 **En pantalla:** Abre el navegador en `https://www.atlassian.com/es/software/jira`.
* 🎬 **En pantalla:** Haz clic en el botón azul **"Obtener gratis"**.
* 🎙️ **Qué decir (Voz en off):**
  > *"Hola a todos. En este video aprenderemos a configurar Jira Software desde cero para gobernar un proyecto real de Ciencia de Datos bajo la metodología Scrum y los lineamientos de Trabajo de Grado. Usaremos la versión en la nube 100% gratuita."*
* 🎬 **En pantalla:** Marca únicamente **Jira** $\rightarrow$ Clic en **"Siguiente"**.
* 🎬 **En pantalla:** Inicia sesión con tu cuenta de Google o correo institucional.
* 🎬 **En pantalla:** En el campo *"Asigna un nombre a tu sitio"*, escribe: `proyecto-tg1-cienciadatos.atlassian.net` (o el nombre que esté disponible) $\rightarrow$ Clic en **"Continuar"**.
* 🎬 **En pantalla:** Si aparecen preguntas iniciales de configuración, haz clic en **"Omitir"** (Skip) abajo para ir directo al entorno.

---

### 1.2. Creación del Proyecto con Plantilla Scrum
* 🎬 **En pantalla:** En la barra superior, haz clic en **"Proyectos"** $\rightarrow$ **"Crear proyecto"**.
* 🎬 **En pantalla:** Selecciona la categoría **"Desarrollo de software"** y haz clic sobre la plantilla **"Scrum"**.
* 🎬 **En pantalla:** Haz clic en **"Usar plantilla"** $\rightarrow$ Elige **"Gestionado por el equipo"** (Team-managed).
* 🎬 **En pantalla:** Completa los campos:
  * **Nombre:** `Trabajo de Grado 1 - Equipo [Número]` (ej. `Trabajo de Grado 1 - Equipo 3`).
  * **Clave:** `TG1` (o `SCRUM`).
* 🎬 **En pantalla:** Haz clic en **"Crear proyecto"**.
* 🎙️ **Qué decir (Voz en off):**
  > *"Es indispensable seleccionar la plantilla Scrum, ya que nuestro plan de trabajo se evaluará mediante ciclos semanales o sprints. La clave de proyecto que definimos identificará de forma única cada requerimiento técnico de la investigación."*

---

## PASO 2: Configuración del Equipo y Roles de Gobernanza (Minuto 3 a 6)

### 2.1. Creación del Equipo en Atlassian Teams
* 🎬 **En pantalla:** En el menú lateral izquierdo de Jira, haz clic en el botón 👉 **"Equipos"** (abajo de Paneles).
* 🎬 **En pantalla:** Haz clic en el botón azul **"Crear un equipo"** (o *"Comenzar un equipo"*).
* 🎬 **En pantalla:** En el nombre escribe:
  `Equipo [Número] - Especialización en Ciencia de Datos`
* 🎬 **En pantalla:** Haz clic en **"Crear equipo"**.
* 🎙️ **Qué decir (Voz en off):**
  > *"En Ciencia de Datos cada integrante asume una responsabilidad dual: una función ágil en Scrum y un cargo formal de gobernanza sobre los datos. Para formalizar esta estructura en el sistema, creamos nuestro equipo oficial en Atlassian Teams."*

---

### 2.2. Documentar la Matriz de Roles en el Perfil del Equipo
* 🎬 **En pantalla:** En la página del equipo que se abre, busca la sección **"Lo que hacemos"** y haz clic en el texto gris:
  👉 **"Comparte lo que hace tu equipo"**.
* 🎬 **En pantalla:** En el cuadro de texto, pega la siguiente matriz oficial:
  ```text
  ROLES DUALES DE GOBERNANZA - TRABAJO DE GRADO 1:

  • Product Owner & Data Owner: Santiago Alejandro Zuñiga Melo
    (Visión de negocio, priorización de requerimientos y titularidad de datos reales).
  • Scrum Master & Data Steward: [Integrante 2]
    (Facilitador ágil, diccionario de metadatos y calidad de la información).
  • Dev Team & Data Custodian (Ing. Datos): [Integrante 3]
    (Arquitectura técnica, almacenamiento, seguridad y pipelines en Databricks).
  • Dev Team & Data Consumer (Analítica): [Integrante 4]
    (Formulación de hipótesis, análisis exploratorio EDA y modelos de Machine Learning).

  *En equipos de 3: El integrante 1 asume PO + Data Owner + Data Consumer.
  ```
* 🎬 **En pantalla:** Haz clic en el botón azul **"Guardar"**.
* 🎙️ **Qué decir (Voz en off):**
  > *"Como estoy realizando este tutorial de forma individual para fines demostrativos, he registrado a mi usuario con el rol de Product Owner y Data Owner. En sus equipos de trabajo, cada uno de los 3 o 4 integrantes quedará formalizado en esta ficha con su respectivo cargo de gobernanza."*

---

### 2.3. Conectar el Equipo al Espacio de Jira e Invitar al Docente
* 🎬 **En pantalla:** En la columna derecha de esa misma pantalla, busca **"Enlaces al equipo"** y haz clic en:
  👉 **"Añadir un espacio de Jira"**.
* 🎬 **En pantalla:** Selecciona tu proyecto (`Trabajo de Grado 1...` o `Mi equipo de gestión de proyectos`) y haz clic en **Añadir**.
* 🎬 **En pantalla:** Arriba a la derecha, haz clic en el botón blanco **"Añadir personas"** $\rightarrow$ escribe el correo del docente tutor institucional y los correos de tus compañeros $\rightarrow$ Clic en **Añadir**.
* 🎙️ **Qué decir (Voz en off):**
  > *"Vinculamos el equipo a nuestro proyecto e invitamos al docente tutor. De esta forma, el docente tiene acceso directo a nuestra plataforma para auditar avances, tiempos y aportes individuales."*

---

## PASO 3: Organización de los 5 Sprints en el Backlog (Minuto 6 a 9)

### 3.1. Entender la Plantilla que crea Jira por Defecto
* 🎬 **En pantalla:** Regresa a tu proyecto de Jira y haz clic en la pestaña **"Backlog"** (arriba a la izquierda, al lado de Tablero).
* 🎙️ **Qué decir (Voz en off):**
  > *"Al entrar al Backlog, observen que Jira crea automáticamente dos sprints de muestra con nombres como 'SCRUM Sprint 0' o 'SCRUM Sprint 1' y unas tareas de ejemplo. Vamos a limpiar esas tareas y a renombrar los sprints para estructurar nuestro calendario de 5 semanas."*

---

### 3.2. Limpiar Tareas de Ejemplo y Renombrar los Sprints Existentes
* 🎬 **En pantalla:** En las tareas de muestra (`Tarea 1`, `Tarea 2`, `Tarea 3`), haz clic en los **tres puntos `...`** de cada una $\rightarrow$ selecciona **"Eliminar"**.
* 🎬 **En pantalla:** En la cabecera gris del primer sprint (`SCRUM Sprint 0` o `Sprint 0`), haz clic en los **tres puntos `...`** a la derecha $\rightarrow$ **"Editar sprint"** $\rightarrow$ cambia el nombre a **`Sprint 1`** $\rightarrow$ Clic en **Guardar**.
* 🎬 **En pantalla:** En el segundo sprint (`SCRUM Sprint 1`), haz clic en los **tres puntos `...`** $\rightarrow$ **"Editar sprint"** $\rightarrow$ cambia el nombre a **`Sprint 2`** $\rightarrow$ Clic en **Guardar**.

---

### 3.3. Completar los 5 Sprints Semanales
* 🎬 **En pantalla:** En la barra gris a la derecha del Backlog, haz clic en el botón **"Crear sprint"** **3 veces más**.
* 🎬 **En pantalla:** Verás que ahora tienes perfectamente creados los 5 bloques en orden:
  * `Sprint 1`
  * `Sprint 2`
  * `Sprint 3`
  * `Sprint 4`
  * `Sprint 5`
* 🎙️ **Qué decir (Voz en off):**
  > *"De esta manera tan rápida dejamos organizados los 5 sprints semanales de la asignatura: los Sprints 1 y 2 corresponden a la primera entrega del 25% (el Informe con problema real, fuentes y diseño experimental), y los Sprints 3, 4 y 5 corresponden a la entrega del 75% (el Anteproyecto completo con EDA, arquitectura en Databricks y definición del MVP)."*

---

## PASO 4: Definición de Terminado (DoD) (Minuto 9 a 10)

* 🎬 **En pantalla:** En la barra del Backlog, haz clic en **`+ Crear`** $\rightarrow$ escribe:
  `[POLÍTICA] Definición de Terminado (DoD) del Equipo` $\rightarrow$ pulsa `Enter`.
* 🎬 **En pantalla:** Haz clic sobre ese ticket para abrir su panel lateral derecho $\rightarrow$ en **Descripción**, pega esto y haz clic en **Guardar**:
  ```text
  Definición de Terminado (Definition of Done - DoD):
  1. Cumple al 100% con los criterios de aceptación técnicos de la historia.
  2. Evidencia de código o documento enlazada al repositorio GitHub referenciando el código del ticket.
  3. No se utilizan datos sintéticos (solo datos reales autorizados o de repositorios oficiales).
  4. Cumplimiento de normas institucionales Santoto y formato APA 7.
  5. Aprobado formalmente por el rol dual responsable.
  ```
* 🎙️ **Qué decir (Voz en off):**
  > *"Antes de iniciar el trabajo, dejamos registrada la Definición de Terminado o DoD. Esta política establece que ninguna tarea se da por cerrada si no cumple con sus criterios de aceptación, si emplea datos sintéticos o si carece de evidencia en GitHub."*

---

## PASO 5: Carga del Product Backlog (10 Historias de Ciencia de Datos) (Minuto 10 a 15)

> [!TIP]
> **MECÁNICA CLIC A CLIC PARA CADA HISTORIA:**
> 1. En la parte inferior del Backlog, haz clic en **`+ Crear`** $\rightarrow$ escribe el Título $\rightarrow$ pulsa `Enter`.
> 2. Haz clic sobre la historia creada para abrir el panel lateral derecho.
> 3. En **Etiquetas (Labels)**: escribe la etiqueta del rol (ej: `PO-DataOwner`) y presiona `Enter`.
> 4. En **Responsable**: selecciónate a ti mismo para el video.
> 5. En **Descripción**: pega los criterios de aceptación y haz clic en **Guardar**.
> 6. Arrastra la tarjeta con el mouse hacia el contenedor del Sprint que le corresponde.

* 🎙️ **Qué decir al crear la primera historia:**
  > *"Para este tutorial me verán asignado a mí en el campo 'Responsable'. Sin embargo, lo que fija el cargo académico ante el docente evaluador es el campo 'Etiquetas', donde marcamos el rol de gobernanza. En sus equipos de trabajo, el Scrum Master seleccionará aquí al compañero asignado según la matriz que definimos en el equipo."*

---

### HISTORIAS DEL SPRINT 1 (Informe - 25%)

#### Historia 1: Problema Real y Viabilidad
* **Título:** `TG1-1: Documentar problema real del sector y verificar viabilidad con usuario`
* **Etiqueta (Label):** `PO-DataOwner`
* **Responsable:** Tú mismo | **Sprint:** Arrastrar a **Sprint 1**
* **Descripción a pegar:**
```text
Como: Product Owner y Data Owner
Quiero: Documentar una necesidad real de una organización y verificar que existan datos accesibles
Para: Garantizar que el alcance sea viable para desarrollar y desplegar un MVP en Trabajo de Grado 2

Criterios de Aceptación:
- [ ] Problema documentado mediante documento institucional o entrevista formal a usuario potencial.
- [ ] Verificación de que los datos requeridos son reales, accesibles y no sintéticos.
- [ ] Evaluación preliminar de viabilidad ética y legal favorable.
```

#### Historia 2: Inventario de Fuentes y Autorización (Punto G1)
* **Título:** `TG1-2: Inventariar fuentes de datos y obtener autorización de acceso (Punto G1)`
* **Etiqueta (Label):** `Dev-DataCustodian`
* **Responsable:** Tú mismo | **Sprint:** Arrastrar a **Sprint 1**
* **Descripción a pegar:**
```text
Como: Data Custodian
Quiero: Consolidar el inventario de fuentes de datos y recopilar la evidencia formal de acceso
Para: Asegurar la disponibilidad de datos reales cumpliendo la regla de no usar datos sintéticos

Criterios de Aceptación:
- [ ] Carta de autorización formal de la organización o licencia de repositorio abierto (datos.gov.co / UCI).
- [ ] Datos anonimizados sin exposición de información personal sensible.
- [ ] Aprobación formal del Punto de Control G1 ante el docente.
```

---

### HISTORIAS DEL SPRINT 2 (Informe - 25%)

#### Historia 3: Diseño Experimental y Formulación de Hipótesis
* **Título:** `TG1-3: Formular diseño experimental: pregunta analítica e hipótesis nula/alternativa`
* **Etiqueta (Label):** `Dev-DataConsumer`
* **Responsable:** Tú mismo | **Sprint:** Arrastrar a **Sprint 2**
* **Descripción a pegar:**
```text
Como: Data Consumer (Analítica y Estadística)
Quiero: Definir la pregunta analítica, hipótesis nula (H0) y alternativa (H1), variables y muestreo
Para: Guiar el modelado cuantitativo y establecer la métrica de éxito del MVP

Criterios de Aceptación:
- [ ] Pregunta analítica e hipótesis nula (H0) y alternativa (H1) claramente formuladas.
- [ ] Variables clasificadas: dependiente, independientes y de control.
- [ ] Técnica de muestreo, tamaño de muestra estimado y métrica cuantitativa de éxito del MVP.
```

#### Historia 4: Diccionario de Datos y Marco Ético (Ley 1581)
* **Título:** `TG1-4: Elaborar diccionario de datos y análisis de riesgos legales (Ley 1581)`
* **Etiqueta (Label):** `SM-DataSteward`
* **Responsable:** Tú mismo | **Sprint:** Arrastrar a **Sprint 2**
* **Descripción a pegar:**
```text
Como: Data Steward
Quiero: Construir el diccionario de metadatos y clasificar la sensibilidad bajo Ley 1581 de 2012
Para: Prevenir riesgos de sesgo algorítmico y garantizar el cumplimiento legal y ético

Criterios de Aceptación:
- [ ] Diccionario preliminar con variables, tipos de datos, rangos y descripciones.
- [ ] Clasificación de sensibilidad de los datos según la Ley 1581 de 2012.
- [ ] Matriz de riesgos de sesgo y medidas de mitigación para no afectar a las personas.
```

---

### HISTORIAS DEL SPRINT 3 (Anteproyecto - 75%)

#### Historia 5: Análisis Exploratorio (EDA) en Python
* **Título:** `TG1-5: Caracterizar muestra real en Python (Pandas/NumPy) y elaborar visualizaciones`
* **Etiqueta (Label):** `Dev-DataConsumer`
* **Responsable:** Tú mismo | **Sprint:** Arrastrar a **Sprint 3**
* **Descripción a pegar:**
```text
Como: Data Consumer (Analítica)
Quiero: Analizar la muestra de datos en Python para calcular estadísticos y detectar anomalías
Para: Conocer la distribución de las variables y preparar el plan de análisis de Trabajo de Grado 2

Criterios de Aceptación:
- [ ] Cuaderno de análisis exploratorio documentando volumen, nulos, duplicados y atípicos.
- [ ] Al menos cuatro visualizaciones analíticas con su respectiva interpretación.
```

#### Historia 6: Auditoría de Gobernanza de Datos por Roles
* **Título:** `TG1-6: Realizar ejercicio de auditoría de datos por roles y definir políticas`
* **Etiqueta (Label):** `SM-DataSteward`
* **Responsable:** Tú mismo | **Sprint:** Arrastrar a **Sprint 3**
* **Descripción a pegar:**
```text
Como: Equipo de Trabajo de Grado y Data Steward
Quiero: Auditar la calidad de los datos desde cada rol dual del equipo
Para: Consolidar una tabla de hallazgos con políticas de calidad, responsables y herramientas

Criterios de Aceptación:
- [ ] Auditoría individual realizada por cada rol (PO, SM, Custodian, Consumer).
- [ ] Tabla consolidada: problema detectado, política propuesta, responsable, plazo y herramienta.
```

#### Historia 7: Árbol de Problemas y Plan de Análisis Estadístico
* **Título:** `TG1-7: Estructurar matriz causa-efecto y plan de análisis estadístico`
* **Etiqueta (Label):** `PO-DataOwner`
* **Responsable:** Tú mismo | **Sprint:** Arrastrar a **Sprint 3**
* **Descripción a pegar:**
```text
Como: Product Owner
Quiero: Redactar el árbol causa-efecto del problema y formalizar las pruebas estadísticas
Para: Demostrar el impacto del proyecto y el rigor metodológico del experimento

Criterios de Aceptación:
- [ ] Matriz causa-efecto completa (problema, causas, efectos e impacto esperado).
- [ ] Plan estadístico: pruebas a aplicar, supuestos, nivel de significancia y criterios de decisión.
```

---

### HISTORIAS DEL SPRINT 4 (Anteproyecto - 75%)

#### Historia 8: Objetivos SMART y Estado del Arte
* **Título:** `TG1-8: Formular objetivos SMART y construir estado del arte con 15 referencias`
* **Etiqueta (Label):** `SM-DataSteward`
* **Responsable:** Tú mismo | **Sprint:** Arrastrar a **Sprint 4**
* **Descripción a pegar:**
```text
Como: Scrum Master / Data Steward
Quiero: Formular el objetivo general y los específicos y redactar el estado del arte
Para: Delimitar el alcance científico del proyecto sustentado en literatura académica indexada

Criterios de Aceptación:
- [ ] Objetivo general formulado con un solo verbo rector respondiendo Qué, Cómo y Para qué.
- [ ] Estado del arte con al menos 15 referencias bibliográficas recientes bajo norma APA 7.
```

#### Historia 9: Arquitectura de Datos y Procesamiento en Databricks
* **Título:** `TG1-9: Diseñar arquitectura de datos considerando procesamiento en Databricks`
* **Etiqueta (Label):** `Dev-DataCustodian`
* **Responsable:** Tú mismo | **Sprint:** Arrastrar a **Sprint 4**
* **Descripción a pegar:**
```text
Como: Data Custodian y arquitecto de datos
Quiero: Diseñar el diagrama de arquitectura comparando al menos dos alternativas tecnológicas
Para: Justificar el entorno de procesamiento en Databricks que se implementará en Trabajo de Grado 2

Criterios de Aceptación:
- [ ] Diagrama de arquitectura: fuentes, ingesta, almacenamiento, procesamiento y seguridad.
- [ ] Justificación técnica y económica comparando alternativas (AWS vs Azure).
```

---

### HISTORIAS DEL SPRINT 5 (Anteproyecto - 75%)

#### Historia 10: Metodología MLOps Nivel 1 y Definición del MVP
* **Título:** `TG1-10: Integrar esquema Scrum/CRISP-DM/MLOps Nivel 1 y definir alcance del MVP`
* **Etiqueta (Label):** `PO-DataOwner`
* **Responsable:** Tú mismo | **Sprint:** Arrastrar a **Sprint 5**
* **Descripción a pegar:**
```text
Como: Product Owner y equipo de investigación
Quiero: Definir el producto mínimo viable y el esquema integrador Scrum, CRISP-DM y MLOps
Para: Garantizar un modelo versionado en la nube y la entrega formal del anteproyecto

Criterios de Aceptación:
- [ ] Definición del MVP: funcionalidades mínimas, métricas de éxito y alcance excluido.
- [ ] Esquema integrador metodológico (Scrum + CRISP-DM + MLOps Nivel 1).
- [ ] Cronograma de 5 semanas para Trabajo de Grado 2 con responsables por rol.
- [ ] Anteproyecto en PDF bajo normas institucionales y carpeta compartida de evidencias.
```

---

## PASO 6: Iniciar el Sprint 1 y Mostrar el Tablero (Minuto 15 a 16)

* 🎬 **En pantalla:** En la cabecera de la caja de **`Sprint 1`**, haz clic en el botón azul **"Iniciar sprint"**.
* 🎬 **En pantalla:** En el modal que se abre:
  * **Duración:** Selecciona `1 semana`.
  * **Objetivo del sprint:** Escribe: *"Validar necesidad real, obtener autorización de fuentes (G1) y formalizar roles de gobernanza."*
* 🎬 **En pantalla:** Haz clic en **"Iniciar"**. Jira te llevará a la vista del **Tablero** (Board).
* 🎬 **En pantalla:** Toma la tarjeta `TG1-1` y arrástrala de la columna *Por hacer* a **"En curso"**.
* 🎙️ **Qué decir (Voz en off):**
  > *"Iniciamos formalmente el Sprint 1. Durante la semana el equipo mueve sus tareas a 'En curso', donde se aprecian con claridad los criterios de aceptación y la etiqueta del rol responsable."*

---

## PASO 7: Registro de la Retrospectiva de Sprint (Minuto 16 a 17)

* 🎬 **En pantalla:** En la barra superior, haz clic en el botón azul **"+ Crear"**.
* 🎬 **En pantalla:** Tipo de incidencia: **Tarea**. Resumen: `Retrospectiva y Revisión - Sprint 1`.
* 🎬 **En pantalla:** En la descripción, pega el siguiente registro formal y haz clic en **Crear**:
  ```text
  REGISTRO FORMAL DE SPRINT REVIEW & RETROSPECTIVE (Sprint 1)
  Fecha: [Fecha actual]
  Participantes: Todo el equipo

  1. Sprint Review (Qué se entregó):
  - Problema real documentado y validado con usuario potencial.
  - Carta de autorización de datos reales obtenida (Punto G1 superado).

  2. Sprint Retrospective (Evaluación del proceso):
  - ¿Qué funcionó bien?: Excelente coordinación en la delimitación del alcance.
  - ¿Qué se puede mejorar?: La gestión de permisos de datos tardó más de lo previsto.
  - Decisión de Mejora Accionable para Sprint 2:
    "El Data Steward enviará los lineamientos de la Ley 1581 con anticipación para acelerar la clasificación de variables en el diccionario de datos."
  ```
* 🎬 **En pantalla:** Mueve esta tarjeta a la columna **"Listo"** (Finalizado).
* 🎙️ **Qué decir (Voz en off):**
  > *"Un requisito indispensable de la rúbrica es registrar la revisión y la retrospectiva con una decisión de mejora accionable al cierre de cada sprint. De esta forma queda evidenciada la mejora continua del equipo."*

---

## PASO 8: Cierre del Video Tutorial (Minuto 17 a 18)

* 🎬 **En pantalla:** Muestra en pantalla completa el Tablero activo con las historias en sus columnas y la URL que se compartirá con el docente.
* 🎙️ **Qué decir (Voz en off final):**
  > *"Y de esta manera tan estructurada dejamos nuestro entorno de Jira 100% operativo: con el equipo y los roles duales formalizados, la plantilla Scrum oficial, los 5 sprints semanales organizados y las 10 historias técnicas reales de Ciencia de Datos listas para su ejecución y evaluación.*
  > 
  > *En el próximo video daremos el salto a Databricks Community Edition para configurar nuestro entorno de cómputo y comenzar a experimentar con algoritmos clásicos de Machine Learning y prueba de hipótesis. ¡Nos vemos en el siguiente tutorial!"*
