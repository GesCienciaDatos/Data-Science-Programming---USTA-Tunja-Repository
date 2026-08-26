#!/usr/bin/env python3
"""
update_catalog.py
Script de automatización para escanear y sincronizar Guias, Contenido, Cuadernos y Datasets
con el catálogo JavaScript del Laboratorio Virtual (docs/assets/js/catalog.js).
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

DEFAULT_MODULES = [
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

def format_title(filename):
    clean = filename.replace(".ipynb", "").replace(".pdf", "").replace(".mp4", "")
    clean = re.sub(r'^\d+[a-z]?_', '', clean)
    clean = clean.replace("_compressed", "").replace("_", " ").replace("-", " ")
    return clean.strip().capitalize()

def infer_difficulty(title, path):
    text = f"{title} {path}".lower()
    if any(k in text for k in ["intro", "conceptos", "basico", "sintaxis", "creacion"]):
        return "Básico"
    if any(k in text for k in ["avanzado", "regularizacion", "knn", "pca", "poo", "clases"]):
        return "Avanzado"
    return "Intermedio"

def sync_folders():
    """Sincroniza Guias/ y Contenido/ hacia docs/Guias/ y docs/Contenido/"""
    for folder_name in ["Guias", "Contenido"]:
        src = BASE_DIR / folder_name
        dest = DOCS_DIR / folder_name
        dest.mkdir(parents=True, exist_ok=True)
        if src.exists():
            for item in src.iterdir():
                if item.is_file():
                    target_file = dest / item.name
                    if not target_file.exists() or target_file.stat().st_mtime < item.stat().st_mtime:
                        shutil.copy2(item, target_file)
                        print(f"  [SYNC] Copiado: {item.name} -> docs/{folder_name}/")

def scan_modules():
    modules = list(DEFAULT_MODULES)
    existing_ids = {m["id"] for m in modules}

    for item in sorted(BASE_DIR.iterdir()):
        if item.is_dir():
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
    return modules

def scan_notebooks(modules):
    notebooks = []
    
    # 1. Escanear carpetas de módulos
    for mod in modules:
        mod_dir = BASE_DIR / mod["name"]
        if mod_dir.exists() and mod_dir.is_dir():
            for nb_file in sorted(mod_dir.glob("*.ipynb")):
                if ".ipynb_checkpoints" in str(nb_file):
                    continue
                
                rel_path = f"{mod['name']}/{nb_file.name}"
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

def scan_datasets():
    datasets = []
    seen = set()

    for data_dir in BASE_DIR.rglob("data"):
        if data_dir.is_dir() and ".git" not in str(data_dir):
            parent_name = data_dir.parent.name
            for csv_file in sorted(data_dir.glob("*.csv")):
                if csv_file.name in seen:
                    continue
                seen.add(csv_file.name)

                # Intentar leer filas y columnas
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
                rel_path = f"{parent_name}/data/{csv_file.name}"
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

def scan_guias():
    guias_dir = BASE_DIR / "Guias"
    if not guias_dir.exists():
        guias_dir = DOCS_DIR / "Guias"
    
    guias = []
    if guias_dir.exists():
        idx = 1
        for f in sorted(guias_dir.glob("*.pdf")):
            size_kb = round(f.stat().st_size / 1024)
            size_str = f"{size_kb} KB" if size_kb < 1024 else f"{size_kb/1024:.1f} MB"
            clean_title = format_title(f.name)
            title = clean_title if clean_title.lower().startswith("guía") or clean_title.lower().startswith("guia") else f"Guía de {clean_title}"
            encoded_name = urllib.parse.quote(f.name)

            guias.append({
                "id": f"guia_{idx}",
                "filename": f.name,
                "title": title,
                "module": "🐍 Módulo 01: Python",
                "size_str": size_str,
                "path": f"Guias/{f.name}",
                "raw_url": f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/Guias/{encoded_name}",
                "lfs_url": f"https://media.githubusercontent.com/media/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/docs/Guias/{encoded_name}"
            })
            idx += 1
    return guias

def scan_videos():
    video_dir = BASE_DIR / "Contenido"
    if not video_dir.exists():
        video_dir = DOCS_DIR / "Contenido"

    videos = []
    video_exts = {".mp4", ".mkv", ".webm", ".avi", ".mov"}
    if video_dir.exists():
        idx = 1
        for f in sorted(video_dir.iterdir()):
            if f.is_file() and f.suffix.lower() in video_exts:
                size_mb = round(f.stat().st_size / (1024 * 1024), 1)
                clean_title = format_title(f.name)
                encoded_name = urllib.parse.quote(f.name)

                videos.append({
                    "id": f"vid_{idx}",
                    "filename": f.name,
                    "title": clean_title,
                    "module": "🐍 Módulo 01: Python",
                    "size_mb": size_mb,
                    "path": f"Contenido/{f.name}",
                    "lfs_url": f"https://media.githubusercontent.com/media/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/docs/Contenido/{encoded_name}",
                    "raw_url": f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/docs/Contenido/{encoded_name}",
                    "github_url": f"https://github.com/{REPO_OWNER}/{REPO_NAME}/blob/{BRANCH}/docs/Contenido/{encoded_name}"
                })
                idx += 1
    return videos

def rebuild_catalog_js():
    print("🚀 Iniciando escaneo completo del repositorio...")
    sync_folders()
    modules = scan_modules()
    notebooks = scan_notebooks(modules)
    datasets = scan_datasets()
    guias = scan_guias()
    videos = scan_videos()

    catalog_data = {
        "modules": modules,
        "notebooks": notebooks,
        "datasets": datasets,
        "stats": {
            "total_notebooks": len(notebooks),
            "total_modules": len([m for m in modules if m["id"] != "hw"]),
            "total_homeworks": len([n for n in notebooks if n["module_id"] == "hw"]),
            "total_datasets": len(datasets),
            "total_guias": len(guias),
            "total_videos": len(videos)
        },
        "videos": videos,
        "guias": guias
    }

    js_content = f"// Virtual Laboratory Catalog Database - Auto-generated\nconst VIRTUAL_LAB_CATALOG = {json.dumps(catalog_data, indent=2, ensure_ascii=False)};\n"
    CATALOG_JS_PATH.write_text(js_content, encoding="utf-8")
    
    print(f"✅ Catálogo reconstruido exitosamente en docs/assets/js/catalog.js:")
    print(f"   - Módulos: {len(modules)}")
    print(f"   - Cuadernos: {len(notebooks)}")
    print(f"   - Datasets: {len(datasets)}")
    print(f"   - Guías PDF: {len(guias)}")
    print(f"   - Videos: {len(videos)}")

if __name__ == "__main__":
    rebuild_catalog_js()
