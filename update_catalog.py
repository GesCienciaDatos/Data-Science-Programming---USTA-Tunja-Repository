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
        "badge": "En Construcción",
        "badge_color": "rose",
        "color": "#f43f5e",
        "gradient": "from-rose-500/20 via-pink-600/10 to-transparent",
        "border_glow": "border-rose-500/40",
        "description": "Metodología KDD, reglas de asociación (Apriori, FP-Growth), detección de valores atípicos y patrones secuenciales en bases de datos complejas.",
        "level": "Especialización",
        "semester": "Semestre II",
        "active": False
    },
    {
        "id": "machine-learning",
        "name": "Machine Learning",
        "title": "Aprendizaje Automático Supervisado y No Supervisado",
        "folder": "Machine Learning",
        "icon": "🧠",
        "badge": "En Construcción",
        "badge_color": "violet",
        "color": "#8b5cf6",
        "gradient": "from-violet-500/20 via-purple-600/10 to-transparent",
        "border_glow": "border-violet-500/40",
        "description": "Algoritmos de clasificación supervisada, ensambles avanzados (Random Forest, XGBoost, LightGBM, CatBoost), clustering no supervisado y optimización de hiperparámetros.",
        "level": "Especialización",
        "semester": "Semestre II",
        "active": False
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
        "title": "Redes Neuronales, Visión y Modelos Generativos",
        "folder": "Introduccion a la Inteligencia Artificial",
        "icon": "🤖",
        "badge": "En Construcción",
        "badge_color": "pink",
        "color": "#ec4899",
        "gradient": "from-pink-500/20 via-rose-600/10 to-transparent",
        "border_glow": "border-pink-500/40",
        "description": "Fundamentos de redes neuronales profundas (Deep Learning) con PyTorch, visión computacional, procesamiento del lenguaje natural (NLP) y fundamentos de LLMs.",
        "level": "Especialización",
        "semester": "Semestre II",
        "active": False
    },
    {
        "id": "visual-analytics",
        "name": "Visual Analytics and Critical Thinking",
        "title": "Analítica Visual y Pensamiento Crítico",
        "folder": "Visual Analytics and Critical Thinking",
        "icon": "👁️",
        "badge": "En Construcción",
        "badge_color": "emerald",
        "color": "#10b981",
        "gradient": "from-emerald-500/20 via-teal-600/10 to-transparent",
        "border_glow": "border-emerald-500/40",
        "description": "Tableros analíticos interactivos con Plotly, Dash y Streamlit, principios de percepción visual y cognitiva, y comunicación de hallazgos para la toma de decisiones.",
        "level": "Especialización",
        "semester": "Semestre II",
        "active": False
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
        "id": "hw",
        "name": "homeworks",
        "title": "Talleres Prácticos Evaluativos (Hands-On)",
        "icon": "📝",
        "color": "#DC2626",
        "description": "Talleres integradores de resolución autónoma con datos reales y desafíos de negocio."
    }
]

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

def format_title(filename):
    for k, v in KNOWN_TITLES.items():
        if k.lower() == filename.lower():
            return v
    clean = filename.replace(".ipynb", "").replace(".pdf", "").replace(".mp4", "").replace(".mkv", "").replace(".webm", "")
    clean = re.sub(r'^\d+[a-z]?_', '', clean)
    clean = clean.replace("_compressed", "").replace("_", " ").replace("-", " ")
    words = clean.strip().split()
    capitalized = " ".join(w.capitalize() if len(w) > 2 else w.lower() for w in words)
    return capitalized.capitalize()

def infer_difficulty(title, path):
    text = f"{title} {path}".lower()
    if any(k in text for k in ["intro", "conceptos", "basico", "sintaxis", "creacion"]):
        return "Básico"
    if any(k in text for k in ["avanzado", "regularizacion", "knn", "pca", "poo", "clases"]):
        return "Avanzado"
    return "Intermedio"

def sync_course_assets(course_dir):
    """Sincroniza Guias/, Contenido/ y Libros/ del curso hacia docs/"""
    for folder_name in ["Guias", "Contenido", "Libros"]:
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

def scan_course_modules(course_dir, default_modules=None):
    modules = list(default_modules) if default_modules else []
    existing_ids = {m["id"] for m in modules}

    if course_dir.exists() and course_dir.is_dir():
        for item in sorted(course_dir.iterdir()):
            if item.is_dir() and not item.name.startswith("."):
                match = re.match(r'^(\d{2})\s*-\s*(.+)$', item.name)
                if match:
                    mod_id = match.group(1)
                    if mod_id not in existing_ids:
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
                elif item.name.lower() == "homeworks" and "hw" not in existing_ids:
                    modules.append({
                        "id": "hw",
                        "name": "homeworks",
                        "title": "Talleres Prácticos Evaluativos (Hands-On)",
                        "icon": "📝",
                        "color": "#DC2626",
                        "description": "Talleres integradores de resolución autónoma con datos reales y desafíos de negocio."
                    })
                    existing_ids.add("hw")
    return modules

BOOKS_CATALOG = [
    {
        "id": "book_1",
        "title": "Python for Data Analysis",
        "subtitle": "Data Wrangling with Pandas, NumPy, and Jupyter",
        "author": "Wes McKinney",
        "year": "2022",
        "edition": "3rd Edition",
        "publisher": "O'Reilly Media",
        "category": "Python & Pandas",
        "level": "Básico a Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Escrito por el creador original de Pandas. Es el manual definitivo para manipular tablas, limpiar datos y operar arrays numéricos sin enredarse.",
        "topics": ["Python", "NumPy", "Pandas", "Jupyter", "Data Cleaning"],
        "cover_gradient": "from-sky-600 to-blue-900",
        "icon": "🐼",
        "open_access_url": "https://wesmckinney.com/book/",
        "github_url": "https://github.com/wesm/pydata-book",
        "official_url": "https://www.oreilly.com/library/view/python-for-data/9781098104023/"
    },
    {
        "id": "book_2",
        "title": "Hands-On Machine Learning",
        "subtitle": "with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques",
        "author": "Aurélien Géron",
        "year": "2022",
        "edition": "3rd Edition",
        "publisher": "O'Reilly Media",
        "category": "Machine Learning",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": True,
        "summary_dummies": "La biblia práctica de Machine Learning mundial. Explica desde una regresión lineal simple hasta redes neuronales profundas con ejemplos claros paso a paso.",
        "topics": ["Scikit-Learn", "Regresión", "Clasificación", "Keras", "TensorFlow"],
        "cover_gradient": "from-emerald-600 to-teal-900",
        "icon": "🤖",
        "open_access_url": "https://github.com/ageron/handson-ml3",
        "github_url": "https://github.com/ageron/handson-ml3",
        "official_url": "https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/"
    },
    {
        "id": "book_3",
        "title": "An Introduction to Statistical Learning",
        "subtitle": "with Applications in Python (ISLP)",
        "author": "G. James, D. Witten, T. Hastie, R. Tibshirani, J. Taylor",
        "year": "2023",
        "edition": "Python Edition",
        "publisher": "Springer",
        "category": "Estadística & ML",
        "level": "Intermedio",
        "dummies_friendly": False,
        "summary_dummies": "El estándar de oro académico para entender la matemática y fundamento estadístico detrás de cada modelo de predicción, clasificación y remuestreo.",
        "topics": ["Regresión Lineal", "Regularización Ridge/Lasso", "Árboles", "Inferencia", "PCA"],
        "cover_gradient": "from-indigo-600 to-slate-900",
        "icon": "📈",
        "open_access_url": "https://www.statlearning.com/",
        "github_url": "https://github.com/intro-stat-learning/ISLP",
        "official_url": "https://www.statlearning.com/"
    },
    {
        "id": "book_4",
        "title": "Practical Statistics for Data Scientists",
        "subtitle": "50+ Essential Concepts Using R and Python",
        "author": "Peter Bruce, Andrew Bruce, Peter Gedeck",
        "year": "2020",
        "edition": "2nd Edition",
        "publisher": "O'Reilly Media",
        "category": "Estadística & EDA",
        "level": "Básico a Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "¿Odiabas las fórmulas abstractas de la universidad? Este libro rescata los 50 conceptos que realmente necesitas en Ciencia de Datos explicados con total sentido práctico.",
        "topics": ["EDA", "Distribuciones", "Pruebas de Hipótesis", "Muestreo", "Significancia"],
        "cover_gradient": "from-amber-600 to-yellow-900",
        "icon": "📊",
        "open_access_url": "https://github.com/gedeck/practical-statistics-for-data-scientists",
        "github_url": "https://github.com/gedeck/practical-statistics-for-data-scientists",
        "official_url": "https://www.oreilly.com/library/view/practical-statistics-for/9781492072935/"
    },
    {
        "id": "book_5",
        "title": "Automate the Boring Stuff with Python",
        "subtitle": "Practical Programming for Total Beginners",
        "author": "Al Sweigart",
        "year": "2019",
        "edition": "2nd Edition",
        "publisher": "No Starch Press",
        "category": "Para Dummies / Principiantes",
        "level": "Básico (100% Dummies)",
        "dummies_friendly": True,
        "summary_dummies": "¡El mejor libro para quienes nunca han programado en su vida! Aprende a automatizar archivos de Excel, tareas repetitivas y scripts útiles en minutos.",
        "topics": ["Sintaxis Básica", "Archivos", "Excel", "Automatización", "Scraping"],
        "cover_gradient": "from-rose-600 to-pink-900",
        "icon": "💡",
        "open_access_url": "https://automatetheboringstuff.com/",
        "github_url": "https://github.com/asweigart",
        "official_url": "https://automatetheboringstuff.com/"
    },
    {
        "id": "book_6",
        "title": "Storytelling with Data",
        "subtitle": "A Data Visualization Guide for Business Professionals",
        "author": "Cole Nussbaumer Knaflic",
        "year": "2015",
        "edition": "1st Edition",
        "publisher": "Wiley",
        "category": "Visualización & Storytelling",
        "level": "Básico a Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Tus gráficos no deben ser adornos confusos. Aprende a eliminar el ruido visual, captar la atención de tu audiencia y comunicar decisiones claras con datos.",
        "topics": ["Visualización", "Storytelling", "Diseño de Gráficos", "Comunicación Ejecutiva"],
        "cover_gradient": "from-purple-600 to-violet-900",
        "icon": "🎨",
        "open_access_url": "https://www.storytellingwithdata.com/books",
        "github_url": "https://www.storytellingwithdata.com/",
        "official_url": "https://www.storytellingwithdata.com/books"
    },
    {
        "id": "book_7",
        "title": "Python Data Science Handbook",
        "subtitle": "Essential Tools for Working with Data",
        "author": "Jake VanderPlas",
        "year": "2023",
        "edition": "2nd Edition",
        "publisher": "O'Reilly Media",
        "category": "Python & Fundamentos",
        "level": "Básico a Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Texto libre completo disponible en Jupyter Notebooks. Cubre a fondo IPython, NumPy, Pandas, Matplotlib y Scikit-Learn de forma estructurada y pedagógica.",
        "topics": ["IPython", "NumPy", "Pandas", "Matplotlib", "Scikit-Learn"],
        "cover_gradient": "from-cyan-600 to-teal-900",
        "icon": "🐍",
        "open_access_url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
        "github_url": "https://github.com/jakevdp/PythonDataScienceHandbook",
        "official_url": "https://jakevdp.github.io/PythonDataScienceHandbook/"
    },
    {
        "id": "book_8",
        "title": "Feature Engineering for Machine Learning",
        "subtitle": "Principles and Techniques for Data Scientists",
        "author": "Alice Zheng, Amanda Casari",
        "year": "2018",
        "edition": "1st Edition",
        "publisher": "O'Reilly Media",
        "category": "Feature Engineering",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Los mejores modelos no provienen del algoritmo más complejo, sino de cómo preparas tus variables: One-Hot, escalado, transformaciones logarítmicas y PCA.",
        "topics": ["Encoding", "Escalamiento", "Texto/NLP", "Reducción Dimensional", "PCA"],
        "cover_gradient": "from-fuchsia-600 to-purple-900",
        "icon": "⚙️",
        "open_access_url": "https://github.com/alicezheng/feature-engineering-book",
        "github_url": "https://github.com/alicezheng/feature-engineering-book",
        "official_url": "https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/"
    },
    {
        "id": "book_9",
        "title": "Naked Statistics",
        "subtitle": "Stripping the Dread from the Data",
        "author": "Charles Wheelan",
        "year": "2013",
        "edition": "1st Edition",
        "publisher": "W. W. Norton & Company",
        "category": "Para Dummies / Principiantes",
        "level": "Básico (100% Dummies)",
        "dummies_friendly": True,
        "summary_dummies": "¡El libro más divertido sobre estadística! Cero fórmulas intimidantes, lleno de humor, analogías de concursos de TV y ejemplos de la vida real.",
        "topics": ["Intuición Estadística", "Correlación vs Causalidad", "Probabilidad", "Inferencia"],
        "cover_gradient": "from-orange-600 to-amber-900",
        "icon": "🎯",
        "open_access_url": "https://wwnorton.com/books/9780393347777/about-the-book/product-details",
        "github_url": "https://wwnorton.com/books/9780393347777",
        "official_url": "https://wwnorton.com/books/9780393347777/about-the-book/product-details"
    },
    {
        "id": "book_10",
        "title": "Fluent Python",
        "subtitle": "Clear, Concise, and Effective Programming",
        "author": "Luciano Ramalho",
        "year": "2022",
        "edition": "2nd Edition",
        "publisher": "O'Reilly Media",
        "category": "Python Avanzado",
        "level": "Avanzado",
        "dummies_friendly": False,
        "summary_dummies": "Para cuando quieras dar el salto a escribir código Python verdaderamente idiomático, elegante, de alto rendimiento y con POO profesional.",
        "topics": ["Data Model", "Generadores", "Decoradores", "Concurrencia", "Tipado"],
        "cover_gradient": "from-emerald-700 to-slate-900",
        "icon": "⚡",
        "open_access_url": "https://github.com/fluentpython/example-code-2e",
        "github_url": "https://github.com/fluentpython/example-code-2e",
        "official_url": "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"
    },
    {
        "id": "book_11",
        "title": "Data Science from Scratch",
        "subtitle": "First Principles with Python",
        "author": "Joel Grus",
        "year": "2019",
        "edition": "2nd Edition",
        "publisher": "O'Reilly Media",
        "category": "Python & Algoritmos",
        "level": "Intermedio",
        "dummies_friendly": True,
        "summary_dummies": "Construye cada algoritmo de Ciencia de Datos desde cero (álgebra lineal, gradiente descendente, KNN, regresión) para entender cómo funcionan por dentro.",
        "topics": ["Álgebra Lineal", "Gradiente", "KNN", "Regresión", "Naive Bayes"],
        "cover_gradient": "from-teal-600 to-cyan-950",
        "icon": "🧪",
        "open_access_url": "https://github.com/joelgrus/data-science-from-scratch",
        "github_url": "https://github.com/joelgrus/data-science-from-scratch",
        "official_url": "https://www.oreilly.com/library/view/data-science-from/9781492041122/"
    },
    {
        "id": "book_12",
        "title": "Deep Learning with Python",
        "subtitle": "Second Edition",
        "author": "François Chollet",
        "year": "2021",
        "edition": "2nd Edition",
        "publisher": "Manning Publications",
        "category": "Machine Learning",
        "level": "Intermedio a Avanzado",
        "dummies_friendly": True,
        "summary_dummies": "Escrito por el creador de Keras. Desmitifica las redes neuronales con explicaciones visuales, metáforas geométricas y código claro sin matemáticas abrumadoras.",
        "topics": ["Redes Neuronales", "Keras", "Computer Vision", "NLP", "Generative AI"],
        "cover_gradient": "from-red-600 to-rose-950",
        "icon": "🧠",
        "open_access_url": "https://github.com/fchollet/deep-learning-with-python-notebooks",
        "github_url": "https://github.com/fchollet/deep-learning-with-python-notebooks",
        "official_url": "https://www.manning.com/books/deep-learning-with-python-second-edition"
    }
]

def scan_course_notebooks(course_folder_name, course_dir, modules):
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
                if is_dummies:
                    clean_title = raw_title.replace(" Dummies", "").replace(" dummies", "")
                    title = f"💡 {clean_title} [Dummies] {mod['icon']}"
                    diff = "Básico (Dummies)"
                    edition = "Para Dummies"
                else:
                    title = f"{raw_title} {mod['icon']}"
                    diff = infer_difficulty(raw_title, rel_path)
                    edition = "Estándar"

                encoded_path = urllib.parse.quote(rel_path)

                notebooks.append({
                    "id": f"{mod['id']}_{nb_file.stem}",
                    "module_id": mod["id"],
                    "module_name": mod["name"],
                    "filename": nb_file.name,
                    "title": title,
                    "path": rel_path,
                    "difficulty": diff,
                    "is_dummies": is_dummies,
                    "edition": edition,
                    "type": "Taller Evaluativo" if mod["id"] == "hw" else ("Introducción" if "00" in nb_file.name else "Teoría y Práctica"),
                    "colab_url": f"https://colab.research.google.com/github/{REPO_OWNER}/{REPO_NAME}/blob/{BRANCH}/{encoded_path}",
                    "github_url": f"https://github.com/{REPO_OWNER}/{REPO_NAME}/blob/{BRANCH}/{encoded_path}"
                })

    return notebooks

def scan_course_datasets(course_folder_name, course_dir):
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
                try:
                    with open(csv_file, 'r', encoding='utf-8', errors='ignore') as f:
                        reader = csv.reader(f)
                        headers = next(reader, [])
                        cols_count = len(headers)
                        rows_count = sum(1 for _ in reader) + 1
                except Exception:
                    pass

                features_str = ", ".join(headers[:5]) if headers else "Feature_1, Feature_2..."
                target_str = headers[-1] if headers else "Target"
                rel_path = f"{course_folder_name}/{parent_name}/data/{csv_file.name}"
                encoded_path = urllib.parse.quote(rel_path)

                datasets.append({
                    "name": csv_file.name,
                    "module": parent_name,
                    "path": rel_path,
                    "rows": rows_count,
                    "cols": cols_count,
                    "target": target_str,
                    "features": features_str,
                    "description": f"Dataset de práctica para {parent_name}.",
                    "snippet": f"df = pd.read_csv('https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/{encoded_path}')"
                })

    return datasets

def scan_course_guias(course_folder_name, course_dir):
    guias_dir = course_dir / "Guias"
    if not guias_dir.exists():
        guias_dir = DOCS_DIR / "Guias"
    
    guias = []
    if guias_dir.exists():
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
        video_dir = DOCS_DIR / "Contenido"

    videos = []
    video_exts = {".mp4", ".mkv", ".webm", ".avi", ".mov"}
    if video_dir.exists():
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

def scan_course_books(c_folder, c_dir):
    books = [dict(b) for b in BOOKS_CATALOG]
    libros_dir = c_dir / "Libros"
    if libros_dir.exists():
        for f in sorted(libros_dir.rglob("*.pdf")):
            fname = f.name
            rel_sub = f.relative_to(libros_dir).as_posix()
            web_path = f"Libros/{rel_sub}"
            encoded_web_path = "/".join(urllib.parse.quote(part) for part in web_path.split("/"))
            
            clean_title = format_title(fname)
            
            # Comprobar si ya coincide con alguno del catálogo curado
            matched = False
            for b in books:
                if b["title"].lower() in clean_title.lower() or clean_title.lower() in b["title"].lower():
                    b["local_pdf_path"] = web_path
                    b["pdf_url"] = encoded_web_path
                    b["has_local_pdf"] = True
                    b["filename"] = fname
                    matched = True
                    break
            
            if not matched:
                is_dummies = any(k in fname.lower() for k in ["crash", "boring", "head first", "beginner", "best practice", "cookbook"])
                books.append({
                    "id": f"local_book_{len(books) + 1}",
                    "title": clean_title,
                    "filename": fname,
                    "subtitle": f"Biblioteca Digital USTA — {f.parent.name if f.parent != libros_dir else 'Python'}",
                    "author": "Referencia Académica Especializada",
                    "year": "2024",
                    "edition": "PDF Completo",
                    "publisher": "Biblioteca Digital USTA",
                    "category": "Para Dummies / Principiantes" if is_dummies else "Python & Pandas",
                    "level": "Básico a Intermedio" if is_dummies else "Intermedio",
                    "dummies_friendly": is_dummies,
                    "summary_dummies": f"Texto de referencia '{clean_title}' disponible en PDF completo para lectura y descarga directa.",
                    "topics": ["Python", "Programación", "Data Science", "Algoritmos"],
                    "cover_gradient": "from-teal-600 to-slate-900",
                    "icon": "📘",
                    "open_access_url": encoded_web_path,
                    "pdf_url": encoded_web_path,
                    "has_local_pdf": True,
                    "github_url": "",
                    "official_url": "",
                    "local_pdf_path": web_path
                })
    return books

def rebuild_catalog_js():
    print("🚀 Iniciando escaneo multi-materia de la Especialización...")

    courses_output = []
    active_course_data = None

    for course_def in COURSE_DEFINITIONS:
        c_id = course_def["id"]
        c_folder = course_def["folder"]
        c_dir = BASE_DIR / c_folder

        if c_id == "data-science-programming":
            sync_course_assets(c_dir)
            modules = scan_course_modules(c_dir, DEFAULT_MODULES_DSP)
            notebooks = scan_course_notebooks(c_folder, c_dir, modules)
            datasets = scan_course_datasets(c_folder, c_dir)
            guias = scan_course_guias(c_folder, c_dir)
            videos = scan_course_videos(c_folder, c_dir)
            books = scan_course_books(c_folder, c_dir)
        else:
            modules = scan_course_modules(c_dir) if c_dir.exists() else []
            notebooks = scan_course_notebooks(c_folder, c_dir, modules) if c_dir.exists() else []
            datasets = scan_course_datasets(c_folder, c_dir) if c_dir.exists() else []
            guias = scan_course_guias(c_folder, c_dir) if c_dir.exists() else []
            videos = scan_course_videos(c_folder, c_dir) if c_dir.exists() else []
            books = scan_course_books(c_folder, c_dir) if c_dir.exists() else BOOKS_CATALOG

        dummies_count = len([n for n in notebooks if n.get("is_dummies", False)])
        standard_count = len(notebooks) - dummies_count

        stats = {
            "total_notebooks": len(notebooks),
            "total_standard_notebooks": standard_count,
            "total_dummies_notebooks": dummies_count,
            "total_modules": len([m for m in modules if m["id"] != "hw"]),
            "total_homeworks": len([n for n in notebooks if n["module_id"] == "hw"]),
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

        if course_def.get("active", False):
            active_course_data = course_obj

    if not active_course_data and courses_output:
        active_course_data = courses_output[0]

    catalog_data = {
        "active_course_id": active_course_data["id"] if active_course_data else "data-science-programming",
        "courses": courses_output,
        "modules": active_course_data["modules"] if active_course_data else [],
        "notebooks": active_course_data["notebooks"] if active_course_data else [],
        "datasets": active_course_data["datasets"] if active_course_data else [],
        "stats": active_course_data["stats"] if active_course_data else {},
        "videos": active_course_data["videos"] if active_course_data else [],
        "guias": active_course_data["guias"] if active_course_data else [],
        "books": active_course_data["books"] if active_course_data else books
    }

    js_content = f"// Virtual Laboratory Catalog Database - Auto-generated Multi-Course Architecture\nwindow.VIRTUAL_LAB_CATALOG = {json.dumps(catalog_data, indent=2, ensure_ascii=False)};\nvar VIRTUAL_LAB_CATALOG = window.VIRTUAL_LAB_CATALOG;\n"
    CATALOG_JS_PATH.write_text(js_content, encoding="utf-8")
    
    print(f"✅ Catálogo multi-materia reconstruido exitosamente:")
    print(f"   - Total Materias/Asignaturas: {len(courses_output)}")
    print(f"   - Materia Activa: {active_course_data['name']} ({active_course_data['stats']['total_notebooks']} notebooks)")

if __name__ == "__main__":
    rebuild_catalog_js()
