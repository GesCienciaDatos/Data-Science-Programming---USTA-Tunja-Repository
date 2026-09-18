"""
file_search.py
================
Módulo reutilizable para la Especialización en Ciencia de Datos (USTA Tunja) —
Asignatura: Introducción a la Inteligencia Artificial.

Implementa:
  * La clase `Nodo`, que representa una carpeta o un archivo dentro de un
    sistema de directorios SIMULADO (no se toca el sistema de archivos real).
  * `construir_sistema_archivos()`: construye el árbol de ejemplo de la
    empresa ficticia "Constructora Horizonte Andino S.A.S." que se reutiliza
    en los 4 notebooks del módulo "Algoritmos de Búsqueda".
  * Búsqueda No Informada:
        - `dfs_buscar()`  -> Depth-First Search (búsqueda en profundidad)
        - `bfs_buscar()`  -> Breadth-First Search (búsqueda en anchura)
  * Utilidades comunes: impresión del árbol y formateo de resultados.

Este archivo puede importarse desde otros scripts o notebooks con:
    from file_search import Nodo, construir_sistema_archivos, dfs_buscar, bfs_buscar
"""

from collections import deque


class Nodo:
    """Representa un elemento del sistema de archivos simulado.

    Un Nodo es una CARPETA (puede tener hijos) o un ARCHIVO (nodo hoja,
    normalmente sin hijos). Esta clase modela el "estado" que los algoritmos
    de búsqueda de IA exploran: cada Nodo es un estado del espacio de
    búsqueda, y sus `hijos` son los estados sucesores alcanzables desde él.
    """

    def __init__(self, nombre, tipo="carpeta", hijos=None):
        if tipo not in ("carpeta", "archivo"):
            raise ValueError("tipo debe ser 'carpeta' o 'archivo'")
        self.nombre = nombre
        self.tipo = tipo
        self.hijos = list(hijos) if hijos else []

    def es_carpeta(self):
        return self.tipo == "carpeta"

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    def __repr__(self):
        icono = "📁" if self.es_carpeta() else "📄"
        return f"{icono} {self.nombre}"


def construir_sistema_archivos():
    """Construye y devuelve la raíz del sistema de archivos simulado.

    Estructura de la empresa ficticia "Constructora Horizonte Andino S.A.S.":
    un servidor central con 4 grandes áreas (Gerencia, Finanzas,
    ProyectosIngenieria y RecursosHumanos). El archivo objetivo que se
    buscará a lo largo de todo el módulo es 'informe_final.pdf', ubicado en
    ProyectosIngenieria/ProyectoNorte/Informes/informe_final.pdf (profundidad 4).
    """
    raiz = Nodo("ServidorCentral", "carpeta", [
        Nodo("Gerencia", "carpeta", [
            Nodo("Actas", "carpeta", [
                Nodo("acta_comite_enero.docx", "archivo"),
                Nodo("acta_comite_febrero.docx", "archivo"),
            ]),
            Nodo("Estrategia", "carpeta", [
                Nodo("plan_estrategico_2026.pptx", "archivo"),
                Nodo("presupuesto_anual.xlsx", "archivo"),
            ]),
        ]),
        Nodo("Finanzas", "carpeta", [
            Nodo("Contabilidad", "carpeta", [
                Nodo("balance_general.xlsx", "archivo"),
                Nodo("estado_resultados.xlsx", "archivo"),
                Nodo("Auditorias", "carpeta", [
                    Nodo("auditoria_2024.pdf", "archivo"),
                    Nodo("auditoria_2025.pdf", "archivo"),
                ]),
            ]),
            Nodo("Tesoreria", "carpeta", [
                Nodo("flujo_caja.xlsx", "archivo"),
                Nodo("pagos_proveedores.csv", "archivo"),
            ]),
        ]),
        Nodo("ProyectosIngenieria", "carpeta", [
            Nodo("ProyectoNorte", "carpeta", [
                Nodo("planos_estructurales.dwg", "archivo"),
                Nodo("fotos_obra.zip", "archivo"),
                Nodo("Informes", "carpeta", [
                    Nodo("informe_avance_q1.pdf", "archivo"),
                    Nodo("informe_avance_q2.pdf", "archivo"),
                    Nodo("informe_final.pdf", "archivo"),   # <-- OBJETIVO
                ]),
            ]),
            Nodo("ProyectoSur", "carpeta", [
                Nodo("planos_estructurales.dwg", "archivo"),
                Nodo("Informes", "carpeta", [
                    Nodo("informe_avance_q1.pdf", "archivo"),
                    Nodo("informe_preliminar.pdf", "archivo"),
                ]),
            ]),
        ]),
        Nodo("RecursosHumanos", "carpeta", [
            Nodo("Nomina", "carpeta", [
                Nodo("nomina_septiembre.xlsx", "archivo"),
            ]),
            Nodo("Contratos", "carpeta", [
                Nodo("contrato_empleado_001.pdf", "archivo"),
                Nodo("contrato_empleado_002.pdf", "archivo"),
            ]),
        ]),
    ])
    return raiz


def imprimir_arbol(nodo, prefijo="", es_ultimo=True, es_raiz=True):
    """Imprime el sistema de archivos simulado como un árbol en consola."""
    conector = "" if es_raiz else ("└── " if es_ultimo else "├── ")
    print(f"{prefijo}{conector}{nodo}")
    nuevo_prefijo = prefijo if es_raiz else prefijo + ("    " if es_ultimo else "│   ")
    for i, hijo in enumerate(nodo.hijos):
        imprimir_arbol(hijo, nuevo_prefijo, i == len(nodo.hijos) - 1, es_raiz=False)


def _empaquetar_resultado(encontrado, nodo_objetivo, camino, orden_visita, nodos_expandidos):
    return {
        "encontrado": encontrado,
        "nodo": nodo_objetivo,
        "camino": camino,                    # lista de nombres desde la raíz hasta el objetivo
        "orden_visita": orden_visita,         # nombres en el orden en que fueron EXPANDIDOS
        "nodos_expandidos": nodos_expandidos,
        "profundidad": (len(camino) - 1) if camino else None,
    }


def dfs_buscar(raiz, nombre_objetivo):
    """Depth-First Search (búsqueda en profundidad) iterativa, con pila.

    Explora primero el hijo más "profundo" de la rama actual antes de
    retroceder (backtrack) a probar la siguiente rama disponible. Usa un
    conjunto `explorados` para no volver a expandir un nodo ya visitado
    (buena práctica defensiva ante ciclos, aunque en este árbol no existan).
    """
    pila = [(raiz, [raiz.nombre])]
    explorados = set()
    orden_visita = []

    while pila:
        nodo_actual, camino_actual = pila.pop()
        if id(nodo_actual) in explorados:
            continue
        explorados.add(id(nodo_actual))
        orden_visita.append(nodo_actual.nombre)

        if nodo_actual.nombre == nombre_objetivo:
            return _empaquetar_resultado(True, nodo_actual, camino_actual, orden_visita, len(orden_visita))

        # Se agregan los hijos en orden inverso para que, al usar pila (LIFO),
        # el primer hijo de la lista sea el primero en explorarse.
        for hijo in reversed(nodo_actual.hijos):
            if id(hijo) not in explorados:
                pila.append((hijo, camino_actual + [hijo.nombre]))

    return _empaquetar_resultado(False, None, [], orden_visita, len(orden_visita))


def bfs_buscar(raiz, nombre_objetivo):
    """Breadth-First Search (búsqueda en anchura), con cola FIFO.

    Explora TODOS los nodos de un nivel de profundidad antes de pasar al
    siguiente nivel. Marca un nodo como "explorado" en el momento en que
    se DESCUBRE (se agrega a la frontera), no cuando se expande; esto es lo
    que garantiza que, en un grafo con costos uniformes, BFS encuentre
    siempre el camino de MENOR número de saltos hacia el objetivo.
    """
    frontera = deque([(raiz, [raiz.nombre])])
    explorados = {id(raiz)}
    orden_visita = []

    while frontera:
        nodo_actual, camino_actual = frontera.popleft()
        orden_visita.append(nodo_actual.nombre)

        if nodo_actual.nombre == nombre_objetivo:
            return _empaquetar_resultado(True, nodo_actual, camino_actual, orden_visita, len(orden_visita))

        for hijo in nodo_actual.hijos:
            if id(hijo) not in explorados:
                explorados.add(id(hijo))
                frontera.append((hijo, camino_actual + [hijo.nombre]))

    return _empaquetar_resultado(False, None, [], orden_visita, len(orden_visita))


def resumen_resultado(nombre_algoritmo, resultado):
    """Devuelve una cadena legible con el resumen de un resultado de búsqueda."""
    if not resultado["encontrado"]:
        return f"[{nombre_algoritmo}] No se encontró el archivo. Nodos expandidos: {resultado['nodos_expandidos']}"
    camino_txt = " → ".join(resultado["camino"])
    return (
        f"[{nombre_algoritmo}] Encontrado en profundidad {resultado['profundidad']} "
        f"tras expandir {resultado['nodos_expandidos']} nodos.\n"
        f"  Camino: {camino_txt}"
    )


if __name__ == "__main__":
    print("=" * 70)
    print("DEMOSTRACIÓN: file_search.py — DFS y BFS sobre el sistema simulado")
    print("=" * 70)

    raiz = construir_sistema_archivos()
    print("\nSistema de archivos simulado:\n")
    imprimir_arbol(raiz)

    objetivo = "informe_final.pdf"
    print(f"\nBuscando archivo objetivo: '{objetivo}'\n")

    resultado_dfs = dfs_buscar(raiz, objetivo)
    resultado_bfs = bfs_buscar(raiz, objetivo)

    print(resumen_resultado("DFS", resultado_dfs))
    print(f"  Orden de exploración DFS: {resultado_dfs['orden_visita']}\n")

    print(resumen_resultado("BFS", resultado_bfs))
    print(f"  Orden de exploración BFS: {resultado_bfs['orden_visita']}\n")

    assert resultado_dfs["encontrado"] and resultado_bfs["encontrado"], "El archivo objetivo debe encontrarse."
    assert resultado_dfs["camino"] == resultado_bfs["camino"], "En un árbol el camino hacia un nodo es único."
    print("✅ Verificación: ambos algoritmos coinciden en el camino (único, por ser un árbol).")
