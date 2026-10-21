# Módulo 03: Analítica y Visualización en Big Data 📈📊

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Big%20Data-ea580c?style=for-the-badge&logo=apachespark&logoColor=white" alt="Big Data"/>
  <img src="https://img.shields.io/badge/Topics-Anal%C3%ADtica%20y%20Visualizaci%C3%B3n-0ea5e9?style=for-the-badge" alt="Topics"/>
  <img src="https://img.shields.io/badge/Course-Big%20Data-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al **Módulo 03** de la asignatura **Big Data** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**.

---

## 🧭 ¿De qué trata este módulo?

Este módulo **abre el Capítulo 2** del libro de la asignatura y corresponde a las secciones **2.1 (*Introducción*)**, **2.2 (*Resumen*)** y **2.3 (*Técnicas de analítica y visualización*)**: **2.3.1** aprendizaje automático, aprendizaje profundo y NLP; **2.3.2** herramientas de visualización (Tableau, Power BI y D3.js); y **2.3.3** *storytelling* con datos. El Capítulo 1 respondió *qué es el Big Data y dónde se guarda y procesa*; este módulo responde **¿cómo cambian la analítica y la visualización cuando los datos son masivos?** Los módulos **04** (seguridad y gobernanza) y **05** (avances y tendencias) completan el capítulo.

El módulo **no** repite lo que ya existe en el repositorio, lo **enlaza**: *Spark* en detalle (arquitectura, ETL, MLlib, *streaming*) está en [Data Mining, Módulo 07](../../Data%20Mining/07%20-%20Mineria%20de%20Datos%20con%20Big%20Data/README.md); las herramientas de visualización y el diseño de gráficos, en [Visual Analytics, Módulo 02](../../Visual%20Analytics%20and%20Critical%20Thinking/02%20-%20Fundamentos%20de%20Visualizacion/02_Herramientas_Tableau_PowerBI_D3.ipynb) y [Módulo 01](../../Visual%20Analytics%20and%20Critical%20Thinking/01%20-%20Introduccion%20al%20Analisis%20Visual/03_Mejores_Practicas_Diseno_Visualizaciones_Efectivas.ipynb); los algoritmos de ML, en [Machine Learning](../../Machine%20Learning/README.md). Aquí el enfoque es **la escala**: algoritmos aproximados **escritos desde cero**, aprendizaje fuera de memoria y distribuido (con *PySpark* local **ejecutado de verdad**), paralelismo de datos en NumPy, agregar antes de graficar y contar con honestidad. Como en el resto del repositorio, todo se **verifica con `assert`**, con **semillas fijas** y **resultados reportados con honestidad** (incluidos los casos en que *Spark* **no** gana en una sola máquina o un resumen no responde una pregunta).

> 🗺️ **Mapa del curso (seis módulos):** **00** Fundamentos → **01** Procesamiento y Almacenamiento → **02** *Data Warehousing* y *Data Lake* → **03** Analítica y Visualización *(este módulo, abre el Capítulo 2)* → **04** Seguridad y Gobernanza → **05** Avances y Tendencias. El [README del curso](../README.md) se actualizará con el índice completo.

> 🛠️ **Ponlo en práctica:** todos los cuadernos (estándar y *Para Dummies*) incluyen secciones **«🛠️ Práctica»**: una celda de código para que escribas tu solución y, justo debajo, la **solución guiada desplegable** (`💡 Haz clic aquí para ver la solución guiada...`). Inténtalo primero y abre la solución solo para comparar.

---

## 📚 Estructura Curricular del Módulo

### 🎓 1. Cuadernos Académicos Estándar:
1. [**00_Introduccion_Cap2_y_Resumen.ipynb**](00_Introduccion_Cap2_y_Resumen.ipynb): *Secciones 2.1 y 2.2.* El **mapa del Capítulo 2** y de los módulos 03-05 (dibujado con `matplotlib`); los **cuatro niveles de analítica** (descriptiva, diagnóstica, predictiva, prescriptiva) **ejecutados sobre un mismo conjunto de datos sintético** (tres sedes de una tienda ficticia, con un competidor que golpea los días sin promoción: la diagnóstica lo encuentra, el pronóstico a un día con *gradient boosting* baja el error medio de ≈ 31.2 a ≈ 16.9 kg/día frente a la línea base ingenua y la decisión óptima de cuánto pedir —cuantil crítico— reduce el costo ≈ 16 %). **Cómo escalar la analítica:** error de muestreo $\propto 1/\sqrt{n}$ verificado (pendiente log-log −0.502), **muestreo de reservorio**, ***Count-Min Sketch*** (nunca subestima; ninguna clave supera la cota $\varepsilon N$) y ***HyperLogLog*** simplificado (desviación típica del error 0.0164 frente a 0.0163 de la teoría, con 4 KiB), todos **desde cero** con `assert` de su garantía, y el contraste con `approx_count_distinct` de *Spark* (en esta máquina y tamaño el conteo exacto fue **más rápido**). 2 prácticas (el pedido óptimo si el costo cambia; dimensionar un *Count-Min Sketch*).
2. [**01_Tecnicas_de_Analitica_ML_DL_NLP.ipynb**](01_Tecnicas_de_Analitica_ML_DL_NLP.ipynb): *Sección 2.3.1.* **ML a escala:** `SGDClassifier.partial_fit` por trozos sobre un CSV de 120 000 filas generado por trozos (exactitud 0.7285 frente a 0.7288 del ajuste completo y el techo teórico 0.7298, con ≈ 5 veces menos memoria; **la tasa por defecto cae a 0.665** y **un archivo ordenado por clase a 0.503**); un ***pipeline* de *Spark MLlib*** (`VectorAssembler`, `StandardScaler`, `LogisticRegression`) ejecutado y comparado con *scikit-learn* (**mismos coeficientes, coseno 1.000000, y *Spark* mucho más lento en una sola máquina**). **Aprendizaje profundo:** **SGD con paralelismo de datos desde cero en NumPy** (retropropagación a mano verificada con diferencias finitas; el gradiente combinado de $K$ trabajadores coincide con el del lote completo y **el promedio simple con fragmentos desiguales no**; $K=1$ y $K=4$ dan los mismos parámetros), una `MLPClassifier` (0.938 donde un modelo lineal acierta 0.481), un modelo de costo ilustrativo y una tabla de **GPU y entrenamiento distribuido**. **NLP a escala:** TF-IDF, el **truco del *hashing*** frente a un vocabulario explícito (colisiones medidas: MurmurHash3 sigue la teoría de ocupación, `crc32` no) y un *pipeline* de *Spark* con `Tokenizer`, `HashingTF` e `IDF` (corpus **sintético** en español). 2 prácticas (media y varianza exactas por trozos; tu propio `HashingTF`).
3. [**02_Herramientas_de_Visualizacion_Tableau_PowerBI_D3.ipynb**](02_Herramientas_de_Visualizacion_Tableau_PowerBI_D3.ipynb): *Sección 2.3.2.* **Por qué visualizar a escala es distinto:** sobredibujo cuantificado (74.6 % de los 400 000 puntos cae en celdas con más de 50 puntos), histograma 2D, *hexbin*, **decimación min-máx** (conserva un pico de 1 muestra que una muestra uniforme pierde) y **muestreo estratificado con pesos**. **Tableau y Power BI frente a datos masivos (solo conceptual; lo incierto, marcado «verificar»):** extracto frente a conexión directa, importación frente a `DirectQuery`, modelos compuestos y **agregaciones precalculadas**, **simulado con *pandas*** (consultas ≈ 10 veces más rápidas con resultados idénticos; y lo que una agregación **no** puede responder: clientes distintos y medianas). **D3.js:** enlace de datos (*enter/update/exit*) y escalas **implementadas en Python** (con *ticks*, `nice`, `scaleBand`, `scaleSqrt`) y **exportación de agregados** a JSON/CSV con metadatos (≈ 100 veces más pequeños que el detalle; **no** se ejecutó la página de D3), más una **tabla guía** de cuándo usar cada herramienta. 2 prácticas (histograma 2D con `bincount`; qué responde una tabla agregada).
4. [**03_Storytelling_con_Datos.ipynb**](03_Storytelling_con_Datos.ipynb): *Sección 2.3.3.* **Estructura narrativa** (contexto-conflicto-resolución y contexto-foco-acción); **rediseño antes/después** de un gráfico; una **historia de tres figuras** y su **guion** sobre un caso de negocio **sintético** (*AgroCanasta*, empresa ficticia: los pedidos se multiplican por 2.2 pero el margen por pedido de Sogamoso se vuelve negativo; un pedido mínimo, con **supuestos declarados y análisis de sensibilidad**, lo corrige); **errores éticos cuantificados** (eje truncado: factor de mentira 10.1 frente a 1.00; ventana a conveniencia: con una serie sin tendencia, 7 ventanas suben y 12 bajan); y una **lista de verificación con auditoría automática** de figuras (el rediseño pasa de 2/8 a 8/8; se aclara que **no** juzga si el mensaje es verdadero). 2 prácticas (un título generado desde los datos; el factor de mentira).

---

### 📝 2. Taller Práctico Evaluativo (*Hands-On*):
* [**../homeworks/03_Analitica_Visualizacion_Hands_On.ipynb**](../homeworks/03_Analitica_Visualizacion_Hands_On.ipynb): Taller evaluativo que integra analítica a escala, visualización y *storytelling* en ejercicios prácticos *(el cuaderno se publica aparte)*.

---

### 🧸 3. Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/). Sin jerga ni fórmulas, con analogías cotidianas; **no requieren *Spark* ni Java**:
1. [**00_Introduccion_Cap2_Dummies.ipynb**](Para%20Dummies/00_Introduccion_Cap2_Dummies.ipynb): **Don Álvaro y sus cuatro preguntas**: qué pasó, por qué, qué pasará y cuánto pedir (95 kg y no 97, porque sobrar sale más caro), **preguntar a pocos para conocer a muchos** (100 veces más encuestados bajan el error unas 10 veces) y **la rifa justa** cuando no se sabe cuántos llegan.
2. [**01_Tecnicas_Analitica_Dummies.ipynb**](Para%20Dummies/01_Tecnicas_Analitica_Dummies.ipynb): **Estudiar por capítulos** (y la trampa del orden), **cuatro ayudantes cuentan votos** (promediar porcentajes sin pesar da ≈ 59 % cuando lo correcto es ≈ 46.5 %) y **el archivador de cajones** (el truco del *hashing*).
3. [**02_Herramientas_Visualizacion_Dummies.ipynb**](Para%20Dummies/02_Herramientas_Visualizacion_Dummies.ipynb): **Un alfiler por casa** frente a **contar por manzana**, **el libro de caja del mes** (lo que se suma y lo que no: 4 ≠ 3 clientes distintos) y **la regla que convierte litros en centímetros** (las escalas).
4. [**03_Storytelling_Dummies.ipynb**](Para%20Dummies/03_Storytelling_Dummies.ipynb): **La panadería de Doña Rosa** (de explorar a explicar), **la regla torcida** (una diferencia de 2 pasteles que parece el doble) y **escoger los meses que convienen**.

---

## 💾 Datos Utilizados

Todos los datos son **sintéticos con semilla fija, generados por código dentro de cada cuaderno**; **no hay descargas** y **no se necesita ninguna carpeta `data/`** (los archivos que se escriben —un CSV de 120 000 filas, JSON/CSV de agregados, una página de D3— se crean en un **directorio temporal** que se borra al cerrar el núcleo; la sesión de *Spark* también escribe ahí y se detiene al terminar cada sección).

| Conjunto | Origen | Dónde se usa |
|---|---|---|
| **Ventas de tomate** de una tienda ficticia (3 sedes × 730 días, con competidor en Sogamoso desde el día 640) | `generar_ventas(semilla=42)` | Cuaderno 00 (cuatro niveles) |
| **Montos** (población lognormal de 1 millón), **flujo de 500 000 montos** y **flujo Zipf de 300 000 términos** | `default_rng(42)` | Cuaderno 00 (muestreo, reservorio, *Count-Min*, *HyperLogLog*) |
| **CSV de clasificación** (120 000 filas × 20 variables, etiquetas logísticas con pesos conocidos) | `generar_trozo` (por trozos de 20 000) | Cuaderno 01 (`partial_fit`, MLlib, Práctica 1) |
| **Datos circulares no lineales** (20 000 × 6) | `default_rng(42)` | Cuaderno 01 (red en NumPy, `MLPClassifier`) |
| **Corpus de 6 000 «documentos» en español**, cuatro temas, con cola larga de términos raros | `generar_corpus` (**sintético**, no es lenguaje natural real) | Cuaderno 01 (TF-IDF, *hashing*, *Spark* NLP) |
| **Viajes** (400 000 puntos con zonas densas y una categoría rara) y **serie de sensor** (1 millón de muestras con un pico) | `default_rng(42)` | Cuaderno 02 |
| **500 000 transacciones** (6 regiones, 120 000 clientes) | `default_rng(42)` | Cuaderno 02 (agregaciones) |
| **AgroCanasta** (≈ 37 000 pedidos de 24 meses en 3 ciudades) y **serie de entregas a tiempo** | `generar_pedidos`, `default_rng(7)` | Cuaderno 03 |
| **Mini-ejemplos de juguete** (kilos de tomate, papeletas, 40 frutas y verduras, 20 000 casas, ventas de la panadería) | Listas y generadores pequeños | Los cuatro *Dummies* |

> ⚠️ **Los datos son inventados** (empresas, cifras y nombres): los resultados describen el **mecanismo**, **no** el rendimiento esperable en un caso real. Los nombres de municipios de Boyacá solo ambientan los ejemplos. Los **supuestos de las simulaciones** (p. ej. qué hacen los clientes ante un pedido mínimo, o los parámetros del modelo de costo del entrenamiento distribuido) son **ilustrativos, no medidos**, y están declarados donde se usan.

## ⚙️ Requisitos

`numpy`, `pandas`, `matplotlib` y `scikit-learn` (preinstalados en Google Colab). Los **cuadernos 00 y 01** usan además **`pyspark`** (en Colab: `!pip install -q pyspark`, línea ya incluida y comentada en la primera celda) y **Java**; si no están disponibles, las celdas de *Spark* **se omiten con un aviso** y el resto del cuaderno sigue (todo se implementa también desde cero en Python). Los cuadernos 02 y 03 y los cuatro **Dummies** usan solo `NumPy`, `pandas`, `matplotlib` (y `scikit-learn` en un *Dummies*) y **no necesitan *Spark*, Java ni red**. **No se usan *PyTorch* ni *TensorFlow***: el aprendizaje profundo se trata con NumPy y `MLPClassifier`.

## 🎬 Video Tutorial Recomendado

* 📊 **Instalación y Configuración de Power BI**: [Ver en YouTube](https://youtu.be/8RifWTEWBOI)
  > Tutorial técnico paso a paso para la descarga, instalación y configuración inicial de Microsoft Power BI Desktop para la analítica visual y dashboards en Big Data.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Asignatura: Big Data</i>
  </p>
</div>
