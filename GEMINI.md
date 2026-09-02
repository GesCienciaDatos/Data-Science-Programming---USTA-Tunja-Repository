## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

**Grafo actual:** 3,825 nodos · 6,350 aristas · 257 comunidades
(Regenerar con: `graphify update .` — solo AST local, sin costo de API)

### Reglas de Uso

- Para preguntas sobre la base de código, ejecuta primero `graphify query "<pregunta>"` cuando exista `graphify-out/graph.json`. Usa `graphify path "<A>" "<B>"` para relaciones entre componentes y `graphify explain "<concepto>"` para nodos específicos. Estos comandos retornan un subgrafo acotado, generalmente mucho más pequeño que `GRAPH_REPORT.md` o búsquedas crudas con grep.
- Si existe `graphify-out/wiki/index.md`, úsalo para navegación de alto nivel en lugar de explorar archivos fuente directamente.
- Lee `graphify-out/GRAPH_REPORT.md` solo para revisiones de arquitectura general o cuando `query/path/explain` no ofrezcan suficiente contexto.
- **Después de modificar archivos de código en esta sesión**, ejecuta `graphify update .` para mantener el grafo actualizado (solo AST, sin costo de API ni LLM).

### Archivos auto-generados (no versionados)

Los siguientes artefactos se generan automáticamente y están excluidos del repositorio via `.gitignore`:
- `graphify-out/` — grafo, reporte, HTML interactivo y árbol D3
- `.graphify_analysis.json` — métricas de análisis incremental
- `.graphify_labels.json` — etiquetas de comunidades
- `.graphify_manifest.json` — manifiesto de archivos procesados
