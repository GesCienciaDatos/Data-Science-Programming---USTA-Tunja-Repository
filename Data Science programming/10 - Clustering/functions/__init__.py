# Module 10 clustering functions
# Auto-descarga en Google Colab si functions/ no está en el path
import os as _os, sys as _sys, pathlib as _pathlib

def _ensure_self():
    """Si la carpeta functions/ no está importable, la descarga desde GitHub."""
    _HERE = _pathlib.Path(__file__).parent
    _ROOT = _HERE.parent
    if str(_ROOT) not in _sys.path:
        _sys.path.insert(0, str(_ROOT))

_ensure_self()
