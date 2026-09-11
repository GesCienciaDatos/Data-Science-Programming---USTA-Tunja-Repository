# ⚡ Power Query — ETL para Power BI

## Descripción

Esta sección cubre **Power Query**, el motor ETL (Extract, Transform, Load) integrado en Power BI y Excel. Los cuadernos muestran cada operación en su equivalente Python/Pandas, permitiendo al estudiante trasladar el conocimiento entre ambos entornos.

> La franja verde esmeralda (`#10b981`) identifica todos los cuadernos de esta sección.

---

## Estructura

```
Power Query/
├── 00_Intro_Power_Query.ipynb          ← Qué es, lenguaje M, Editor Avanzado
├── 01_Transformaciones_Power_Query.ipynb ← Merge, Append, Pivot, Unpivot, limpieza
├── 02_Power_Query_vs_Pandas.ipynb      ← Tabla comparativa completa (referencia)
└── Para Dummies/
    └── 00_Power_Query_Dummies.ipynb    ← Explicación sin tecnicismos
```

---

## Contenido de cada cuaderno

| Cuaderno | Temas | Nivel |
|---|---|---|
| `00_Intro_Power_Query` | Arquitectura ETL, lenguaje M `let...in`, GUI vs código | Introductorio |
| `01_Transformaciones` | Merge (JOIN), Append (UNION), Pivot, Unpivot (melt), limpieza, columnas condicionales | Intermedio |
| `02_PQ_vs_Pandas` | Tabla exhaustiva de equivalencias: cargar, filtrar, agrupar, fechas, texto | Referencia |
| `00_PQ_Dummies` | Los 5 problemas más comunes y cómo resolverlos | Básico |

---

## Equivalencias Rápidas: M ↔ Pandas

| Operación | Power Query (M) | Pandas (Python) |
|---|---|---|
| Cargar CSV | `Csv.Document(File.Contents("data.csv"))` | `pd.read_csv("data.csv")` |
| Filtrar filas | `Table.SelectRows(t, each [col] > 100)` | `df[df['col'] > 100]` |
| Quitar nulos | `Table.SelectRows(t, each [col] <> null)` | `df.dropna(subset=['col'])` |
| Agrupar | `Table.Group(t, {"cat"}, {"Suma", each List.Sum([v])})` | `df.groupby('cat')['v'].sum()` |
| Combinar tablas | `Table.NestedJoin(t1, "id", t2, "id", "nuevo", JoinKind.Inner)` | `pd.merge(df1, df2, on='id')` |
| Apilar tablas | `Table.Combine({t1, t2, t3})` | `pd.concat([df1, df2, df3])` |
| Despivotar | `Table.Unpivot(t, {"Norte","Sur"}, "Region", "Ventas")` | `df.melt(id_vars=['Mes'], var_name='Region', value_name='Ventas')` |
| Columna calculada | `Table.AddColumn(t, "Nuevo", each [v1] + [v2])` | `df['Nuevo'] = df['v1'] + df['v2']` |
| Renombrar | `Table.RenameColumns(t, {{"viejo", "nuevo"}})` | `df.rename(columns={'viejo': 'nuevo'})` |
| Eliminar duplicados | `Table.Distinct(t)` | `df.drop_duplicates()` |

---

## Recursos de Aprendizaje Adicionales

- [📚 Documentación oficial M Language](https://learn.microsoft.com/es-es/powerquery-m/)
- [📺 Guy in a Cube — Power BI YouTube](https://www.youtube.com/@GuyInACube)
- [📺 Exceleinfo — Power Query en español](https://www.youtube.com/@exceleinfo)
- [🐍 Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

---

*Universidad Santo Tomás — Seccional Tunja | Especialización en Ciencia de Datos*
