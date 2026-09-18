# Introducción a la Inteligencia Artificial 🧠

> **Especialización en Ciencia de Datos**
> **Universidad Santo Tomás — Seccional Tunja**
> **Nivel Académico:** Semestre II
> **Docente / Gestor Virtual:** Santiago A. Zúñiga M.
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Artificial%20Intelligence-4f46e5?style=for-the-badge&logo=openai&logoColor=white" alt="IA"/>
  <img src="https://img.shields.io/badge/Topics-Búsqueda%20%26%20Lógica-0ea5e9?style=for-the-badge" alt="Temas"/>
  <img src="https://img.shields.io/badge/Course-Introducción%20a%20la%20IA-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

---

## 📌 Descripción de la Asignatura

Fundamentos de Inteligencia Artificial moderna: definición y evolución histórica de la disciplina, identificación de problemas aptos para IA, disciplinas y aplicaciones sectoriales, taxonomía de ramas y tipos de IA, consideraciones éticas, la relación entre IA/Machine Learning/Deep Learning, una introducción a la IA Generativa, algoritmos clásicos de búsqueda (no informada, Greedy Best-First Search y A*) y agentes basados en conocimiento con lógica proposicional, model-checking y resolución sobre forma normal conjuntiva (CNF).

---

## 📚 Estructura Curricular Oficial del Capítulo

El capítulo está estructurado en **6 módulos temáticos correlativos** diseñados con enfoque teórico riguroso, aplicaciones prácticas en Python y guías intuitivas de apoyo:

| # | Módulo Oficial | Temas Principales | Ruta Estándar | Ruta Para Dummies | Taller Práctico |
|:---:|:---|:---|:---:|:---:|:---:|
| **00** | **Fundamentos y Orígenes de la IA** | Definición formal de IA y los 4 enfoques de Russell & Norvig, Historia de la IA (Dartmouth, inviernos de la IA, resurgimiento con Deep Learning y LLMs), El Test de Turing y sus críticas | [Ver Cuadernos](00%20-%20Fundamentos%20y%20Origenes%20de%20la%20IA/) | [Para Dummies](00%20-%20Fundamentos%20y%20Origenes%20de%20la%20IA/Para%20Dummies/) | [Hands-On](homeworks/00_Fundamentos_IA_Hands_On.ipynb) |
| **01** | **Problemas, Disciplinas y Aplicaciones de la IA** | Problemas aptos para IA (diagnóstico médico, supermercados/cajeros, ajedrez, sistemas expertos), disciplinas relacionadas, importancia de la IA como tecnología de propósito general, campos y aplicaciones sectoriales | [Ver Cuadernos](01%20-%20Problemas%20Disciplinas%20y%20Aplicaciones%20de%20la%20IA/) | [Para Dummies](01%20-%20Problemas%20Disciplinas%20y%20Aplicaciones%20de%20la%20IA/Para%20Dummies/) | [Hands-On](homeworks/01_Problemas_Disciplinas_Aplicaciones_Hands_On.ipynb) |
| **02** | **Taxonomía de la Inteligencia Artificial** | Ramas de la IA, Tipos de IA por capacidad (Débil/General/Superinteligencia) y por funcionalidad (taxonomía de Hintze), Solucionador General de Problemas (GPS) de Newell y Simon | [Ver Cuadernos](02%20-%20Taxonomia%20de%20la%20Inteligencia%20Artificial/) | [Para Dummies](02%20-%20Taxonomia%20de%20la%20Inteligencia%20Artificial/Para%20Dummies/) | [Hands-On](homeworks/02_Taxonomia_IA_Hands_On.ipynb) |
| **03** | **Ética y el Nuevo Paradigma de la IA** | Consideraciones éticas (sesgo, privacidad, explicabilidad, regulación), relación IA ⊃ Machine Learning ⊃ Deep Learning, introducción a la IA Generativa | [Ver Cuadernos](03%20-%20Etica%20y%20el%20Nuevo%20Paradigma%20de%20la%20IA/) | [Para Dummies](03%20-%20Etica%20y%20el%20Nuevo%20Paradigma%20de%20la%20IA/Para%20Dummies/) | [Hands-On](homeworks/03_Etica_MLDL_GenAI_Hands_On.ipynb) |
| **04** | **Algoritmos de Búsqueda** | Búsqueda no informada (DFS/BFS) vs. informada, búsqueda de archivos en un sistema de directorios simulado, Greedy Best-First Search, Algoritmo A* | [Ver Cuadernos](04%20-%20Algoritmos%20de%20Busqueda/) | [Para Dummies](04%20-%20Algoritmos%20de%20Busqueda/Para%20Dummies/) | [Hands-On](homeworks/04_Algoritmos_Busqueda_Hands_On.ipynb) |
| **05** | **Agentes Basados en Conocimiento** | Lógica proposicional, modelos y mundos posibles, bases de conocimiento e inferencia, model-checking, forma normal conjuntiva (CNF) y resolución | [Ver Cuadernos](05%20-%20Agentes%20Basados%20en%20Conocimiento/) | [Para Dummies](05%20-%20Agentes%20Basados%20en%20Conocimiento/Para%20Dummies/) | [Hands-On](homeworks/05_Agentes_Conocimiento_Hands_On.ipynb) |

---

## 📝 Talleres Prácticos Evaluativos (Hands-On)

Todos los talleres del capítulo, junto con su ruta guiada **Para Dummies**, están centralizados en la carpeta [`homeworks/`](homeworks/). Consulta [`homeworks/README.md`](homeworks/README.md) para el mapa completo de retos, criterios de entrega e instrucciones de ejecución.

---

## 🧩 Recursos de Código Reutilizables

Los módulos 04 y 05 incluyen, además de los notebooks, scripts standalone ejecutables por línea de comandos que implementan los algoritmos vistos en clase:

* **Módulo 04 — Algoritmos de Búsqueda:** [`file_search.py`](04%20-%20Algoritmos%20de%20Busqueda/file_search.py) (DFS/BFS), [`file_search_gbfs.py`](04%20-%20Algoritmos%20de%20Busqueda/file_search_gbfs.py) (Greedy Best-First Search), [`file_search_astar.py`](04%20-%20Algoritmos%20de%20Busqueda/file_search_astar.py) (A*) — todos operan sobre un sistema de archivos simulado de una empresa ficticia.
* **Módulo 05 — Agentes Basados en Conocimiento:** [`logic.py`](05%20-%20Agentes%20Basados%20en%20Conocimiento/logic.py) (mini-librería de lógica proposicional con `model_check` y resolución sobre CNF), y los casos aplicados [`medico_o_clase.py`](05%20-%20Agentes%20Basados%20en%20Conocimiento/medico_o_clase.py), [`programando.py`](05%20-%20Agentes%20Basados%20en%20Conocimiento/programando.py), [`futbol.py`](05%20-%20Agentes%20Basados%20en%20Conocimiento/futbol.py) y [`perdidos.py`](05%20-%20Agentes%20Basados%20en%20Conocimiento/perdidos.py).

---

## 🛠️ Tecnologías y Librerías Utilizadas

* **Python 3.10+** (Entorno base de ejecución)
* **NumPy, Pandas, Matplotlib** (Cálculo numérico, manejo de datos sintéticos y visualización)
* **Lógica proposicional y algoritmos de búsqueda implementados en Python puro** (sin dependencias externas de IA simbólica)

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Plataforma de Laboratorios Virtuales</i>
  </p>
</div>
