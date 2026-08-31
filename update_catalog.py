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
    """Sincroniza Guias/ y Contenido/ del curso hacia docs/Guias/ y docs/Contenido/"""
    for folder_name in ["Guias", "Contenido"]:
        src = course_dir / folder_name
        dest = DOCS_DIR / folder_name
        dest.mkdir(parents=True, exist_ok=True)
        if src.exists() and src.is_dir():
            for item in src.iterdir():
                if item.is_file():
                    target_file = dest / item.name
                    if not target_file.exists() or target_file.stat().st_mtime < item.stat().st_mtime:
                        shutil.copy2(item, target_file)
                        print(f"  [SYNC] Copiado: {item.name} -> docs/{folder_name}/")

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

def scan_course_notebooks(course_folder_name, course_dir, modules):
    notebooks = []
    
    for mod in modules:
        mod_dir = course_dir / mod["name"]
        if mod_dir.exists() and mod_dir.is_dir():
            for nb_file in sorted(mod_dir.glob("*.ipynb")):
                if ".ipynb_checkpoints" in str(nb_file):
                    continue
                
                rel_path = f"{course_folder_name}/{mod['name']}/{nb_file.name}"
                title = format_title(nb_file.name)
                diff = infer_difficulty(title, rel_path)
                encoded_path = urllib.parse.quote(rel_path)

                notebooks.append({
                    "id": f"{mod['id']}_{nb_file.name}",
                    "module_id": mod["id"],
                    "module_name": mod["name"],
                    "filename": nb_file.name,
                    "title": f"{title} {mod['icon']}",
                    "path": rel_path,
                    "difficulty": diff,
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

def scan_course_videos(course_folder_name, course_dir):
    video_dir = course_dir / "Contenido"
    if not video_dir.exists():
        video_dir = DOCS_DIR / "Contenido"

    videos = []
    video_exts = {".mp4", ".mkv", ".webm", ".avi", ".mov"}
    if video_dir.exists():
        idx = 1
        for f in sorted(video_dir.iterdir()):
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
        else:
            modules = scan_course_modules(c_dir) if c_dir.exists() else []
            notebooks = scan_course_notebooks(c_folder, c_dir, modules) if c_dir.exists() else []
            datasets = scan_course_datasets(c_folder, c_dir) if c_dir.exists() else []
            guias = scan_course_guias(c_folder, c_dir) if c_dir.exists() else []
            videos = scan_course_videos(c_folder, c_dir) if c_dir.exists() else []

        stats = {
            "total_notebooks": len(notebooks),
            "total_modules": len([m for m in modules if m["id"] != "hw"]),
            "total_homeworks": len([n for n in notebooks if n["module_id"] == "hw"]),
            "total_datasets": len(datasets),
            "total_guias": len(guias),
            "total_videos": len(videos)
        }

        course_obj = {
            **course_def,
            "modules": modules,
            "notebooks": notebooks,
            "datasets": datasets,
            "guias": guias,
            "videos": videos,
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
        "guias": active_course_data["guias"] if active_course_data else []
    }

    js_content = f"// Virtual Laboratory Catalog Database - Auto-generated Multi-Course Architecture\nwindow.VIRTUAL_LAB_CATALOG = {json.dumps(catalog_data, indent=2, ensure_ascii=False)};\nvar VIRTUAL_LAB_CATALOG = window.VIRTUAL_LAB_CATALOG;\n"
    CATALOG_JS_PATH.write_text(js_content, encoding="utf-8")
    
    print(f"✅ Catálogo multi-materia reconstruido exitosamente:")
    print(f"   - Total Materias/Asignaturas: {len(courses_output)}")
    print(f"   - Materia Activa: {active_course_data['name']} ({active_course_data['stats']['total_notebooks']} notebooks)")

if __name__ == "__main__":
    rebuild_catalog_js()
