"""
file_search_astar.py
=====================
Especialización en Ciencia de Datos (USTA Tunja) — Introducción a la
Inteligencia Artificial.

Implementa el algoritmo A* (A-estrella) sobre una versión EXTENDIDA del
sistema de archivos simulado de `file_search.py`.

A diferencia de GBFS (que sólo mira h(n)), A* combina:

    f(n) = g(n) + h(n)

    g(n) = costo real acumulado desde la raíz hasta el nodo n
           (en este módulo, 1 salto = 1 de costo).
    h(n) = estimación heurística del costo restante desde n hasta el objetivo.

Si h(n) es ADMISIBLE (nunca sobrestima el costo real restante) y CONSISTENTE
(h(n) <= costo(n, n') + h(n') para cada arista), A* garantiza encontrar el
camino de costo mínimo (es ÓPTIMO) y siempre lo encuentra si existe
(es COMPLETO), explorando además muchos menos nodos "inútiles" que una
búsqueda no informada.

EXTENSIÓN DEL SISTEMA DE ARCHIVOS — "acceso directo" (atajo):
Para poder demostrar la garantía de OPTIMALIDAD de A* de forma concreta,
extendemos el árbol original con una carpeta "AccesosDirectos" en la raíz
que contiene un acceso directo (idéntico a un symlink real de un sistema
operativo) que apunta a la MISMA carpeta "Informes" del ProyectoNorte.
Esto convierte el árbol en un GRAFO con dos rutas posibles hacia
'informe_final.pdf':

    Ruta larga  (4 saltos): ServidorCentral -> ProyectosIngenieria ->
                             ProyectoNorte -> Informes -> informe_final.pdf
    Ruta corta  (3 saltos): ServidorCentral -> AccesosDirectos ->
                             Informes -> informe_final.pdf

La heurística h(n) se calcula UNA SOLA VEZ para todo el grafo (como si un
índice ya hubiese sido construido de antemano, algo común en sistemas de
archivos reales) y se guarda en el atributo `nodo.h_astar`, de modo que sea
consistente sin importar por cuál ruta se llegue a un nodo compartido.
"""

from collections import deque
import heapq

from file_search import Nodo, construir_sistema_archivos, imprimir_arbol


PROFUNDIDAD_MAXIMA_ARBOL = 4  # profundidad máxima conocida del árbol original


def agregar_acceso_directo(raiz, nombre_objetivo="informe_final.pdf"):
    """Extiende el árbol original con una carpeta 'AccesosDirectos' en la
    raíz, cuyo único hijo es una REFERENCIA COMPARTIDA (no una copia) a la
    carpeta 'Informes' que contiene el archivo objetivo.

    Esto convierte el árbol en un grafo dirigido acíclico (DAG) con dos
    rutas posibles hacia el archivo objetivo. Devuelve la raíz modificada.
    """
    carpeta_informes_objetivo = None
    for nodo_proyecto in raiz.hijos:
        if nodo_proyecto.nombre == "ProyectosIngenieria":
            for subproyecto in nodo_proyecto.hijos:
                for hijo in subproyecto.hijos:
                    if hijo.tipo == "carpeta" and any(
                        n.nombre == nombre_objetivo for n in hijo.hijos
                    ):
                        carpeta_informes_objetivo = hijo

    if carpeta_informes_objetivo is None:
        raise ValueError("No se encontró la carpeta 'Informes' que contiene el objetivo.")

    acceso_directo = Nodo("AccesosDirectos", "carpeta", [carpeta_informes_objetivo])
    raiz.agregar_hijo(acceso_directo)
    return raiz


def calcular_heuristica_admisible(raiz, nombre_objetivo):
    """Calcula, para cada nodo alcanzable del grafo, una heurística h(n)
    ADMISIBLE y CONSISTENTE respecto a `nombre_objetivo`, y la guarda en el
    atributo `nodo.h_astar`.

    Estrategia:
      1. Recorre el grafo desde la raíz registrando, para cada nodo, el
         conjunto de sus padres directos (un nodo compartido, como la
         carpeta 'Informes' del atajo, puede tener más de un padre).
      2. Ubica el nodo objetivo.
      3. Ejecuta un BFS "hacia atrás" (de hijo a padre) partiendo del
         objetivo: la distancia mínima encontrada así SÍ es el costo real
         más corto (en saltos) desde cada nodo hasta el objetivo, porque
         helper recorre exactamente las mismas aristas que usaría la
         búsqueda hacia adelante, sólo que en reversa.
      4. A los nodos desde los que el objetivo NO es alcanzable (ninguna
         combinación de hijos llega a él) se les asigna, de forma
         conservadora, `PROFUNDIDAD_MAXIMA_ARBOL` como cota superior: nunca
         sobrestima el costo real porque ningún archivo del sistema está a
         más saltos de profundidad que ese valor.
    """
    padres = {}          # id(nodo) -> set(id(nodo_padre))
    referencia = {}       # id(nodo) -> nodo  (para recuperar el objeto)
    visitados = set()
    pila = [raiz]
    nodo_objetivo = None

    while pila:
        actual = pila.pop()
        if id(actual) in visitados:
            continue
        visitados.add(id(actual))
        referencia[id(actual)] = actual
        if actual.nombre == nombre_objetivo:
            nodo_objetivo = actual
        for hijo in actual.hijos:
            padres.setdefault(id(hijo), set()).add(id(actual))
            if id(hijo) not in visitados:
                pila.append(hijo)

    if nodo_objetivo is None:
        raise ValueError(f"No existe el archivo objetivo '{nombre_objetivo}' en el grafo.")

    # BFS hacia atrás (de hijo a padres) para obtener la distancia real mínima.
    distancia_real = {id(nodo_objetivo): 0}
    cola = deque([id(nodo_objetivo)])
    while cola:
        actual_id = cola.popleft()
        for padre_id in padres.get(actual_id, ()):
            if padre_id not in distancia_real:
                distancia_real[padre_id] = distancia_real[actual_id] + 1
                cola.append(padre_id)

    for id_nodo, nodo in referencia.items():
        nodo.h_astar = distancia_real.get(id_nodo, PROFUNDIDAD_MAXIMA_ARBOL)

    return nodo_objetivo


def astar_buscar(raiz, nombre_objetivo):
    """A* sobre el grafo, asumiendo que cada nodo ya tiene `nodo.h_astar`
    calculado (ver `calcular_heuristica_admisible`). Usa un conjunto
    `cerrados` (closed set): como la heurística es consistente, la PRIMERA
    vez que un nodo sale de la cola de prioridad, es garantizado que fue
    alcanzado por su camino de MENOR costo.
    """
    contador = 0
    f_raiz = 0 + raiz.h_astar
    frontera = [(f_raiz, contador, 0, raiz, [raiz.nombre])]
    cerrados = set()
    orden_visita = []

    while frontera:
        f_actual, _, g_actual, nodo_actual, camino_actual = heapq.heappop(frontera)

        if id(nodo_actual) in cerrados:
            continue
        cerrados.add(id(nodo_actual))
        orden_visita.append(nodo_actual.nombre)

        if nodo_actual.nombre == nombre_objetivo:
            return {
                "encontrado": True,
                "nodo": nodo_actual,
                "camino": camino_actual,
                "orden_visita": orden_visita,
                "nodos_expandidos": len(orden_visita),
                "profundidad": g_actual,
                "costo_total": g_actual,
            }

        for hijo in nodo_actual.hijos:
            if id(hijo) not in cerrados:
                g_hijo = g_actual + 1
                f_hijo = g_hijo + hijo.h_astar
                contador += 1
                heapq.heappush(frontera, (f_hijo, contador, g_hijo, hijo, camino_actual + [hijo.nombre]))

    return {
        "encontrado": False,
        "nodo": None,
        "camino": [],
        "orden_visita": orden_visita,
        "nodos_expandidos": len(orden_visita),
        "profundidad": None,
        "costo_total": None,
    }


if __name__ == "__main__":
    from file_search import dfs_buscar, bfs_buscar, resumen_resultado
    from file_search_gbfs import gbfs_buscar

    print("=" * 70)
    print("DEMOSTRACIÓN: file_search_astar.py — Algoritmo A*")
    print("=" * 70)

    objetivo = "informe_final.pdf"

    raiz = construir_sistema_archivos()
    agregar_acceso_directo(raiz, objetivo)
    calcular_heuristica_admisible(raiz, objetivo)

    print("\nSistema de archivos EXTENDIDO con acceso directo (grafo):\n")
    imprimir_arbol(raiz)

    print("\nHeurística h(n) precalculada para algunos nodos clave:")

    # Búsqueda simple de nodos por nombre para imprimir su heurística (solo demo/depuración)
    def _buscar_por_nombre(nodo, nombre, vistos=None):
        vistos = vistos if vistos is not None else set()
        if id(nodo) in vistos:
            return []
        vistos.add(id(nodo))
        encontrados = [nodo] if nodo.nombre == nombre else []
        for h in nodo.hijos:
            encontrados += _buscar_por_nombre(h, nombre, vistos)
        return encontrados

    for nombre_buscado in ["ServidorCentral", "AccesosDirectos", "ProyectosIngenieria",
                            "ProyectoNorte", "Informes", "informe_final.pdf"]:
        coincidencias = _buscar_por_nombre(raiz, nombre_buscado)
        if coincidencias:
            print(f"  h('{nombre_buscado}') = {coincidencias[0].h_astar}")

    print(f"\nBuscando archivo objetivo: '{objetivo}' con A*, DFS, BFS y GBFS sobre el MISMO grafo extendido\n")

    resultado_astar = astar_buscar(raiz, objetivo)
    resultado_dfs = dfs_buscar(raiz, objetivo)
    resultado_bfs = bfs_buscar(raiz, objetivo)
    resultado_gbfs = gbfs_buscar(raiz, objetivo)

    print(resumen_resultado("A*", resultado_astar))
    print(resumen_resultado("DFS", resultado_dfs))
    print(resumen_resultado("BFS", resultado_bfs))
    print(resumen_resultado("GBFS", resultado_gbfs))

    print("\n" + "-" * 70)
    print(f"{'Algoritmo':<8} | {'Nodos expandidos':<18} | {'Saltos en el camino':<20} | ¿Óptimo (3 saltos)?")
    print("-" * 70)
    for nombre_algo, resultado in [("DFS", resultado_dfs), ("BFS", resultado_bfs),
                                    ("GBFS", resultado_gbfs), ("A*", resultado_astar)]:
        saltos = resultado["profundidad"]
        es_optimo = "Sí" if saltos == 3 else "No"
        print(f"{nombre_algo:<8} | {resultado['nodos_expandidos']:<18} | {saltos!s:<20} | {es_optimo}")

    assert resultado_astar["encontrado"], "A* debe encontrar el archivo objetivo."
    assert resultado_astar["profundidad"] == 3, "A* debe encontrar la ruta óptima de 3 saltos (vía el acceso directo)."
    print("\n✅ Verificación: A* encontró el camino de costo mínimo (3 saltos, vía AccesosDirectos).")
