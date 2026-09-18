"""
file_search_gbfs.py
====================
Especialización en Ciencia de Datos (USTA Tunja) — Introducción a la
Inteligencia Artificial.

Implementa el algoritmo de Búsqueda Voraz Primero el Mejor
(Greedy Best-First Search, GBFS) sobre el mismo sistema de archivos
simulado definido en `file_search.py`.

GBFS es un algoritmo de BÚSQUEDA INFORMADA: usa una función heurística
h(n) que ESTIMA qué tan "cerca" está un nodo del objetivo, y en cada paso
expande el nodo de la frontera con el MENOR valor de h(n), sin importar
cuánto le costó llegar hasta ahí (ignora g(n), el costo acumulado).
Por eso se dice que es "voraz" (greedy): toma la decisión que luce mejor
en el momento, sin garantía de que sea la mejor a largo plazo.

La heurística usada aquí es una heurística de SIMILITUD DE TEXTO entre el
nombre de cada nodo y el nombre del archivo objetivo (basada en
`difflib.SequenceMatcher`). Es una heurística "de sentido común" -parecida
a cómo un humano buscaría a ojo por nombres parecidos- pero, como se
demuestra en el notebook 02, NO es una heurística admisible: puede
subestimar Y sobrestimar la distancia real, lo que hace que GBFS pueda
desviarse a callejones sin salida antes de llegar al objetivo.
"""

import heapq
from difflib import SequenceMatcher

from file_search import Nodo, construir_sistema_archivos, imprimir_arbol


def heuristica_similitud_nombre(nombre_nodo, nombre_objetivo):
    """Heurística h(n): entre menor sea el valor devuelto, más "prometedor"
    parece el nodo para GBFS.

    h(n) = 1 - similitud_texto(nombre_nodo, nombre_objetivo)

    similitud_texto está en [0, 1], donde 1 = nombres idénticos.
    Por lo tanto h(n) está en [0, 1], donde 0 = coincidencia perfecta.
    """
    similitud = SequenceMatcher(None, nombre_nodo.lower(), nombre_objetivo.lower()).ratio()
    return round(1 - similitud, 4)


def gbfs_buscar(raiz, nombre_objetivo, funcion_heuristica=heuristica_similitud_nombre):
    """Greedy Best-First Search usando una cola de prioridad (heap) ordenada
    únicamente por h(n).

    Se usa un contador `orden_insercion` como criterio de desempate para que
    `heapq` nunca intente comparar objetos `Nodo` directamente entre sí.
    """
    contador = 0
    h_raiz = funcion_heuristica(raiz.nombre, nombre_objetivo)
    frontera = [(h_raiz, contador, raiz, [raiz.nombre])]
    explorados = {id(raiz)}
    orden_visita = []
    nodos_evaluados_h = [(raiz.nombre, h_raiz)]

    while frontera:
        h_actual, _, nodo_actual, camino_actual = heapq.heappop(frontera)
        orden_visita.append(nodo_actual.nombre)

        if nodo_actual.nombre == nombre_objetivo:
            return {
                "encontrado": True,
                "nodo": nodo_actual,
                "camino": camino_actual,
                "orden_visita": orden_visita,
                "nodos_expandidos": len(orden_visita),
                "profundidad": len(camino_actual) - 1,
                "historial_heuristica": nodos_evaluados_h,
            }

        for hijo in nodo_actual.hijos:
            if id(hijo) not in explorados:
                explorados.add(id(hijo))
                contador += 1
                h_hijo = funcion_heuristica(hijo.nombre, nombre_objetivo)
                nodos_evaluados_h.append((hijo.nombre, h_hijo))
                heapq.heappush(frontera, (h_hijo, contador, hijo, camino_actual + [hijo.nombre]))

    return {
        "encontrado": False,
        "nodo": None,
        "camino": [],
        "orden_visita": orden_visita,
        "nodos_expandidos": len(orden_visita),
        "profundidad": None,
        "historial_heuristica": nodos_evaluados_h,
    }


if __name__ == "__main__":
    from file_search import dfs_buscar, bfs_buscar, resumen_resultado

    print("=" * 70)
    print("DEMOSTRACIÓN: file_search_gbfs.py — Greedy Best-First Search")
    print("=" * 70)

    raiz = construir_sistema_archivos()
    objetivo = "informe_final.pdf"

    print(f"\nBuscando archivo objetivo: '{objetivo}' con GBFS\n")
    resultado_gbfs = gbfs_buscar(raiz, objetivo)
    print(resumen_resultado("GBFS", resultado_gbfs))
    print(f"  Orden de exploración GBFS: {resultado_gbfs['orden_visita']}")

    print("\nHeurísticas h(n) calculadas para los hijos directos de la raíz:")
    for nombre, h in resultado_gbfs["historial_heuristica"][:6]:
        print(f"  h('{nombre}') = {h}")

    # Comparación rápida contra la búsqueda no informada
    resultado_bfs = bfs_buscar(raiz, objetivo)
    resultado_dfs = dfs_buscar(raiz, objetivo)
    print("\nComparación de nodos expandidos hasta encontrar el objetivo:")
    print(f"  DFS : {resultado_dfs['nodos_expandidos']} nodos")
    print(f"  BFS : {resultado_bfs['nodos_expandidos']} nodos")
    print(f"  GBFS: {resultado_gbfs['nodos_expandidos']} nodos")

    assert resultado_gbfs["encontrado"], "GBFS debe encontrar el archivo objetivo."
    print("\n✅ Verificación: GBFS encontró el archivo objetivo correctamente.")
