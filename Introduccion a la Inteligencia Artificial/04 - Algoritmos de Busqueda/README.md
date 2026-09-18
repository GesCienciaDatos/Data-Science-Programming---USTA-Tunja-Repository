# Módulo 04: Algoritmos de Búsqueda 🧭🔎

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Inteligencia%20Artificial-4f46e5?style=for-the-badge&logo=github&logoColor=white" alt="Inteligencia Artificial"/>
  <img src="https://img.shields.io/badge/Algoritmos-DFS%20%7C%20BFS%20%7C%20GBFS%20%7C%20A*-0ea5e9?style=for-the-badge" alt="Algoritmos"/>
  <img src="https://img.shields.io/badge/Course-Introducci%C3%B3n%20a%20la%20IA-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al módulo de **Algoritmos de Búsqueda** de la asignatura **Introducción a la Inteligencia Artificial** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**.

---

## 🧭 ¿De qué trata este módulo?

Gran parte de los problemas clásicos de la Inteligencia Artificial se pueden formular como un **problema de búsqueda** en un espacio de estados: un agente parte de un estado inicial y debe encontrar una secuencia de acciones que lo lleve a un estado meta.

Este es el módulo **más orientado a código** de todo el capítulo. A lo largo de los 4 cuadernos implementamos, con Python real y ejecutable (no pseudocódigo), los cuatro algoritmos de búsqueda clásicos de la IA —**DFS**, **BFS**, **Greedy Best-First Search (GBFS)** y **A\* (A-estrella)**— aplicados a un mismo caso de estudio coherente de principio a fin: **buscar un archivo específico (`informe_final.pdf`) dentro del sistema de directorios simulado de la empresa ficticia *Constructora Horizonte Andino S.A.S.***, sin tocar el sistema de archivos real de ningún computador.

---

## 📚 Estructura Curricular del Módulo

### 🎓 1. Cuadernos Académicos Estándar:
1. [**00_Fundamentos_de_Busqueda_No_Informada.ipynb**](00_Fundamentos_de_Busqueda_No_Informada.ipynb): El problema de búsqueda en IA, los conceptos de frontera / nodo explorado / estado meta, búsqueda no informada vs. informada, el trade-off memoria-tiempo entre BFS y DFS, y las limitaciones de la búsqueda no informada (espacios infinitos, ciclos).
2. [**01_Busqueda_en_Sistemas_de_Archivos_DFS_BFS.ipynb**](01_Busqueda_en_Sistemas_de_Archivos_DFS_BFS.ipynb): Modelado del sistema de archivos como una clase `Nodo` reutilizable, e implementación completa de **DFS** y **BFS**, comparando su orden de exploración y el camino encontrado.
3. [**02_Busqueda_Informada_Greedy_Best_First_Search.ipynb**](02_Busqueda_Informada_Greedy_Best_First_Search.ipynb): Construcción de una heurística de similitud de nombres y del algoritmo **GBFS**; análisis de por qué es "voraz" y no garantiza optimalidad.
4. [**03_Algoritmo_A_Estrella.ipynb**](03_Algoritmo_A_Estrella.ipynb): El algoritmo **A\*** ($f(n) = g(n) + h(n)$), heurísticas admisibles y consistentes, extensión del sistema de archivos con un acceso directo (grafo) para demostrar la garantía de optimalidad, y comparación final **A\* vs. GBFS vs. BFS vs. DFS**.

---

### 🐍 2. Módulos Python Reutilizables (*Standalone*):
1. [**file_search.py**](file_search.py): Clase `Nodo`, construcción del sistema de archivos simulado, e implementación de `dfs_buscar()` y `bfs_buscar()`.
2. [**file_search_gbfs.py**](file_search_gbfs.py): Heurística de similitud de nombres (`heuristica_similitud_nombre()`) e implementación de `gbfs_buscar()`.
3. [**file_search_astar.py**](file_search_astar.py): Extensión del sistema de archivos con un acceso directo (`agregar_acceso_directo()`), cálculo de una heurística admisible (`calcular_heuristica_admisible()`) e implementación de `astar_buscar()`.

Cada uno de estos archivos puede ejecutarse de forma independiente (`python3 file_search.py`) e imprime una demostración completa en consola.

---

### 📝 3. Taller Práctico Evaluativo (*Hands-On*):
* [**../homeworks/04_Algoritmos_Busqueda_Hands_On.ipynb**](../homeworks/04_Algoritmos_Busqueda_Hands_On.ipynb): Aplicación práctica y evaluada de DFS, BFS, GBFS y A* sobre variaciones del sistema de archivos simulado.

---

### 🧸 4. Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/):
1. [**00_Busqueda_No_Informada_Dummies.ipynb**](Para%20Dummies/00_Busqueda_No_Informada_Dummies.ipynb): ¿Cómo busca una computadora algo perdido? La analogía de la oficina con archivadores.
2. [**01_DFS_BFS_Dummies.ipynb**](Para%20Dummies/01_DFS_BFS_Dummies.ipynb): DFS y BFS, las dos formas de buscar a ciegas.
3. [**02_GBFS_Dummies.ipynb**](Para%20Dummies/02_GBFS_Dummies.ipynb): GBFS, el detective que sigue el olfato (y a veces se equivoca).
4. [**03_A_Estrella_Dummies.ipynb**](Para%20Dummies/03_A_Estrella_Dummies.ipynb): A\*, el GPS que nunca se equivoca.

---

## 🏢 El Caso de Estudio: Constructora Horizonte Andino S.A.S.

Los 4 cuadernos estándar comparten el mismo sistema de archivos simulado (una empresa ficticia con las áreas `Gerencia`, `Finanzas`, `ProyectosIngenieria` y `RecursosHumanos`), y el mismo archivo objetivo: **`informe_final.pdf`**, ubicado en `ProyectosIngenieria/ProyectoNorte/Informes/`. En el cuaderno de A\* este árbol se extiende con un **acceso directo** (convirtiéndolo en un grafo) para demostrar, con código real, la garantía de optimalidad del algoritmo.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Asignatura: Introducción a la Inteligencia Artificial</i>
  </p>
</div>
