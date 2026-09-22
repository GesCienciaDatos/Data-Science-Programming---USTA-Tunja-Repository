#!/usr/bin/env python3
"""
update_catalog.py
Script de automatización multi-materia para escanear y sincronizar Guias, Contenido, 
Cuadernos y Datasets por asignatura con el catálogo JavaScript del Laboratorio Virtual 
(docs/assets/js/catalog.js).
"""

import os
import sys
import shutil
import json
import re
import csv
import urllib.parse
from pathlib import Path

# Configurar stdout en UTF-8 para entornos Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
CATALOG_JS_PATH = DOCS_DIR / "assets" / "js" / "catalog.js"
FRONTEND_CATALOG_PATH = BASE_DIR / "frontend" / "src" / "data" / "catalog.js"

REPO_OWNER = "sazuniga06"
REPO_NAME = "Data-Science-Programming---USTA-Tunja-Repository"
BRANCH = "main"

COURSE_DEFINITIONS = [
    {
        "id": "data-science-programming",
        "name": "Data Science Programming",
        "title": "Programación para Ciencia de Datos",
        "folder": "Data Science programming",
        "icon": "🐍",
        "badge": "Activo / Disponible",
        "badge_color": "emerald",
        "color": "#38bdf8",
        "gradient": "from-sky-500/20 via-blue-600/10 to-transparent",
        "border_glow": "border-sky-500/40",
        "description": "Pensamiento computacional avanzado, NumPy, Pandas, Análisis Exploratorio de Datos (EDA), Limpieza e Imputación, Feature Engineering regularizado y Modelos de Regresión supervisados.",
        "level": "Especialización",
        "semester": "Semestre I",
        "active": True
    },
    {
        "id": "estadistica-analisis",
        "name": "Estadística, Análisis y Representación de Datos",
        "title": "Modelamiento Estadístico e Inferencia",
        "folder": "Estadistica analisis y representacion de datos",
        "icon": "📊",
        "badge": "En Construcción",
        "badge_color": "amber",
        "color": "#f59e0b",
        "gradient": "from-amber-500/20 via-yellow-600/10 to-transparent",
        "border_glow": "border-amber-500/40",
        "description": "Modelamiento probabilístico, inferencia estadística rigurosa, pruebas de hipótesis paramétricas y no paramétricas, análisis multivariado y técnicas avanzadas de representación.",
        "level": "Especialización",
        "semester": "Semestre I",
        "active": False
    },
    {
        "id": "adquisicion-gobernanza",
        "name": "Adquisición, Gestión y Gobernanza de Datos",
        "title": "Arquitectura, Calidad y Gestión de Datos",
        "folder": "Adquision gestion y gobernanza de datos",
        "icon": "🗄️",
        "badge": "En Construcción",
        "badge_color": "purple",
        "color": "#a855f7",
        "gradient": "from-purple-500/20 via-indigo-600/10 to-transparent",
        "border_glow": "border-purple-500/40",
        "description": "Ingeniería de pipelines ETL/ELT, arquitectura de bases de datos relacionales y NoSQL, calidad del dato, catálogos de metadatos y marcos de gobernanza DAMA-DMBOK.",
        "level": "Especialización",
        "semester": "Semestre I",
        "active": False
    },
    {
        "id": "privacidad-seguridad",
        "name": "Privacidad, Seguridad e Integridad de los Datos",
        "title": "Ciberseguridad y Ética en Datos",
        "folder": "Privacidad, Seguridad e Integridad de los datos",
        "icon": "🛡️",
        "badge": "En Construcción",
        "badge_color": "cyan",
        "color": "#06b6d4",
        "gradient": "from-cyan-500/20 via-teal-600/10 to-transparent",
        "border_glow": "border-cyan-500/40",
        "description": "Ciberseguridad analítica, anonimización y privacidad diferencial, criptografía aplicada a datos en reposo y tránsito, y cumplimiento normativo (Habeas Data / GDPR).",
        "level": "Especialización",
        "semester": "Semestre I",
        "active": False
    },
    {
        "id": "data-mining",
        "name": "Data Mining",
        "title": "Minería de Datos y Descubrimiento de Patrones",
        "folder": "Data Mining",
        "icon": "⛏️",
        "badge": "Activo / Disponible",
        "badge_color": "emerald",
        "color": "#f43f5e",
        "gradient": "from-rose-500/20 via-pink-600/10 to-transparent",
        "border_glow": "border-rose-500/40",
        "description": "Fundamentos de Scikit-Learn, preprocesamiento avanzado, pipelines, validación cruzada, optimización y descubrimiento de patrones en bases de datos.",
        "level": "Especialización",
        "semester": "Semestre II",
        "active": True
    },
    {
        "id": "machine-learning",
        "name": "Machine Learning",
        "title": "Aprendizaje Automático Supervisado y No Supervisado",
        "folder": "Machine Learning",
        "icon": "🧠",
        "badge": "Biblioteca Activa",
        "badge_color": "violet",
        "color": "#8b5cf6",
        "gradient": "from-violet-500/20 via-purple-600/10 to-transparent",
        "border_glow": "border-violet-500/40",
        "description": "Algoritmos de clasificación supervisada, ensambles avanzados (Random Forest, XGBoost, LightGBM, CatBoost), clustering no supervisado y optimización de hiperparámetros.",
        "level": "Especialización",
        "semester": "Semestre II",
        "active": True
    },
    {
        "id": "big-data",
        "name": "Big Data",
        "title": "Procesamiento Distribuido y Masivo",
        "folder": "Big Data",
        "icon": "⚡",
        "badge": "En Construcción",
        "badge_color": "amber",
        "color": "#f59e0b",
        "gradient": "from-amber-500/20 via-orange-600/10 to-transparent",
        "border_glow": "border-amber-500/40",
        "description": "Computación distribuida con Apache Spark, PySpark, DuckDB, streaming en tiempo real con Kafka, arquitectura Lakehouse y almacenamiento optimizado en la nube.",
        "level": "Especialización",
        "semester": "Semestre II",
        "active": False
    },
    {
        "id": "introduccion-ia",
        "name": "Introducción a la Inteligencia Artificial",
        "title": "Fundamentos de IA, Búsqueda y Agentes de Conocimiento",
        "folder": "Introduccion a la Inteligencia Artificial",
        "icon": "🤖",
        "badge": "Activo / Disponible",
        "badge_color": "emerald",
        "color": "#ec4899",
        "gradient": "from-pink-500/20 via-rose-600/10 to-transparent",
        "border_glow": "border-pink-500/40",
        "description": "Fundamentos y evolución histórica de la IA, problemas aptos y disciplinas convergentes, taxonomía de ramas, consideraciones éticas, convergencia IA/ML/DL y GenAI, algoritmos de búsqueda (DFS, BFS, GBFS, A*) y agentes basados en conocimiento con lógica proposicional.",
        "level": "Especialización",
        "semester": "Semestre II",
        "active": True
    },
    {
        "id": "visual-analytics",
        "name": "Visual Analytics and Critical Thinking",
        "title": "Analítica Visual, Storytelling y Power Query",
        "folder": "Visual Analytics and Critical Thinking",
        "icon": "📊",
        "badge": "Activo / Disponible",
        "badge_color": "emerald",
        "color": "#10b981",
        "gradient": "from-emerald-500/20 via-teal-600/10 to-transparent",
        "border_glow": "border-emerald-500/40",
        "description": "Analítica visual interactiva (Python ↔ Power BI ↔ Tableau), narrativa con datos (Data Storytelling), diseño perceptual, sesgos cognitivos y transformaciones ETL con Power Query.",
        "level": "Especialización",
        "semester": "Semestre II",
        "active": True
    }
]

DEFAULT_MODULES_DSP = [
    {
        "id": "01",
        "name": "01 - Python",
        "title": "Fundamentos de Programación en Python",
        "icon": "🐍",
        "color": "#3776AB",
        "description": "Pensamiento algorítmico, tipos primitivos, colecciones, control de flujo, funciones, POO y modularización."
    },
    {
        "id": "02",
        "name": "02 - Numpy",
        "title": "Computación Científica con NumPy",
        "icon": "🔢",
        "color": "#013243",
        "description": "Arreglos ndarray, operaciones vectorizadas, funciones universales (ufuncs), indexación, slicing y broadcasting."
    },
    {
        "id": "03",
        "name": "03 - Pandas",
        "title": "Manipulación Tabular con Pandas",
        "icon": "🐼",
        "color": "#150458",
        "description": "Series, DataFrames, operaciones de entrada/salida, transformaciones, agregaciones con groupby y merge/join."
    },
    {
        "id": "04",
        "name": "04 - EDA",
        "title": "Análisis Exploratorio de Datos (EDA)",
        "icon": "📊",
        "color": "#388E3C",
        "description": "Estadística descriptiva, cuarteto de Anscombe, visualización univariada y bivariada con Matplotlib y Seaborn."
    },
    {
        "id": "05",
        "name": "05 - Data Preparation",
        "title": "Limpieza y Preparación de Datos",
        "icon": "🧹",
        "color": "#D97706",
        "description": "Imputación de nulos (MCAR/MAR/MNAR), escalado de variables, parseo de fechas y fuzzy matching tipográfico."
    },
    {
        "id": "06",
        "name": "06 - Feature Engineering",
        "title": "Ingeniería de Características",
        "icon": "⚙️",
        "color": "#7C3AED",
        "description": "Codificación categórica, Target Encoding con suavizado, ratios, transformaciones grupales, PCA e Información Mutua."
    },
    {
        "id": "07",
        "name": "07 - Regression",
        "title": "Modelos de Regresión y Aprendizaje Supervisado",
        "icon": "📈",
        "color": "#0284C7",
        "description": "Regresión OLS, supuestos de Gauss-Markov, Regresión Polinomial, Ridge, Lasso, ElasticNet, CV y k-NN Regressor."
    },
    {
        "id": "08",
        "name": "08 - Classification",
        "title": "Modelos de Clasificación y Evaluación Supervisada",
        "icon": "🎯",
        "color": "#EC4899",
        "description": "Regresión Logística binaria y multiclase, Fronteras de Decisión, Métricas (ROC, AUC, F1), Regularización y k-NN Classifier."
    },
    {
        "id": "09",
        "name": "09 - Decision Trees",
        "title": "Árboles de Decisión y Métodos de Ensamble",
        "icon": "🌲",
        "color": "#10B981",
        "description": "Modelos CART, Criterios de Gini y Entropía, Poda Cost-Complexity, Bagging, Random Forests y Gradient Boosting."
    },
    {
        "id": "10",
        "name": "10 - Clustering",
        "title": "Clustering y Aprendizaje No Supervisado",
        "icon": "🔮",
        "color": "#8B5CF6",
        "description": "Agrupamiento no supervisado, métricas de distancia, K-Means, K-Means++, Clustering Jerárquico Aglomerativo, Dendrogramas, DBSCAN y Métricas de Silueta."
    },
    {
        "id": "11",
        "name": "11 - Polars",
        "title": "Procesamiento de Datos de Alto Rendimiento con Polars",
        "icon": "⚡",
        "color": "#06b6d4",
        "description": "Procesamiento analítico columnar de alto rendimiento en Rust/Python, evaluación perezosa (lazy evaluation) y optimización de memoria."
    },
    {
        "id": "hw",
        "name": "homeworks",
        "title": "Talleres Prácticos Evaluativos (Hands-On)",
        "icon": "📝",
        "color": "#DC2626",
        "description": "Talleres integradores de resolución autónoma con datos reales y desafíos de negocio."
    }
]

MODULES_DATA_MINING = [
    {
        "id": "00",
        "name": "00 - Introduccion al Data Mining",
        "title": "Introducción a la Minería de Datos y CRISP-DM",
        "icon": "⛏️",
        "color": "#f43f5e",
        "description": "Ciclo de vida metodológico (CRISP-DM, KDD), taxonomía de tareas analíticas y auditoría de calidad de datos en entornos empresariales."
    },
    {
        "id": "01",
        "name": "01 - Preprocesamiento de los Datos",
        "title": "Preprocesamiento y Calidad del Dato",
        "icon": "🧹",
        "color": "#d97706",
        "description": "Tratamiento de valores faltantes, detección y manejo de anomalías/outliers, transformaciones de potencia y escalamiento."
    },
    {
        "id": "02",
        "name": "02 - Clasificacion y Regresion",
        "title": "Modelos Predictivos: Clasificación y Regresión",
        "icon": "🎯",
        "color": "#0284c7",
        "description": "Regresión logística binaria y multiclase, Naive Bayes, k-NN, regresión lineal regularizada y matrices de confusión."
    },
    {
        "id": "03",
        "name": "03 - Clustering y Mineria Reglas de Asociacion",
        "title": "Clustering y Reglas de Asociación (Apriori)",
        "icon": "🔮",
        "color": "#8b5cf6",
        "description": "Agrupamiento con K-Means y DBSCAN, segmentación de clientes, minería de patrones frecuentes y reglas de asociación con métricas Support/Confidence/Lift."
    },
    {
        "id": "04",
        "name": "04 - Arboles de Decision y Bosques Aleatorios",
        "title": "Árboles de Decisión y Bosques Aleatorios",
        "icon": "🌲",
        "color": "#10b981",
        "description": "Algoritmos CART, criterios de impureza Gini y Entropía, ensambles homogéneos por Bagging y bosques aleatorios."
    },
    {
        "id": "05",
        "name": "05 - Comparacion de Arboles de Decision y Bosques Aleatorios",
        "title": "Benchmark y Comparativa de Modelos de Ensamble",
        "icon": "⚖️",
        "color": "#ec4899",
        "description": "Análisis comparativo de sesgo vs varianza, sobreajuste, curvas de aprendizaje, calibración de probabilidades e interpretabilidad."
    },
    {
        "id": "06",
        "name": "06 - Maquinas de Soporte Vectorial y Redes Neuronales",
        "title": "Máquinas de Soporte Vectorial (SVM) y Redes Neuronales",
        "icon": "🧠",
        "color": "#6366f1",
        "description": "Hiperplanos de margen máximo, kernel trick (RBF, polinomial), arquitectura del perceptrón multicapa (MLP) y backpropagation."
    },
    {
        "id": "07",
        "name": "07 - Mineria de Datos con Big Data",
        "title": "Minería de Datos Distribuida con Big Data",
        "icon": "⚡",
        "color": "#f59e0b",
        "description": "Computación paralela a gran escala con Apache Spark y PySpark MLlib, pipelines distribuidos y análisis de flujos masivos."
    },
    {
        "id": "hw",
        "name": "homeworks",
        "title": "Talleres Prácticos Evaluativos (Hands-On)",
        "icon": "📝",
        "color": "#dc2626",
        "description": "Desafíos autónomos con datasets reales de riesgo crediticio, fraude financiero y retención de clientes."
    }
]

MODULES_IA = [
    {
        "id": "00",
        "name": "00 - Fundamentos y Origenes de la IA",
        "title": "Fundamentos y Orígenes de la Inteligencia Artificial",
        "icon": "🧠",
        "color": "#6366f1",
        "description": "Definición formal de IA (Russell & Norvig), hitos históricos desde Dartmouth hasta la era del Deep Learning, inviernos de la IA y el Test de Turing."
    },
    {
        "id": "01",
        "name": "01 - Problemas Disciplinas y Aplicaciones de la IA",
        "title": "Problemas, Disciplinas y Aplicaciones de la IA",
        "icon": "🎯",
        "color": "#0ea5e9",
        "description": "Caracterización de problemas aptos para IA, disciplinas convergentes, la IA como tecnología de propósito general (GPT) y casos sectoriales."
    },
    {
        "id": "02",
        "name": "02 - Taxonomia de la Inteligencia Artificial",
        "title": "Taxonomía de la Inteligencia Artificial",
        "icon": "🌳",
        "color": "#8b5cf6",
        "description": "Ramas de la IA, tipos por capacidad (ANI, AGI, ASI), clasificación funcional de Hintze y el General Problem Solver (GPS) de Newell & Simon."
    },
    {
        "id": "03",
        "name": "03 - Etica y el Nuevo Paradigma de la IA",
        "title": "Ética, Paradigmas Contemporáneos y GenAI",
        "icon": "⚖️",
        "color": "#ec4899",
        "description": "Consideraciones éticas, sesgos y explicabilidad, el marco IA ⊃ Machine Learning ⊃ Deep Learning y fundamentos de la IA Generativa."
    },
    {
        "id": "04",
        "name": "04 - Algoritmos de Busqueda",
        "title": "Algoritmos de Búsqueda y Espacios de Estados",
        "icon": "🔍",
        "color": "#10b981",
        "description": "Búsqueda no informada (DFS, BFS), búsqueda informada con heurísticas (Greedy Best-First Search) y el algoritmo A* óptimo aplicado a sistemas de archivos."
    },
    {
        "id": "05",
        "name": "05 - Agentes Basados en Conocimiento",
        "title": "Agentes Basados en Conocimiento y Lógica",
        "icon": "💡",
        "color": "#f59e0b",
        "description": "Lógica proposicional, sintaxis y semántica, model-checking, bases de conocimiento en Python, Forma Normal Conjuntiva (CNF) y resolución."
    },
    {
        "id": "hw",
        "name": "homeworks",
        "title": "Talleres Prácticos Evaluativos (Hands-On)",
        "icon": "📝",
        "color": "#dc2626",
        "description": "Retos prácticos integradores con edición estándar y Para Dummies cubriendo búsqueda heurística, deducción lógica y taxonomía de IA."
    }
]

MODULES_VISUAL_ANALYTICS = [
    {
        "id": "01",
        "name": "01 - Introduccion al Analisis Visual",
        "title": "Introducción a la Analítica Visual",
        "icon": "👁️",
        "color": "#06b6d4",
        "description": "Definición, pipeline de analítica visual, evolución histórica y el triángulo tecnológico interactivo Python ↔ Power BI ↔ Tableau."
    },
    {
        "id": "02",
        "name": "02 - Fundamentos de Visualizacion",
        "title": "Fundamentos y Percepción Visual",
        "icon": "📐",
        "color": "#10b981",
        "description": "Gramática de los gráficos de Leland Wilkinson, codificación visual por canales de Bertin y principios de diseño y data-ink ratio de Edward Tufte."
    },
    {
        "id": "03",
        "name": "03 - Pensamiento Critico en Datos",
        "title": "Pensamiento Crítico y Sesgos Cognitivos",
        "icon": "🤔",
        "color": "#f59e0b",
        "description": "Falacias gráficas, detección de visualizaciones engañosas, paradoja de Simpson, falacia ecológica y correlación versus causalidad."
    },
    {
        "id": "04",
        "name": "04 - Visualizacion de Datos Categoricos",
        "title": "Visualización de Variables Categóricas",
        "icon": "📊",
        "color": "#8b5cf6",
        "description": "Gráficos de barras ordenadas, diagramas de Pareto, treemaps, waffle charts y representación jerárquica de composiciones discretas."
    },
    {
        "id": "05",
        "name": "05 - Visualizacion de Datos Numericos",
        "title": "Visualización de Variables Numéricas y Continuas",
        "icon": "📈",
        "color": "#3b82f6",
        "description": "Distribuciones univariadas y bivariadas: histogramas, KDE, boxplots, diagramas de violín, scatter plots y matrices de correlación."
    },
    {
        "id": "06",
        "name": "06 - Visualizacion Avanzada",
        "title": "Visualización Avanzada y Tableros Analíticos",
        "icon": "🚀",
        "color": "#ec4899",
        "description": "Creación de dashboards interactivos con Plotly, Dash y Streamlit, mapas geoespaciales coropléticos y Data Storytelling estratégico."
    },
    {
        "id": "07",
        "name": "07 - Casos de Estudio",
        "title": "Casos de Estudio Aplicados",
        "icon": "💼",
        "color": "#14b8a6",
        "description": "Proyectos analíticos integrales de negocio: métricas de ventas comerciales, analítica en salud pública y flujos urbanos."
    },
    {
        "id": "08",
        "name": "Power Query",
        "title": "Transformación ETL con Power Query & Lenguaje M",
        "icon": "⚡",
        "color": "#eab308",
        "description": "Automatización de transformaciones de datos, fórmulas en lenguaje M, preparación de tablas y comparativa metodológica con Pandas."
    }
]

COURSE_MODULE_DEFAULTS = {
    "data-science-programming": DEFAULT_MODULES_DSP,
    "data-mining": MODULES_DATA_MINING,
    "introduccion-ia": MODULES_IA,
    "visual-analytics": MODULES_VISUAL_ANALYTICS,
}

PALETTE = [
    {"icon": "🐍", "color": "#3776AB"},
    {"icon": "🔢", "color": "#013243"},
    {"icon": "🐼", "color": "#150458"},
    {"icon": "📊", "color": "#388E3C"},
    {"icon": "🧹", "color": "#D97706"},
    {"icon": "⚙️", "color": "#7C3AED"},
    {"icon": "📈", "color": "#0284C7"},
    {"icon": "🧠", "color": "#8B5CF6"},
    {"icon": "🤖", "color": "#EC4899"},
    {"icon": "🌐", "color": "#14B8A6"}
]

KNOWN_TITLES = {
    "Instalacion Python_compressed.mp4": "Instalación y Configuración de Python",
    "Instalacion Python.mp4": "Instalación y Configuración de Python",
    "Creacion de Venv.mp4": "Creación y Gestión de Entornos Virtuales (VENV)",
    "Creacion_Venv.mp4": "Creación y Gestión de Entornos Virtuales (VENV)",
    "Instalacion_Python.pdf": "Guía de Instalación y Configuración de Python",
    "Instalación_Python.pdf": "Guía de Instalación y Configuración de Python",
    "Creacion_VENV.pdf": "Guía de Creación de Entornos Virtuales (VENV)"
}

KNOWN_YOUTUBE_VIDEOS = {
    "instalacion python_compressed.mp4": {
        "youtube_id": "4GN9WlumZ7o",
        "youtube_url": "https://youtu.be/4GN9WlumZ7o",
        "embed_url": "https://www.youtube.com/embed/4GN9WlumZ7o",
        "thumbnail": "https://img.youtube.com/vi/4GN9WlumZ7o/hqdefault.jpg"
    },
    "instalacion python.mp4": {
        "youtube_id": "4GN9WlumZ7o",
        "youtube_url": "https://youtu.be/4GN9WlumZ7o",
        "embed_url": "https://www.youtube.com/embed/4GN9WlumZ7o",
        "thumbnail": "https://img.youtube.com/vi/4GN9WlumZ7o/hqdefault.jpg"
    },
    "creacion_venv.mp4": {
        "youtube_id": "GX0rf6HjdcU",
        "youtube_url": "https://youtu.be/GX0rf6HjdcU",
        "embed_url": "https://www.youtube.com/embed/GX0rf6HjdcU",
        "thumbnail": "https://img.youtube.com/vi/GX0rf6HjdcU/hqdefault.jpg"
    },
    "creacion de venv.mp4": {
        "youtube_id": "GX0rf6HjdcU",
        "youtube_url": "https://youtu.be/GX0rf6HjdcU",
        "embed_url": "https://www.youtube.com/embed/GX0rf6HjdcU",
        "thumbnail": "https://img.youtube.com/vi/GX0rf6HjdcU/hqdefault.jpg"
    }
}

ACRONYMS = {"ia", "ai", "eda", "knn", "pca", "cnf", "dfs", "bfs", "gbfs", "gps", "etl", "csv", "json", "pdf", "sql", "svm", "mlp", "mcar", "mar", "mnar", "ols", "auc", "roc", "cart", "kdd", "crisp-dm", "nlp", "llm", "llms", "genai", "cv"}
LOWERCASE_WORDS = {"de", "la", "el", "los", "las", "en", "y", "del", "al", "para", "por", "con", "un", "una", "unos", "unas", "o", "a", "vs"}

def format_title(filename):
    for k, v in KNOWN_TITLES.items():
        if k.lower() == filename.lower():
            return v
    clean = filename.replace(".ipynb", "").replace(".pdf", "").replace(".mp4", "").replace(".mkv", "").replace(".webm", "")
    clean = re.sub(r'^\d+[a-z]?_', '', clean)
    clean = clean.replace("_compressed", "").replace("_", " ").replace("-", " ")
    words = clean.strip().split()
    formatted = []
    for i, w in enumerate(words):
        w_lower = w.lower()
        if w_lower in ACRONYMS:
            formatted.append(w.upper())
        elif i > 0 and w_lower in LOWERCASE_WORDS:
            formatted.append(w_lower)
        else:
            formatted.append(w.capitalize())
    return " ".join(formatted)

def infer_difficulty(title, path):
    text = f"{title} {path}".lower()
    if any(k in text for k in ["intro", "conceptos", "basico", "sintaxis", "creacion"]):
        return "Básico"
    if any(k in text for k in ["avanzado", "regularizacion", "knn", "pca", "poo", "clases"]):
        return "Avanzado"
    return "Intermedio"

def sync_course_assets(course_id, course_folder_name, course_dir):
    """Sincroniza Guias/, Contenido/ y Libros/ del curso hacia docs/"""
    for folder_name in ["Guias", "Contenido"]:
        src = course_dir / folder_name
        dest = DOCS_DIR / folder_name
        dest.mkdir(parents=True, exist_ok=True)
        if src.exists() and src.is_dir():
            for item in src.rglob("*"):
                if item.is_file():
                    rel = item.relative_to(src)
                    target_file = dest / rel
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    if not target_file.exists() or target_file.stat().st_mtime < item.stat().st_mtime:
                        shutil.copy2(item, target_file)
                        print(f"  [SYNC] Copiado: {item.name} -> docs/{folder_name}/{rel}")

    src_libros = course_dir / "Libros"
    if src_libros.exists() and src_libros.is_dir():
        if course_id == "data-science-programming":
            dest_libros = DOCS_DIR / "Libros"
            for item in src_libros.rglob("*"):
                if item.is_file():
                    rel = item.relative_to(src_libros)
                    target_file = dest_libros / rel
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    if not target_file.exists() or target_file.stat().st_mtime < item.stat().st_mtime:
                        shutil.copy2(item, target_file)
                        print(f"  [SYNC] Copiado: {item.name} -> docs/Libros/{rel}")
        else:
            subname = SUBFOLDER_MAP.get(course_id, course_folder_name)
            dest_libros = DOCS_DIR / "Libros" / subname
            dest_libros.mkdir(parents=True, exist_ok=True)
            for item in src_libros.glob("*.pdf"):
                if item.is_file():
                    target_file = dest_libros / item.name
                    if not target_file.exists() or target_file.stat().st_mtime < item.stat().st_mtime:
                        shutil.copy2(item, target_file)
                        print(f"  [SYNC] Copiado: {item.name} -> docs/Libros/{subname}/{item.name}")

def scan_course_modules(course_dir, default_modules=None):
    modules = [dict(m) for m in default_modules] if default_modules else []
    existing_ids = {m["id"] for m in modules}
    existing_names = {m["name"] for m in modules}

    if course_dir.exists() and course_dir.is_dir():
        for item in sorted(course_dir.iterdir()):
            if item.is_dir() and not item.name.startswith(".") and item.name not in ["Libros", "Guias", "Contenido", "node_modules", "data"]:
                match = re.match(r'^(\d{2})\s*-\s*(.+)$', item.name)
                if match:
                    mod_id = match.group(1)
                    if mod_id not in existing_ids and item.name not in existing_names:
                        pal = PALETTE[len(modules) % len(PALETTE)]
                        modules.append({
                            "id": mod_id,
                            "name": item.name,
                            "title": format_title(match.group(2)),
                            "icon": pal["icon"],
                            "color": pal["color"],
                            "description": f"Módulo de especialización sobre {format_title(match.group(2))}."
                        })
                        existing_ids.add(mod_id)
                        existing_names.add(item.name)
                elif item.name.lower() == "homeworks" and "hw" not in existing_ids and item.name not in existing_names:
                    modules.append({
                        "id": "hw",
                        "name": "homeworks",
                        "title": "Talleres Prácticos Evaluativos (Hands-On)",
                        "icon": "📝",
                        "color": "#DC2626",
                        "description": "Talleres integradores de resolución autónoma con datos reales y desafíos de negocio."
                    })
                    existing_ids.add("hw")
                    existing_names.add(item.name)
                elif any(item.rglob("*.ipynb")):
                    mod_id = f"{len(modules)+1:02d}"
                    if mod_id not in existing_ids and item.name not in existing_names:
                        pal = PALETTE[len(modules) % len(PALETTE)]
                        modules.append({
                            "id": mod_id,
                            "name": item.name,
                            "title": f"Módulo: {format_title(item.name)}",
                            "icon": "⚡",
                            "color": "#10b981",
                            "description": f"Módulo complementario sobre {format_title(item.name)}."
                        })
                        existing_ids.add(mod_id)
                        existing_names.add(item.name)
    return modules

# =========================================================================
# CATÁLOGO OFICIAL DE LIBROS EN PDF (EXCLUSIVAMENTE LOS PRESENTES EN Libros/)
# =========================================================================

SUBFOLDER_MAP = {
    "data-science-programming": "Python",
    "data-mining": "Data Mining",
    "machine-learning": "Machine Learning",
    "visual-analytics": "Visual Analytics",
    "introduccion-ia": "Inteligencia Artificial"
}

BOOKS_METADATA = {
    # -------------------------------------------------------------------------
    # 1. Programación para Ciencia de Datos (Python & Algoritmos)
    # -------------------------------------------------------------------------
    "head first python, 2nd edition.pdf": {
        "title": "Head First Python",
        "subtitle": "A Brain-Friendly Guide to Learning Python",
        "author": "Paul Barry",
        "publisher": "O'Reilly Media",
        "year": "2016",
        "edition": "2nd Edition",
        "category": "Para Dummies / Principiantes",
        "level": "Básico (100% Visual / Dummies)",
        "dummies_friendly": True,
        "summary_dummies": "Enfoque 100% visual y entretenido con diagramas, ilustraciones y analogías intuitivas. Ideal para aprender a programar sin aburrirse ni perderse en tecnicismos densos.",
        "topics": ["Sintaxis Básica", "Estructuras de Datos", "Funciones", "Bases de Datos", "Aplicaciones Web"],
        "cover_gradient": "from-amber-600 via-yellow-700 to-amber-950",
        "cover_bg": "#f59e0b",
        "accent_color": "#fbbf24",
        "icon": "🧠"
    },
    "python crash course, 2nd edition.pdf": {
        "title": "Python Crash Course",
        "subtitle": "A Hands-On, Project-Based Introduction to Programming",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "year": "2019",
        "edition": "2nd Edition",
        "category": "Para Dummies / Principiantes",
        "level": "Básico (Paso a Paso)",
        "dummies_friendly": True,
        "summary_dummies": "El bestseller mundial #1 para iniciarse en Python. Enseña conceptos paso a paso y te guía en la creación de proyectos prácticos, visualizaciones interactivas y aplicaciones reales.",
        "topics": ["Variables & Listas", "Bucles & Diccionarios", "Clases POO", "Visualización con Matplotlib", "Proyectos Reales"],
        "cover_gradient": "from-red-600 via-rose-700 to-neutral-900",
        "cover_bg": "#e11d48",
        "accent_color": "#f43f5e",
        "icon": "🚀"
    },
    "automate the boring stuff with python.pdf": {
        "title": "Automate the Boring Stuff with Python",
        "subtitle": "Practical Programming for Total Beginners",
        "author": "Al Sweigart",
        "publisher": "No Starch Press",
        "year": "2019",
        "edition": "2nd Edition",
        "category": "Para Dummies / Principiantes",
        "level": "Básico (Para No Ingenieros)",
        "dummies_friendly": True,
        "summary_dummies": "Diseñado para profesionales sin conocimientos previos de programación. Aprende a manipular hojas de cálculo de Excel, archivos PDF, correos electrónicos y tareas repetitivas en minutos.",
        "topics": ["Automatización", "Archivos Excel & CSV", "Manipulación de PDFs", "Web Scraping", "Expresiones Regulares"],
        "cover_gradient": "from-emerald-600 via-teal-700 to-slate-950",
        "cover_bg": "#059669",
        "accent_color": "#10b981",
        "icon": "⚙️"
    },
    "python data science handbook.pdf": {
        "title": "Python Data Science Handbook",
        "subtitle": "Essential Tools for Working with Data",
        "author": "Jake VanderPlas",
        "publisher": "O'Reilly Media",
        "year": "2023",
        "edition": "2nd Edition",
        "category": "Ciencia de Datos & Análisis",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "El manual de referencia esencial para Ciencia de Datos. Guía exhaustiva y práctica sobre IPython, NumPy, Pandas, visualización con Matplotlib y Machine Learning con Scikit-Learn.",
        "topics": ["IPython & Jupyter", "NumPy Vectorizado", "Pandas DataFrames", "Matplotlib", "Scikit-Learn ML"],
        "cover_gradient": "from-sky-600 via-blue-700 to-indigo-950",
        "cover_bg": "#0284c7",
        "accent_color": "#38bdf8",
        "icon": "📊"
    },
    "fluent python, 2nd edition.pdf": {
        "title": "Fluent Python",
        "subtitle": "Clear, Concise, and Effective Programming",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "year": "2022",
        "edition": "2nd Edition",
        "category": "Fundamentos & Estructuras",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "El libro cumbre para escribir código Python idiomático, limpio y elegante. Profundiza en el modelo de objetos de Python, decoradores, generadores, corrutinas y tipado moderno.",
        "topics": ["Modelo de Datos", "Estructuras Especiales", "POO Idiomática", "Decoradores & Generadores", "Concurrencia Async"],
        "cover_gradient": "from-purple-600 via-indigo-700 to-slate-950",
        "cover_bg": "#7c3aed",
        "accent_color": "#a855f7",
        "icon": "🐍"
    },
    "data structures and algorithms with python.pdf": {
        "title": "Data Structures and Algorithms with Python",
        "subtitle": "Undergraduate Topics in Computer Science",
        "author": "Kent D. Lee, Steve Hubbard",
        "publisher": "Springer",
        "year": "2015",
        "edition": "1st Edition",
        "category": "Fundamentos & Estructuras",
        "level": "Intermedio",
        "dummies_friendly": False,
        "summary_dummies": "Explicación rigurora de las estructuras de datos fundamentales (listas enlazadas, pilas, colas, árboles, grafos y tablas hash) y análisis de complejidad de algoritmos con Python.",
        "topics": ["Complejidad Big-O", "Pilas & Colas", "Árboles Binarios", "Grafos & Búsqueda", "Algoritmos de Ordenación"],
        "cover_gradient": "from-cyan-600 via-teal-800 to-slate-950",
        "cover_bg": "#0891b2",
        "accent_color": "#06b6d4",
        "icon": "🌳"
    },
    "high performance python.pdf": {
        "title": "High Performance Python",
        "subtitle": "Practical Performant Programming for Humans",
        "author": "Micha Gorelick, Ian Ozsvald",
        "publisher": "O'Reilly Media",
        "year": "2020",
        "edition": "2nd Edition",
        "category": "Rendimiento & Optimización",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Aprende a acelerar código de Ciencia de Datos y Machine Learning. Perfilado de CPU y memoria, operaciones vectoriales con NumPy, compilación Cython/Numba y computación distribuida.",
        "topics": ["Perfilado CPU & RAM", "NumPy & Numba", "Cython", "Multiprocessing", "Big Data"],
        "cover_gradient": "from-amber-700 via-orange-800 to-stone-950",
        "cover_bg": "#c2410c",
        "accent_color": "#f97316",
        "icon": "⚡"
    },
    "python cookbook, 3rd edition.pdf": {
        "title": "Python Cookbook",
        "subtitle": "Recipes for Mastering Python 3",
        "author": "David Beazley, Brian K. Jones",
        "publisher": "O'Reilly Media",
        "year": "2013",
        "edition": "3rd Edition",
        "category": "Recetas & Buenas Prácticas",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Colección de soluciones prácticas y concisas a problemas cotidianos de programación: manipulación de estructuras de datos, iteradores, algoritmos, metaprogramación y manejo de archivos.",
        "topics": ["Estructuras & Algoritmos", "Iteradores & Generadores", "I/O de Archivos", "Metaprogramación", "Concurrencia"],
        "cover_gradient": "from-emerald-700 via-green-800 to-slate-950",
        "cover_bg": "#047857",
        "accent_color": "#10b981",
        "icon": "📖"
    },
    "modern python cookbook.pdf": {
        "title": "Modern Python Cookbook",
        "subtitle": "Over 130 Recipes to Build Smart, Scalable Applications",
        "author": "Steven F. Lott",
        "publisher": "Packt Publishing",
        "year": "2020",
        "edition": "2nd Edition",
        "category": "Recetas & Buenas Prácticas",
        "level": "Intermedio",
        "dummies_friendly": False,
        "summary_dummies": "Más de 130 recetas modernas con las últimas características del lenguaje, programación funcional, tipado estático, persistencia de datos y desarrollo de APIs limpias.",
        "topics": ["Programación Funcional", "Tipado Estático", "Bases de Datos & SQL", "JSON/CSV", "Estructuras Modernas"],
        "cover_gradient": "from-blue-700 via-indigo-800 to-slate-950",
        "cover_bg": "#1d4ed8",
        "accent_color": "#3b82f6",
        "icon": "🍳"
    },
    "pro python best practices.pdf": {
        "title": "Pro Python Best Practices",
        "subtitle": "Debugging, Testing and Maintaining Code in Real-World Projects",
        "author": "Cristian Medina",
        "publisher": "Apress",
        "year": "2020",
        "edition": "1st Edition",
        "category": "Recetas & Buenas Prácticas",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Aprende los estándares de la industria profesional: depuración de errores, pruebas unitarias automatizadas con pytest, linters, documentación clara y código mantenible para proyectos reales.",
        "topics": ["Clean Code", "Testing con PyTest", "Debugging", "Linters & Flake8", "Documentación Profesional"],
        "cover_gradient": "from-teal-700 via-emerald-800 to-slate-950",
        "cover_bg": "#0f766e",
        "accent_color": "#14b8a6",
        "icon": "🛡️"
    },
    "programming in python 3, 2nd edition.pdf": {
        "title": "Programming in Python 3",
        "subtitle": "A Complete Introduction to the Python Language",
        "author": "Mark Summerfield",
        "publisher": "Addison-Wesley Professional",
        "year": "2010",
        "edition": "2nd Edition",
        "category": "Fundamentos & Estructuras",
        "level": "Básico a Intermedio",
        "dummies_friendly": False,
        "summary_dummies": "Tratado exhaustivo y metódico sobre el lenguaje Python 3. Estructurado paso a paso desde tipos de datos básicos y control de flujo hasta programación funcional, bases de datos y red.",
        "topics": ["Sintaxis & Semántica", "Tipos de Datos", "E/S de Archivos", "Módulos & Paquetes", "Programación de Redes"],
        "cover_gradient": "from-slate-700 via-gray-800 to-zinc-950",
        "cover_bg": "#334155",
        "accent_color": "#94a3b8",
        "icon": "📘"
    },

    # -------------------------------------------------------------------------
    # 2. Data Mining (Minería de Datos, KDD & Algoritmos)
    # -------------------------------------------------------------------------
    "data mining - the textbook.pdf": {
        "title": "Data Mining: The Textbook",
        "subtitle": "Principles, Algorithms, and Systems of Data Mining",
        "author": "Charu C. Aggarwal",
        "publisher": "Springer",
        "year": "2015",
        "edition": "1st Edition",
        "category": "Data Mining & KDD",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Texto de referencia académica global. Tratamiento matemático riguroso y sistemático de clustering, clasificación, minería de reglas, detección de anomalías y grafos.",
        "topics": ["Clustering", "Clasificación", "Outlier Detection", "Association Rules", "Graph Mining"],
        "cover_gradient": "from-rose-600 via-pink-700 to-slate-950",
        "cover_bg": "#f43f5e",
        "accent_color": "#fb7185",
        "icon": "⛏️"
    },
    "introduction to data mining - vipin kumar.pdf": {
        "title": "Introduction to Data Mining",
        "subtitle": "Concepts, Techniques, and Algorithmic Foundations",
        "author": "Pang-Ning Tan, Michael Steinbach, Vipin Kumar",
        "publisher": "Pearson",
        "year": "2018",
        "edition": "2nd Edition",
        "category": "Data Mining & KDD",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "El estándar pedagógico mundial para aprender minería de datos. Enfoque visual e intuitivo sobre K-Means, DBSCAN, árboles de decisión, soporte/confianza y métricas de evaluación.",
        "topics": ["CRISP-DM", "K-Means", "DBSCAN", "Apriori & FP-Growth", "Árboles de Decisión"],
        "cover_gradient": "from-pink-600 via-rose-700 to-neutral-900",
        "cover_bg": "#e11d48",
        "accent_color": "#f43f5e",
        "icon": "🔍"
    },
    "principles of data mining - max bramer.pdf": {
        "title": "Principles of Data Mining",
        "subtitle": "Undergraduate Topics in Computer Science",
        "author": "Max Bramer",
        "publisher": "Springer",
        "year": "2020",
        "edition": "4th Edition",
        "category": "Data Mining & KDD",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Enfoque claro y directo sobre inducción de reglas clasificadoras, entropía, ganancia de información, Naive Bayes y evaluación empírica de algoritmos.",
        "topics": ["Reglas de Decisión", "Naive Bayes", "Medidas de Impureza", "Ensembles"],
        "cover_gradient": "from-indigo-600 via-purple-700 to-slate-950",
        "cover_bg": "#6366f1",
        "accent_color": "#818cf8",
        "icon": "📐"
    },
    "web data mining 2nd edition - bing liu.pdf": {
        "title": "Web Data Mining",
        "subtitle": "Exploring Hyperlinks, Contents, and Usage Data",
        "author": "Bing Liu",
        "publisher": "Springer",
        "year": "2011",
        "edition": "2nd Edition",
        "category": "Data Mining & KDD",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Obra cumbre sobre minería en la web: análisis de enlaces (PageRank, HITS), web crawling, opinion mining, sentiment analysis y minería de registros de navegación.",
        "topics": ["Web Crawling", "PageRank", "Sentiment Analysis", "Text Mining", "Web Logs"],
        "cover_gradient": "from-teal-600 via-cyan-700 to-slate-950",
        "cover_bg": "#0d9488",
        "accent_color": "#14b8a6",
        "icon": "🌐"
    },
    "web data mining with python - ranjana rajnish.pdf": {
        "title": "Web Data Mining with Python",
        "subtitle": "Techniques and Tools for Mining Unstructured Web Data",
        "author": "Ranjana Rajnish",
        "publisher": "CRC Press",
        "year": "2023",
        "edition": "1st Edition",
        "category": "Data Mining & KDD",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Guía práctica de minería web aplicada en Python: extracción automatizada con BeautifulSoup y Selenium, procesamiento de lenguaje natural y modelado de tópicos.",
        "topics": ["Web Scraping", "Python", "BeautifulSoup", "NLP", "Text Mining"],
        "cover_gradient": "from-emerald-600 via-teal-700 to-slate-950",
        "cover_bg": "#059669",
        "accent_color": "#10b981",
        "icon": "🕷️"
    },
    "handbook of statistical analysis and data mining applications.pdf": {
        "title": "Handbook of Statistical Analysis and Data Mining Applications",
        "subtitle": "Comprehensive Reference for Data Science Practitioners",
        "author": "Robert Nisbet, John Elder, Gary Miner",
        "publisher": "Academic Press",
        "year": "2018",
        "edition": "2nd Edition",
        "category": "Data Mining & KDD",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Enciclopedia práctica sobre el ciclo de vida del dato: preparación de tablas analíticas, selección óptima de algoritmos, validación cruzada y casos de estudio industriales.",
        "topics": ["CRISP-DM", "Metodología KDD", "Estadística Multivariada", "Modelos Predictivos"],
        "cover_gradient": "from-amber-600 via-orange-700 to-neutral-900",
        "cover_bg": "#d97706",
        "accent_color": "#f59e0b",
        "icon": "📚"
    },
    "data mining and predictive analytics for business decisions.pdf": {
        "title": "Data Mining and Predictive Analytics for Business Decisions",
        "subtitle": "Turning Enterprise Data into High-Value Strategic Insights",
        "author": "Daniel T. Larose, Chantal D. Larose",
        "publisher": "Wiley",
        "year": "2015",
        "edition": "2nd Edition",
        "category": "Ciencia de Datos & Análisis",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Aprende a aplicar modelos predictivos y minería de datos directamente en el mundo de los negocios: scoring de crédito, retención de clientes y predicción de fraude.",
        "topics": ["Business Analytics", "Scoring Crediticio", "Churn Prediction", "Segmentación"],
        "cover_gradient": "from-blue-600 via-indigo-700 to-slate-950",
        "cover_bg": "#2563eb",
        "accent_color": "#3b82f6",
        "icon": "💼"
    },
    "data mining competition practices - methods and cases.pdf": {
        "title": "Data Mining Competition Practices",
        "subtitle": "Winning Methods, Advanced Feature Engineering, and Real Cases",
        "author": "Xue-Bo Jin, Competition Group",
        "publisher": "Springer",
        "year": "2024",
        "edition": "1st Edition",
        "category": "Ciencia de Datos & Análisis",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Metodologías de élite en competiciones de ciencia de datos: validación cruzada estratificada adversaria, target encoding regularizado, ensambles por apilamiento (Stacking) y Optuna.",
        "topics": ["Kaggle Strategies", "Feature Engineering", "Ensembles", "Model Stacking", "Optuna"],
        "cover_gradient": "from-violet-600 via-purple-700 to-slate-950",
        "cover_bg": "#7c3aed",
        "accent_color": "#a855f7",
        "icon": "🏆"
    },
    "data mining and analytics in healthcare management.pdf": {
        "title": "Data Mining and Analytics in Healthcare Management",
        "subtitle": "Transforming Clinical Care and Health Systems Optimization",
        "author": "V. K. Singh et al.",
        "publisher": "Springer",
        "year": "2023",
        "edition": "1st Edition",
        "category": "Ciencia de Datos & Análisis",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Aplicación de técnicas analíticas al sector biomédico y clínico: diagnóstico temprano asistido por machine learning, minería de historiales electrónicos y optimización hospitalaria.",
        "topics": ["Health Informatics", "Historias Clínicas", "Modelos Predictivos en Salud", "Clustering Pacientes"],
        "cover_gradient": "from-cyan-600 via-blue-700 to-slate-950",
        "cover_bg": "#0891b2",
        "accent_color": "#06b6d4",
        "icon": "🏥"
    },
    "e-commerce big data mining and analytics.pdf": {
        "title": "E-Commerce Big Data Mining and Analytics",
        "subtitle": "Market Baskets, Recommender Systems, and Customer Intelligence",
        "author": "Zhi-Pei Fan et al.",
        "publisher": "CRC Press",
        "year": "2022",
        "edition": "1st Edition",
        "category": "Ciencia de Datos & Análisis",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Técnicas esenciales para el comercio digital: minería de carritos de compra (Market Basket), reglas de asociación, filtrado colaborativo en recomendaciones y fijación dinámica de precios.",
        "topics": ["Market Basket Analysis", "Sistemas de Recomendación", "Pricing Dinámico", "Reglas Apriori"],
        "cover_gradient": "from-amber-600 via-yellow-700 to-stone-900",
        "cover_bg": "#d97706",
        "accent_color": "#f59e0b",
        "icon": "🛒"
    },
    "data science and machine learning for non-programmers - dothang truong.pdf": {
        "title": "Data Science and Machine Learning for Non-Programmers",
        "subtitle": "Using Visual Analytics and Intuitive Workflows",
        "author": "Dothang Truong",
        "publisher": "Chapman and Hall / CRC",
        "year": "2024",
        "edition": "1st Edition",
        "category": "Para Dummies / Principiantes",
        "level": "Básico (Visual / Dummies)",
        "dummies_friendly": True,
        "summary_dummies": "El libro ideal para entender la ciencia de datos sin programar código complejo. Explica cómo funcionan los árboles de decisión, regresiones y clusters mediante diagramas y flujo de datos visual.",
        "topics": ["Conceptos Visuales", "Clasificación", "Regresión", "Analítica Sin Código"],
        "cover_gradient": "from-rose-600 via-orange-700 to-neutral-900",
        "cover_bg": "#e11d48",
        "accent_color": "#f43f5e",
        "icon": "💡"
    },
    "feature engineering for modern machine learning with scikit-learn - miguel gonzalez.pdf": {
        "title": "Feature Engineering for Modern Machine Learning",
        "subtitle": "Building Production-Grade Pipelines with Scikit-Learn",
        "author": "Miguel Gonzalez",
        "publisher": "O'Reilly Media",
        "year": "2025",
        "edition": "1st Edition",
        "category": "Fundamentos & Estructuras",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Manual técnico indispensable: transformación de variables numéricas, codificación de alta cardinalidad, creación de ratios, extracción de componentes PCA y validación cruzada libre de data leakage.",
        "topics": ["Feature Engineering", "Scikit-Learn Pipelines", "Target Encoding", "PCA", "Preprocesamiento"],
        "cover_gradient": "from-purple-600 via-indigo-700 to-slate-950",
        "cover_bg": "#7c3aed",
        "accent_color": "#a855f7",
        "icon": "⚙️"
    },
    "data mining for scientific and engineering applications.pdf": {
        "title": "Data Mining for Scientific and Engineering Applications",
        "subtitle": "Massive Datasets in Physics, Astronomy, and Bioinformatics",
        "author": "Robert L. Grossman et al.",
        "publisher": "Kluwer Academic Publishers",
        "year": "2021",
        "edition": "1st Edition",
        "category": "Algoritmos & Métodos",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Tratamiento avanzado de grandes volúmenes de datos experimentales, series de tiempo continuas, análisis espacial y modelado estocástico para ingeniería y física computacional.",
        "topics": ["Scientific Data", "Time Series", "Spatial Mining", "Signal Processing"],
        "cover_gradient": "from-slate-700 via-teal-800 to-neutral-950",
        "cover_bg": "#0f766e",
        "accent_color": "#14b8a6",
        "icon": "🔬"
    },
    "linear algebra tools for data mining 2nd edition - dan a simovici.pdf": {
        "title": "Linear Algebra Tools for Data Mining",
        "subtitle": "Mathematical Foundations for Machine Learning Algorithms",
        "author": "Dan A. Simovici",
        "publisher": "World Scientific",
        "year": "2020",
        "edition": "2nd Edition",
        "category": "Algoritmos & Métodos",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Fundamentos matemáticos esenciales: descomposición en valores singulares (SVD), análisis de componentes principales (PCA), factorización de matrices no negativas (NMF) y teoría espectral de grafos.",
        "topics": ["Álgebra Lineal", "SVD", "PCA", "Factorización Matricial", "Teoría Espectral"],
        "cover_gradient": "from-cyan-700 via-blue-800 to-slate-950",
        "cover_bg": "#0369a1",
        "accent_color": "#0284c7",
        "icon": "📐"
    },
    "machine learning and data mining - andries engelbrecht.pdf": {
        "title": "Computational Intelligence & Data Mining",
        "subtitle": "An Introduction to Neural Networks and Evolutionary Computing",
        "author": "Andries P. Engelbrecht",
        "publisher": "Wiley",
        "year": "2019",
        "edition": "2nd Edition",
        "category": "Algoritmos & Métodos",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Algoritmos bioinspirados para optimización: redes neuronales artificiales, algoritmos genéticos, optimización por enjambre de partículas (PSO) y sistemas inmunes aplicados a minería de datos.",
        "topics": ["Redes Neuronales", "Algoritmos Genéticos", "PSO", "Inteligencia Computacional"],
        "cover_gradient": "from-violet-700 via-indigo-800 to-slate-950",
        "cover_bg": "#6d28d9",
        "accent_color": "#8b5cf6",
        "icon": "🤖"
    },
    "metalearning - applications to data mining - pavel brazdil.pdf": {
        "title": "Metalearning: Applications to Data Mining",
        "subtitle": "Automated Algorithm Selection and AutoML Foundations",
        "author": "Pavel Brazdil, Christophe Giraud-Carrier, Carlos Soares",
        "publisher": "Springer",
        "year": "2022",
        "edition": "2nd Edition",
        "category": "Algoritmos & Métodos",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "El arte de aprender a aprender: selección automatizada de algoritmos de clasificación, extracción de meta-características de datasets y bases teóricas de los modernos sistemas AutoML.",
        "topics": ["AutoML", "Meta-Learning", "Selección de Modelos", "Hyperparameter Tuning"],
        "cover_gradient": "from-pink-700 via-rose-800 to-slate-950",
        "cover_bg": "#be123c",
        "accent_color": "#f43f5e",
        "icon": "🧬"
    },
    "swarm intelligence in data mining - ajith abraham.pdf": {
        "title": "Swarm Intelligence in Data Mining",
        "subtitle": "Collective Intelligence for Clustering and Optimization",
        "author": "Ajith Abraham, Crina Grosan, Vitorino Ramos",
        "publisher": "Springer",
        "year": "2021",
        "edition": "1st Edition",
        "category": "Algoritmos & Métodos",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Aplica el comportamiento colectivo de hormigas, abejas y bandadas de aves para resolver problemas complejos de agrupamiento no supervisado y selección óptima de atributos en alta dimensión.",
        "topics": ["Swarm Intelligence", "Ant Colony Optimization", "Feature Selection", "Clustering Heurístico"],
        "cover_gradient": "from-amber-700 via-yellow-800 to-stone-950",
        "cover_bg": "#b45309",
        "accent_color": "#f59e0b",
        "icon": "🐝"
    },
    "learning tableau 2025 6th edition - joshua n milligan.pdf": {
        "title": "Learning Tableau 2025",
        "subtitle": "Tools for Visual Data Exploration and Storytelling",
        "author": "Joshua N. Milligan",
        "publisher": "Packt Publishing",
        "year": "2025",
        "edition": "6th Edition",
        "category": "Tableau & Visualización",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "El manual más actualizado sobre Tableau 2025: expresiones de nivel de detalle (LOD), mapas geoespaciales interactivos, acciones de conjuntos y diseño de dashboards ejecutivos dinámicos.",
        "topics": ["Tableau 2025", "LOD Expressions", "Dashboards", "Visual Analytics"],
        "cover_gradient": "from-blue-600 via-teal-700 to-slate-950",
        "cover_bg": "#0284c7",
        "accent_color": "#38bdf8",
        "icon": "📊"
    },

    # -------------------------------------------------------------------------
    # 3. Machine Learning (Aprendizaje Automático & Deep Learning)
    # -------------------------------------------------------------------------
    "hands-on machine learning with scikit-learn and pytorch - aurelien geron.pdf": {
        "title": "Hands-On Machine Learning with Scikit-Learn and PyTorch",
        "subtitle": "Concepts, Tools, and Techniques to Build Intelligent Systems",
        "author": "Aurélien Géron",
        "publisher": "O'Reilly Media",
        "year": "2025",
        "edition": "3rd / 4th Edition (Latest 2025 Release)",
        "category": "Machine Learning & IA",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": True,
        "summary_dummies": "La biblia mundial indiscutible del aprendizaje automático práctico. Cubre desde regresión logística y árboles de ensamble con Scikit-Learn hasta redes neuronales profundas con PyTorch.",
        "topics": ["Scikit-Learn", "PyTorch", "Deep Learning", "Random Forest", "Transformers", "Redes Neuronales"],
        "cover_gradient": "from-violet-600 via-indigo-700 to-slate-950",
        "cover_bg": "#7c3aed",
        "accent_color": "#a855f7",
        "icon": "🧠"
    },

    # -------------------------------------------------------------------------
    # 4. Visual Analytics and Critical Thinking (Power BI, Tableau & Power Query)
    # -------------------------------------------------------------------------
    "microsoft power bi for dummies.pdf": {
        "title": "Microsoft Power BI For Dummies",
        "subtitle": "Turn Your Data into Dynamic Visual Presentations",
        "author": "Jack A. Hyman",
        "publisher": "Wiley (For Dummies)",
        "year": "2022",
        "edition": "1st Edition",
        "category": "Para Dummies / Principiantes",
        "level": "Básico (100% Visual / Dummies)",
        "dummies_friendly": True,
        "summary_dummies": "La mejor introducción amigable para profesionales de cualquier área. Aprende a conectar Excel, limpiar datos visualmente y crear tableros impactantes en minutos.",
        "topics": ["Power BI Básico", "Importación de Datos", "Visualizaciones", "Dashboards"],
        "cover_gradient": "from-yellow-600 via-amber-700 to-stone-900",
        "cover_bg": "#eab308",
        "accent_color": "#fde047",
        "icon": "💡"
    },
    "tableau for dummies 2nd edition - jack a hyman.pdf": {
        "title": "Tableau For Dummies",
        "subtitle": "The Easy Way to Understand and Visualize Your Data",
        "author": "Jack A. Hyman",
        "publisher": "Wiley (For Dummies)",
        "year": "2022",
        "edition": "2nd Edition",
        "category": "Para Dummies / Principiantes",
        "level": "Básico (100% Visual / Dummies)",
        "dummies_friendly": True,
        "summary_dummies": "Explicado con analogías y pasos simples sin jerga matemática: conecta tablas de datos, arrastra campos a los ejes y comparte historias interactivas con tus colegas.",
        "topics": ["Tableau Básico", "Conexión de Datos", "Story Points", "Visualizaciones"],
        "cover_gradient": "from-amber-600 via-yellow-700 to-stone-900",
        "cover_bg": "#d97706",
        "accent_color": "#fbbf24",
        "icon": "📈"
    },
    "96 common challenges in power query.pdf": {
        "title": "96 Common Challenges in Power Query",
        "subtitle": "Practical Solutions for Data Transformation in Power BI and Excel",
        "author": "Gil Raviv",
        "publisher": "Packt Publishing",
        "year": "2023",
        "edition": "1st Edition",
        "category": "Power Query & ETL",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Recetario directo con 96 soluciones a los problemas más frecuentes de preparación de datos: unificar columnas, corregir fechas corruptas, limpiar caracteres invisibles y despivotar.",
        "topics": ["Power Query", "Lenguaje M", "Limpieza de Datos", "Transformaciones ETL"],
        "cover_gradient": "from-amber-600 via-yellow-700 to-slate-950",
        "cover_bg": "#d97706",
        "accent_color": "#f59e0b",
        "icon": "⚡"
    },
    "collect, combine, and transform data using power query in power bi and excel 2nd edition.pdf": {
        "title": "Collect, Combine, and Transform Data Using Power Query",
        "subtitle": "The Definitive Guide for Power BI and Excel",
        "author": "Gil Raviv",
        "publisher": "Microsoft Press",
        "year": "2024",
        "edition": "2nd Edition",
        "category": "Power Query & ETL",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "El manual oficial de Microsoft Press sobre Power Query: arquitectura del motor Mashup, plegado de consultas (Query Folding) para máxima velocidad y automatización de pipelines ETL.",
        "topics": ["Microsoft Press", "Power Query", "Lenguaje M", "Query Folding", "ETL"],
        "cover_gradient": "from-orange-600 via-amber-700 to-slate-950",
        "cover_bg": "#ea580c",
        "accent_color": "#f97316",
        "icon": "🛠️"
    },
    "the definitive guide to power query m - greg deckler.pdf": {
        "title": "The Definitive Guide to Power Query (M)",
        "subtitle": "Mastering the Functional Language of Data Preparation in Power BI",
        "author": "Greg Deckler",
        "publisher": "Packt Publishing",
        "year": "2023",
        "edition": "1st Edition",
        "category": "Power Query & ETL",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Aprende a programar en el lenguaje funcional M como un profesional: funciones recursivas, manipulación directa de listas y registros, integración con APIs REST y webhooks.",
        "topics": ["Lenguaje M", "Funciones Personalizadas", "APIs REST", "Dataflow"],
        "cover_gradient": "from-amber-700 via-orange-800 to-stone-950",
        "cover_bg": "#c2410c",
        "accent_color": "#f97316",
        "icon": "💻"
    },
    "data cleaning with power bi - gus frazer.pdf": {
        "title": "Data Cleaning with Power BI",
        "subtitle": "The Definitive Guide to Transforming Dirty Data into Actionable Insights",
        "author": "Gus Frazer",
        "publisher": "Packt Publishing",
        "year": "2024",
        "edition": "1st Edition",
        "category": "Power BI & DAX",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Estrategias prácticas de saneamiento: detección de valores atípicos, auditoría de integridad referencial, diseño de esquemas en estrella y normalización de catálogos maestros.",
        "topics": ["Data Cleaning", "Power BI", "Modelado Dimensional", "Calidad del Dato"],
        "cover_gradient": "from-teal-600 via-emerald-700 to-slate-950",
        "cover_bg": "#0d9488",
        "accent_color": "#14b8a6",
        "icon": "🧹"
    },
    "data visualization with microsoft power bi - alex kolokolov.pdf": {
        "title": "Data Visualization with Microsoft Power BI",
        "subtitle": "Design Principles and Best Practices for Business Dashboards",
        "author": "Alex Kolokolov",
        "publisher": "Packt Publishing",
        "year": "2023",
        "edition": "1st Edition",
        "category": "Power BI & DAX",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Diseño estético y funcional para reportes corporativos: psicología del color, contraste, microinteracciones, disposición en rejilla (Grid Layout) y data storytelling ejecutivo.",
        "topics": ["UI/UX en Dashboards", "Visual Storytelling", "Paletas de Color", "Power BI"],
        "cover_gradient": "from-blue-600 via-indigo-700 to-slate-950",
        "cover_bg": "#2563eb",
        "accent_color": "#3b82f6",
        "icon": "🎨"
    },
    "exam ref pl-300 microsoft power bi data analyst - daniil maslyuk.pdf": {
        "title": "Exam Ref PL-300: Microsoft Power BI Data Analyst",
        "subtitle": "Official Microsoft Certification Study Guide",
        "author": "Daniil Maslyuk",
        "publisher": "Microsoft Press",
        "year": "2024",
        "edition": "2nd Edition",
        "category": "Power BI & DAX",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "La guía oficial de preparación para la certificación PL-300 de Microsoft: modelado dimensional, optimización de expresiones DAX, seguridad a nivel de fila (RLS) y gobernanza de áreas de trabajo.",
        "topics": ["Certificación PL-300", "DAX Avanzado", "Row-Level Security (RLS)", "Modelado"],
        "cover_gradient": "from-indigo-600 via-blue-700 to-slate-950",
        "cover_bg": "#4f46e5",
        "accent_color": "#6366f1",
        "icon": "🎓"
    },
    "learning microsoft power bi - jeremey arnold.pdf": {
        "title": "Learning Microsoft Power BI",
        "subtitle": "Transforming Data and Delivering Actionable Business Insights",
        "author": "Jeremey Arnold",
        "publisher": "O'Reilly Media",
        "year": "2023",
        "edition": "1st Edition",
        "category": "Power BI & DAX",
        "level": "Básico a Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Manual metódico de O'Reilly para dominar la plataforma: importación desde múltiples fuentes, creación de medidas analíticas con DAX, tarjetas KPI y distribución de aplicaciones.",
        "topics": ["O'Reilly", "Power BI Desktop", "Power BI Service", "Modelado de Datos"],
        "cover_gradient": "from-yellow-600 via-amber-700 to-neutral-900",
        "cover_bg": "#ca8a04",
        "accent_color": "#eab308",
        "icon": "📊"
    },
    "microsoft power bi cookbook 3rd edition - greg deckler.pdf": {
        "title": "Microsoft Power BI Cookbook",
        "subtitle": "Gain Actionable Insights with Over 90 Recipes for Power BI",
        "author": "Greg Deckler",
        "publisher": "Packt Publishing",
        "year": "2023",
        "edition": "3rd Edition",
        "category": "Power BI & DAX",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Más de 90 recetas avanzadas para resolver retos analíticos: DAX complejo para inteligencia temporal, segmentaciones dinámicas, deshabilitación de contexto y visuales personalizados.",
        "topics": ["Recetas DAX", "Time Intelligence", "Filtros Cruzados", "Visualizaciones"],
        "cover_gradient": "from-amber-600 via-yellow-700 to-slate-950",
        "cover_bg": "#d97706",
        "accent_color": "#f59e0b",
        "icon": "🍳"
    },
    "microsoft power bi data analyst associate study guide - paul turley.pdf": {
        "title": "Microsoft Power BI Data Analyst Associate Study Guide",
        "subtitle": "Prepare for the PL-300 Exam and Apply Best Practice Design",
        "author": "Paul Turley",
        "publisher": "O'Reilly Media",
        "year": "2024",
        "edition": "1st Edition",
        "category": "Power BI & DAX",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Guía exhaustiva escrita por el reconocido mentor Paul Turley. Enfoque analítico riguroso sobre diseño de soluciones confiables, DAX corporativo y preparación rigurosa para el examen PL-300.",
        "topics": ["PL-300", "Arquitectura Power BI", "Mejores Prácticas", "DAX"],
        "cover_gradient": "from-blue-700 via-indigo-800 to-slate-950",
        "cover_bg": "#1d4ed8",
        "accent_color": "#3b82f6",
        "icon": "📘"
    },
    "microsoft power bi visual calculations - jeroen ter heerdt.pdf": {
        "title": "Microsoft Power BI Visual Calculations",
        "subtitle": "The New Way to Calculate Metrics Directly on Visuals",
        "author": "Jeroen ter Heerdt",
        "publisher": "Packt Publishing",
        "year": "2024",
        "edition": "1st Edition",
        "category": "Power BI & DAX",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Descubre la última revolución de Microsoft: cálculos visuales que simplifican el DAX tradicional para medias móviles, variaciones porcentuales y acumulados sin fórmulas complejas.",
        "topics": ["Visual Calculations", "DAX Simplificado", "Métricas Móviles", "Power BI"],
        "cover_gradient": "from-cyan-600 via-teal-700 to-slate-950",
        "cover_bg": "#0891b2",
        "accent_color": "#06b6d4",
        "icon": "⚡"
    },
    "artificial intelligence with microsoft power bi - jennifer stirrup.pdf": {
        "title": "Artificial Intelligence with Microsoft Power BI",
        "subtitle": "Using AI Insights, Machine Learning and Cognitive Services",
        "author": "Jennifer Stirrup",
        "publisher": "Packt Publishing",
        "year": "2022",
        "edition": "1st Edition",
        "category": "Power BI & DAX",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": True,
        "summary_dummies": "Potencia tus tableros con inteligencia artificial: análisis de sentimientos, visión artificial, explicaciones automáticas con Key Influencers y modelos de AutoML en la nube.",
        "topics": ["AI Insights", "Key Influencers", "AutoML en Power BI", "Cognitive Services"],
        "cover_gradient": "from-violet-600 via-purple-700 to-slate-950",
        "cover_bg": "#7c3aed",
        "accent_color": "#a855f7",
        "icon": "🤖"
    },
    "architecting power bi solutions in microsoft fabric.pdf": {
        "title": "Architecting Power BI Solutions in Microsoft Fabric",
        "subtitle": "Enterprise Analytics, OneLake, and Direct Lake Architecture",
        "author": "Fabric Architecture Forum",
        "publisher": "Packt Publishing",
        "year": "2024",
        "edition": "1st Edition",
        "category": "Power BI & DAX",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "La arquitectura analítica del futuro: unificación en OneLake, pipelines Medallion (Bronze/Silver/Gold) y el modo Direct Lake que consulta terabytes en memoria con latencia cero.",
        "topics": ["Microsoft Fabric", "OneLake", "Direct Lake", "Arquitectura Empresarial"],
        "cover_gradient": "from-blue-700 via-slate-800 to-neutral-950",
        "cover_bg": "#1e40af",
        "accent_color": "#3b82f6",
        "icon": "🏗️"
    },
    "modern data analytics in excel - george mount.pdf": {
        "title": "Modern Data Analytics in Excel",
        "subtitle": "Using Power Query, Power Pivot, and Python in Excel",
        "author": "George Mount",
        "publisher": "O'Reilly Media",
        "year": "2024",
        "edition": "1st Edition",
        "category": "Ciencia de Datos & Análisis",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Moderniza tu flujo de trabajo en Excel adoptando Power Query para limpieza, Power Pivot para modelado relacional y la nueva integración nativa con Python para estadística avanzada.",
        "topics": ["Excel Moderno", "Power Query", "Power Pivot", "Python en Excel"],
        "cover_gradient": "from-emerald-700 via-teal-800 to-slate-950",
        "cover_bg": "#047857",
        "accent_color": "#10b981",
        "icon": "📗"
    },
    "mastering tableau 2026 - marleen meier.pdf": {
        "title": "Mastering Tableau 2026",
        "subtitle": "Enterprise Data Analytics, Governance, and Advanced Visualization",
        "author": "Marleen Meier",
        "publisher": "Packt Publishing",
        "year": "2025",
        "edition": "2026 Edition",
        "category": "Tableau & Visualización",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "La referencia cumbre para arquitectos de datos en Tableau: optimización de fuentes masivas, gobernanza y seguridad, extensiones web y tableros interactivos de alta complejidad.",
        "topics": ["Tableau Avanzado", "Gobernanza", "Performance Tuning", "Extensiones"],
        "cover_gradient": "from-teal-600 via-cyan-700 to-slate-950",
        "cover_bg": "#0d9488",
        "accent_color": "#14b8a6",
        "icon": "🚀"
    },
    "beginning with tableau cloud - urmisha patel.pdf": {
        "title": "Beginning with Tableau Cloud",
        "subtitle": "Accessing, Sharing, and Managing Analytical Content in the Cloud",
        "author": "Urmisha Patel",
        "publisher": "BPB Publications",
        "year": "2025",
        "edition": "1st Edition",
        "category": "Tableau & Visualización",
        "level": "Básico a Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Guía integral para colaborar en la nube: publicación de libros de trabajo, administración de accesos, programación de actualizaciones automáticas y flujos en Tableau Prep.",
        "topics": ["Tableau Cloud", "Colaboración", "Gobernanza", "Publicación"],
        "cover_gradient": "from-sky-600 via-blue-700 to-slate-950",
        "cover_bg": "#0284c7",
        "accent_color": "#38bdf8",
        "icon": "☁️"
    },
    "learning ai tools in tableau.pdf": {
        "title": "Learning AI Tools in Tableau",
        "subtitle": "Leveraging Tableau Pulse, Einstein Discovery and Predictive Analytics",
        "author": "Analytics Innovation Press",
        "publisher": "O'Reilly / Packt",
        "year": "2024",
        "edition": "1st Edition",
        "category": "Tableau & Visualización",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Descubre las herramientas de IA generativa y predictiva en Tableau: resúmenes automatizados con Tableau Pulse, explicaciones automáticas y modelos predictivos de Einstein Discovery.",
        "topics": ["Tableau Pulse", "Einstein Discovery", "IA Predictiva", "Storytelling"],
        "cover_gradient": "from-purple-600 via-pink-700 to-slate-950",
        "cover_bg": "#9333ea",
        "accent_color": "#c084fc",
        "icon": "🔮"
    },
    "visual analytics using tableau - sulabh bhatt.pdf": {
        "title": "Visual Analytics Using Tableau",
        "subtitle": "Structured Approach for Turning Raw Data to Powerful Insights",
        "author": "Neha Rajput, Sulabh Bhatt",
        "publisher": "BPB Publications",
        "year": "2025",
        "edition": "1st Edition",
        "category": "Tableau & Visualización",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Metodología estructurada de diseño visual: leyes de la Gestalt, codificación preatentiva por color y tamaño, minimización del desorden visual y creación de narrativas visuales persuasivas.",
        "topics": ["Percepción Visual", "Storytelling con Tableau", "Diseño Perceptual", "Leyes de Gestalt"],
        "cover_gradient": "from-indigo-600 via-teal-700 to-slate-950",
        "cover_bg": "#4f46e5",
        "accent_color": "#6366f1",
        "icon": "📊"
    },
    "python data analysis with tableau - francis mccaffery.pdf": {
        "title": "Python Data Analysis with Tableau",
        "subtitle": "Integrating TabPy for Advanced Statistical Computing and Machine Learning",
        "author": "Francis McCaffery",
        "publisher": "Packt Publishing",
        "year": "2023",
        "edition": "1st Edition",
        "category": "Tableau & Visualización",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Combina el poder de cálculo científico de Python con la elegancia visual de Tableau: conecta el servidor TabPy para ejecutar modelos de ML y pasar resultados en vivo a los tableros.",
        "topics": ["TabPy", "Python + Tableau", "Machine Learning en Tableau", "Simulaciones"],
        "cover_gradient": "from-blue-700 via-emerald-700 to-slate-950",
        "cover_bg": "#1d4ed8",
        "accent_color": "#3b82f6",
        "icon": "🐍"
    },
    "tableau cookbook for experienced professionals - pablo saenz de tejada.pdf": {
        "title": "Tableau Cookbook for Experienced Professionals",
        "subtitle": "Proven Recipes for Complex Data Visualization and Optimization",
        "author": "Pablo Sáenz de Tejada",
        "publisher": "Packt Publishing",
        "year": "2025",
        "edition": "1st Edition",
        "category": "Tableau & Visualización",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Colección experta de técnicas no convencionales: diagramas de Sankey, gráficos radiales, coordenadas paralelas, expresiones LOD anidadas y optimización para grandes volúmenes.",
        "topics": ["Gráficos Avanzados", "Sankey Charts", "LOD Anidados", "Optimización"],
        "cover_gradient": "from-teal-700 via-indigo-800 to-slate-950",
        "cover_bg": "#0f766e",
        "accent_color": "#14b8a6",
        "icon": "🍳"
    }
}


def scan_course_notebooks(course_folder_name, course_dir, modules, course_name=""):
    notebooks = []
    
    for mod in modules:
        mod_dir = course_dir / mod["name"]
        if mod_dir.exists() and mod_dir.is_dir():
            for nb_file in sorted(mod_dir.rglob("*.ipynb")):
                if ".ipynb_checkpoints" in str(nb_file):
                    continue
                
                rel_to_mod = nb_file.relative_to(mod_dir).as_posix()
                rel_path = f"{course_folder_name}/{mod['name']}/{rel_to_mod}"
                raw_title = format_title(nb_file.name)
                
                is_dummies = ("Para Dummies" in nb_file.parts) or ("_dummies" in nb_file.name.lower())
                is_homework = (mod["id"] == "hw") or ("homeworks" in nb_file.parts) or ("hands_on" in nb_file.name.lower())
                
                if is_dummies:
                    clean_title = re.sub(r'\b(Para\s+)?Dummies\b', '', raw_title, flags=re.IGNORECASE).strip()
                    title = f"💡 {clean_title} [Dummies] {mod['icon']}"
                    diff = "Básico (Dummies)"
                    edition = "Para Dummies"
                elif is_homework:
                    title = f"📝 {raw_title} {mod['icon']}"
                    diff = "Intermedio (Hands-On)"
                    edition = "Taller Evaluativo"
                else:
                    title = f"{raw_title} {mod['icon']}"
                    diff = infer_difficulty(raw_title, rel_path)
                    edition = "Estándar"

                encoded_path = urllib.parse.quote(rel_path)

                notebooks.append({
                    "id": f"{mod['id']}_{nb_file.stem}",
                    "course_name": course_name,
                    "course_folder": course_folder_name,
                    "module_id": mod["id"],
                    "module_name": mod["name"],
                    "filename": nb_file.name,
                    "title": title,
                    "path": rel_path,
                    "difficulty": diff,
                    "is_dummies": is_dummies,
                    "is_homework": is_homework,
                    "edition": edition,
                    "type": "Taller Evaluativo" if is_homework else ("Introducción" if "00" in nb_file.name else "Teoría y Práctica"),
                    "colab_url": f"https://colab.research.google.com/github/{REPO_OWNER}/{REPO_NAME}/blob/{BRANCH}/{encoded_path}",
                    "github_url": f"https://github.com/{REPO_OWNER}/{REPO_NAME}/blob/{BRANCH}/{encoded_path}"
                })

    return notebooks

def scan_course_datasets(course_folder_name, course_dir, course_name=""):
    datasets = []
    seen = set()

    if not course_dir.exists():
        return datasets

    for data_dir in course_dir.rglob("data"):
        if any(part.startswith(".") or part in ["docs", "tmp", "node_modules"] for part in data_dir.parts):
            continue

        if data_dir.is_dir():
            parent_name = data_dir.parent.name
            for csv_file in sorted(data_dir.glob("*.csv")):
                if csv_file.name in seen:
                    continue
                seen.add(csv_file.name)

                rows_count = 100
                cols_count = 5
                headers = []
                sample_data = []
                try:
                    with open(csv_file, 'r', encoding='utf-8', errors='ignore') as f:
                        reader = csv.reader(f)
                        headers = next(reader, [])
                        cols_count = len(headers)
                        # Extract up to 5 sample rows for live preview
                        for _ in range(5):
                            row = next(reader, None)
                            if row is not None:
                                sample_row = {}
                                for i, (h, val) in enumerate(zip(headers, row)):
                                    key = h.strip() if h and h.strip() else f"col_{i+1}"
                                    # Truncate very long cells to keep catalog lightweight
                                    sample_row[key] = (val[:80] + "...") if len(val) > 80 else val
                                sample_data.append(sample_row)
                            else:
                                break
                        rows_count = len(sample_data) + sum(1 for _ in reader) + 1
                except Exception:
                    pass

                features_str = ", ".join(headers[:5]) if headers else "Feature_1, Feature_2..."
                target_str = headers[-1] if headers else "Target"
                rel_path = f"{course_folder_name}/{parent_name}/data/{csv_file.name}"
                encoded_path = urllib.parse.quote(rel_path)
                raw_url = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/{encoded_path}"

                datasets.append({
                    "name": csv_file.name,
                    "course_name": course_name,
                    "module": parent_name,
                    "path": rel_path,
                    "rows": rows_count,
                    "cols": cols_count,
                    "target": target_str,
                    "features": features_str,
                    "description": f"Dataset oficial de práctica para {parent_name} ({course_name})." if course_name else f"Dataset de práctica para {parent_name}.",
                    "sample_data": sample_data,
                    "download_url": raw_url,
                    "raw_url": raw_url,
                    "snippet": f"df = pd.read_csv('{raw_url}')"
                })

    return datasets

def scan_course_guias(course_folder_name, course_dir):
    guias_dir = course_dir / "Guias"
    if not guias_dir.exists():
        return []
    
    guias = []
    idx = 1
    for f in sorted(guias_dir.glob("*.pdf")):
        size_kb = round(f.stat().st_size / 1024)
        size_str = f"{size_kb} KB" if size_kb < 1024 else f"{size_kb/1024:.1f} MB"
        title = format_title(f.name)
        encoded_name = urllib.parse.quote(f.name)

        guias.append({
            "id": f"guia_{idx}",
            "filename": f.name,
            "title": title,
            "module": "🐍 Módulo 01: Python",
            "size_str": size_str,
            "path": f"Guias/{f.name}",
            "raw_url": f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/{urllib.parse.quote(course_folder_name)}/Guias/{encoded_name}",
            "lfs_url": f"https://media.githubusercontent.com/media/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/docs/Guias/{encoded_name}"
        })
        idx += 1
    return guias

def video_sort_key(file_path):
    name = file_path.name.lower()
    if "instalacion" in name or "python" in name:
        return (0, name)
    if "venv" in name or "entorno" in name:
        return (1, name)
    return (2, name)

def scan_course_videos(course_folder_name, course_dir):
    video_dir = course_dir / "Contenido"
    if not video_dir.exists():
        return []

    videos = []
    video_exts = {".mp4", ".mkv", ".webm", ".avi", ".mov"}
    sorted_files = sorted(video_dir.iterdir(), key=video_sort_key)
    idx = 1
    for f in sorted_files:
        if f.is_file() and f.suffix.lower() in video_exts:
            size_mb = round(f.stat().st_size / (1024 * 1024), 1)
            title = format_title(f.name)
            encoded_name = urllib.parse.quote(f.name)
            
            yt_info = KNOWN_YOUTUBE_VIDEOS.get(f.name.lower(), {
                "youtube_id": "",
                "youtube_url": "",
                "embed_url": "",
                "thumbnail": ""
            })

            videos.append({
                "id": f"vid_{idx}",
                "filename": f.name,
                "title": title,
                "module": "🐍 Módulo 01: Python",
                "size_mb": size_mb,
                "path": f"Contenido/{f.name}",
                "youtube_id": yt_info["youtube_id"],
                "youtube_url": yt_info["youtube_url"],
                "embed_url": yt_info["embed_url"],
                "thumbnail": yt_info["thumbnail"],
                "lfs_url": f"https://media.githubusercontent.com/media/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/docs/Contenido/{encoded_name}",
                "raw_url": f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/docs/Contenido/{encoded_name}",
                "github_url": f"https://github.com/{REPO_OWNER}/{REPO_NAME}/blob/{BRANCH}/docs/Contenido/{encoded_name}"
            })
            idx += 1
    return videos

def find_book_cover_image(pdf_stem, libros_dir):
    portadas_dirs = [libros_dir / "Python" / "Portadas", libros_dir / "Portadas"]
    clean_stem = re.sub(r',\s*\d+.*$', '', pdf_stem).strip().lower()
    
    best_img = None
    for p_dir in portadas_dirs:
        if p_dir.exists():
            # 1. Exact match
            for img_file in p_dir.iterdir():
                if img_file.is_file() and img_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp']:
                    img_stem = img_file.stem.strip().lower()
                    if clean_stem == img_stem:
                        best_img = img_file
                        break
            if best_img:
                break
            # 2. Prefix / containment match
            for img_file in p_dir.iterdir():
                if img_file.is_file() and img_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp']:
                    img_stem = img_file.stem.strip().lower()
                    if img_stem == clean_stem or clean_stem.startswith(img_stem) or img_stem.startswith(clean_stem):
                        best_img = img_file
                        break
            if best_img:
                break

    if best_img:
        rel_img = best_img.relative_to(libros_dir).as_posix()
        return '/'.join(urllib.parse.quote(part) for part in f"Libros/{rel_img}".split("/"))
    return ""

def scan_course_books(course_id, c_folder, c_dir):
    books = []
    libros_dir = c_dir / "Libros"
    if not libros_dir.exists():
        return []

    subname = SUBFOLDER_MAP.get(course_id, "Python")

    for f in sorted(libros_dir.rglob("*.pdf")):
        fname = f.name
        key = fname.lower()
        meta = BOOKS_METADATA.get(key, {})
        
        if course_id == "data-science-programming":
            rel_sub = f.relative_to(libros_dir).as_posix()
            web_path = f"Libros/{rel_sub}"
        else:
            web_path = f"Libros/{subname}/{f.name}"

        encoded_web_path = "/".join(urllib.parse.quote(part) for part in web_path.split("/"))
        
        size_mb = f"{round(f.stat().st_size / (1024 * 1024), 1)} MB"
        cover_img_url = find_book_cover_image(f.stem, libros_dir)
        
        title = meta.get("title", format_title(fname))
        subtitle = meta.get("subtitle", f"Biblioteca Digital USTA — {subname}")
        author = meta.get("author", "Referencia Académica")
        publisher = meta.get("publisher", "Editorial Especializada")
        year = meta.get("year", "2024")
        edition = meta.get("edition", "PDF Completo")
        category = meta.get("category", "Ciencia de Datos & Análisis")
        level = meta.get("level", "Intermedio")
        dummies_friendly = meta.get("dummies_friendly", any(k in fname.lower() for k in ["crash", "boring", "head first", "beginner", "best practice", "dummies"]))
        summary_dummies = meta.get("summary_dummies", f"Texto de referencia '{title}' disponible en PDF completo ({size_mb}) para consulta y descarga directa.")
        topics = meta.get("topics", [subname, "Data Science", "Analítica"])
        cover_gradient = meta.get("cover_gradient", "from-teal-600 via-slate-700 to-slate-950")
        cover_bg = meta.get("cover_bg", "#0f766e")
        accent_color = meta.get("accent_color", "#14b8a6")
        icon = meta.get("icon", "📘")
        
        books.append({
            "id": f"book_{course_id}_{len(books) + 1}",
            "course_id": course_id,
            "course_name": c_folder,
            "subject": subname,
            "title": title,
            "filename": fname,
            "subtitle": subtitle,
            "author": author,
            "publisher": publisher,
            "year": year,
            "edition": edition,
            "size_mb": size_mb,
            "cover_image": cover_img_url,
            "has_cover_image": bool(cover_img_url),
            "category": category,
            "level": level,
            "dummies_friendly": dummies_friendly,
            "summary_dummies": summary_dummies,
            "topics": topics,
            "cover_gradient": cover_gradient,
            "cover_bg": cover_bg,
            "accent_color": accent_color,
            "icon": icon,
            "download_url": encoded_web_path,
            "pdf_url": encoded_web_path,
            "has_local_pdf": True,
            "local_pdf_path": web_path
        })
    return books

def rebuild_catalog_js():
    print("🚀 Iniciando escaneo multi-materia de la Especialización...")

    courses_output = []
    all_specialization_datasets = []
    active_course_data = None

    for course_def in COURSE_DEFINITIONS:
        c_id = course_def["id"]
        c_folder = course_def["folder"]
        c_name = course_def["name"]
        c_dir = BASE_DIR / c_folder

        default_mods = COURSE_MODULE_DEFAULTS.get(c_id)

        if c_dir.exists():
            sync_course_assets(c_id, c_folder, c_dir)
            modules = scan_course_modules(c_dir, default_mods)
            notebooks = scan_course_notebooks(c_folder, c_dir, modules, course_name=c_name)
            datasets = scan_course_datasets(c_folder, c_dir, course_name=c_name)
            guias = scan_course_guias(c_folder, c_dir)
            videos = scan_course_videos(c_folder, c_dir)
            books = scan_course_books(c_id, c_folder, c_dir)
        else:
            modules = []
            notebooks = []
            datasets = []
            guias = []
            videos = []
            books = []

        all_specialization_datasets.extend(datasets)

        dummies_count = len([n for n in notebooks if n.get("is_dummies", False)])
        standard_count = len(notebooks) - dummies_count

        stats = {
            "total_notebooks": len(notebooks),
            "total_standard_notebooks": standard_count,
            "total_dummies_notebooks": dummies_count,
            "total_modules": len([m for m in modules if m["id"] != "hw"]),
            "total_homeworks": len([n for n in notebooks if n.get("is_homework", False) or n.get("module_id") == "hw"]),
            "total_datasets": len(datasets),
            "total_guias": len(guias),
            "total_videos": len(videos),
            "total_books": len(books)
        }

        course_obj = {
            **course_def,
            "modules": modules,
            "notebooks": notebooks,
            "datasets": datasets,
            "guias": guias,
            "videos": videos,
            "books": books,
            "stats": stats
        }
        courses_output.append(course_obj)

        if c_id == "data-science-programming":
            active_course_data = course_obj

    if not active_course_data and courses_output:
        active_course_data = courses_output[0]

    all_specialization_books = []
    for c in courses_output:
        all_specialization_books.extend(c.get("books", []))

    # Crear enlaces simbólicos para frontend/public/Libros para soporte de Vite dev
    pub_libros_dir = BASE_DIR / "frontend" / "public" / "Libros"
    pub_libros_dir.mkdir(parents=True, exist_ok=True)
    for sub in ["Data Mining", "Machine Learning", "Visual Analytics"]:
        target = DOCS_DIR / "Libros" / sub
        link = pub_libros_dir / sub
        if target.exists() and not link.exists():
            try:
                rel_target = os.path.relpath(target, pub_libros_dir)
                link.symlink_to(rel_target)
            except Exception:
                pass

    catalog_data = {
        "active_course_id": active_course_data["id"] if active_course_data else "data-science-programming",
        "courses": courses_output,
        "modules": active_course_data["modules"] if active_course_data else [],
        "notebooks": active_course_data["notebooks"] if active_course_data else [],
        "datasets": all_specialization_datasets,
        "stats": active_course_data["stats"] if active_course_data else {},
        "videos": active_course_data["videos"] if active_course_data else [],
        "guias": active_course_data["guias"] if active_course_data else [],
        "books": active_course_data["books"] if active_course_data else [],
        "all_books": all_specialization_books
    }

    # 1. Guardar para plataforma legacy (docs/assets/js/catalog.js)
    js_content = f"// Virtual Laboratory Catalog Database - Auto-generated Multi-Course Architecture\nwindow.VIRTUAL_LAB_CATALOG = {json.dumps(catalog_data, indent=2, ensure_ascii=False)};\nvar VIRTUAL_LAB_CATALOG = window.VIRTUAL_LAB_CATALOG;\n"
    CATALOG_JS_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_JS_PATH.write_text(js_content, encoding="utf-8")
    
    # 2. Guardar para plataforma Vue 3 (frontend/src/data/catalog.js)
    es6_content = f"// Virtual Laboratory Catalog Database - Auto-generated Multi-Course Architecture\nexport const CATALOG_DATA = {json.dumps(catalog_data, indent=2, ensure_ascii=False)};\n"
    FRONTEND_CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    FRONTEND_CATALOG_PATH.write_text(es6_content, encoding="utf-8")
    
    print(f"✅ Catálogo multi-materia reconstruido exitosamente:")
    print(f"   - Total Materias/Asignaturas: {len(courses_output)}")
    print(f"   - Materias Activas: {[c['name'] for c in courses_output if c.get('active')]}")
    print(f"   - Materia Principal: {active_course_data['name']} ({active_course_data['stats']['total_notebooks']} notebooks)")
    print(f"   - Total Datasets Especialización: {len(all_specialization_datasets)}")
    print(f"   - Guardado en: {CATALOG_JS_PATH}")
    print(f"   - Guardado en: {FRONTEND_CATALOG_PATH}")

if __name__ == "__main__":
    rebuild_catalog_js()
