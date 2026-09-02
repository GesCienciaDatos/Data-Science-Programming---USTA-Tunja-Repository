"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  setup_colab.py — Módulo 10: Clustering                                     ║
║  Descarga el paquete functions/ desde GitHub para ejecución en Colab.       ║
╚══════════════════════════════════════════════════════════════════════════════╝

Si ves el error:
    ModuleNotFoundError: No module named 'functions'

Pega este bloque en una celda NUEVA al inicio del cuaderno y ejecútalo:

─────────────────────────────────────────────────────────────────────────────
import urllib.request, os
exec(urllib.request.urlopen(
    'https://raw.githubusercontent.com/sazuniga06/'
    'Data-Science-Programming---USTA-Tunja-Repository/main/'
    'Data%20Science%20programming/10%20-%20Clustering/setup_colab.py'
).read())
─────────────────────────────────────────────────────────────────────────────
"""
import urllib.request, os, sys
from pathlib import Path

_BASE = (
    "https://raw.githubusercontent.com/sazuniga06/"
    "Data-Science-Programming---USTA-Tunja-Repository/main/"
    "Data%20Science%20programming/10%20-%20Clustering/"
)

_FILES = [
    "functions/__init__.py",
    "functions/dendrogram_util.py",
    "functions/clustering_metrics.py",
]

print("📦 Configurando paquete functions/ para Colab...")
Path("functions").mkdir(exist_ok=True)

for f in _FILES:
    dest = Path(f)
    url  = _BASE + f.replace(" ", "%20")
    print(f"  ↓ {f}", end=" ... ")
    urllib.request.urlretrieve(url, dest)
    print("✅")

cwd = os.getcwd()
if cwd not in sys.path:
    sys.path.insert(0, cwd)

# Verificación rápida
try:
    from functions.dendrogram_util import plot_dendrogram, plot_node
    from functions.clustering_metrics import wss, bss, correlation
    print("\n✅ Todo listo. Puedes ejecutar las celdas del cuaderno normalmente.")
except Exception as e:
    print(f"\n❌ Error en verificación: {e}")
