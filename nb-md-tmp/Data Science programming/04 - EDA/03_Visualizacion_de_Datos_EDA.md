# 03_Visualizacion_de_Datos_EDA

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Visualización de Datos y el Cuarteto de Anscombe 📈
      </h1>
      <p style="margin: 6px 0 0 0; color: #1e3a8a; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Programación para Ciencia de Datos
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #1e3a8a; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Módulo 04
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/04%20-%20EDA/03_Visualizacion_de_Datos_EDA.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Visualización de Datos 

Por defecto, **Pandas** viene con la librería `matplotlib` incorporada, lo que nos permite hacer gráficos rápidos y sencillos. Sin embargo, para crear visualizaciones mucho más atractivas e informativas desde el punto de vista estadístico, utilizamos **Seaborn**.

> Seaborn es una librería de visualización de datos en Python basada en `matplotlib`. Proporciona una interfaz de alto nivel para dibujar gráficos estadísticos atractivos e informativos.

Comencemos importando nuestras herramientas y cargando el misterioso dataset de cuartetos.

```python
import os
import urllib.parse
import urllib.request
import pandas as pd

# 🚀 Función de utilidad para cargar datasets de forma segura (Local o Google Colab)
def load_dataset(filename, module_name="04 - EDA"):
    candidates = [
        f"data/{filename}",
        f"{module_name}/data/{filename}",
        filename
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
            
    os.makedirs("data", exist_ok=True)
    target_path = f"data/{filename}"
    encoded_module = urllib.parse.quote(module_name)
    encoded_file = urllib.parse.quote(filename)
    url_main = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/{encoded_module}/data/{encoded_file}"
    url_master = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/master/{encoded_module}/data/{encoded_file}"
    
    print(f"📥 Descargando dataset '{filename}' desde el repositorio oficial...")
    try:
        urllib.request.urlretrieve(url_main, target_path)
    except Exception:
        urllib.request.urlretrieve(url_master, target_path)
    print(f"✅ Dataset '{filename}' cargado exitosamente.")
    return target_path

# Carga del Cuarteto de Anscombe
file_path = load_dataset('quartets.csv', '04 - EDA')
df = pd.read_csv(file_path, index_col=0)
df.head()
```

---
### 1. Diagramas de Caja (BoxPlot) 📦

Los diagramas de caja proporcionan un resumen de la distribución, incluyendo la mediana, los cuartiles y los posibles valores atípicos (outliers). 

- La **caja** representa el Rango Intercuartílico (IQR = Q3 - Q1).
- Los **bigotes** se extienden hasta los valores mínimos y máximos dentro de un rango determinado. Por defecto, se extienden no más de `1.5 * IQR` desde los bordes de la caja.
- Los **valores atípicos** se trazan como puntos separados.

#### 1.1 Boxplots con Pandas
Pandas nos permite generar boxplots agrupados de forma muy directa.

```python
quartets.groupby('quartet').boxplot(grid=False, figsize=(10, 4));
```

#### 1.2 Paletas de Colores de Seaborn

📚 **Documentación:** [Paletas de Seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html)

Antes de usar Seaborn, configuremos una paleta de colores para mejorar la estética.

```python
sns.color_palette('pastel')
```

```python
palette = 'pastel'
```

#### 1.3 Boxplots con Seaborn
Podemos crear diagramas de caja similares usando Matplotlib y Seaborn en conjunto.

```python
fig, axes = plt.subplots(2, 2, figsize=(8, 7))
axes = axes.flatten().tolist()

for quartet, g in quartets.groupby('quartet'):
    ax = axes.pop(0)
    sns.boxplot(data=g, ax=ax, palette=palette)
    ax.set_title(f'Cuarteto {quartet}')
    
plt.suptitle("Boxplots de los cuartetos");
plt.tight_layout()
```

#### 1.4 Unificando características con `pd.melt()`

📚 **Documentación:** 
- [seaborn.boxplot()](https://seaborn.pydata.org/generated/seaborn.boxplot.html)
- [pandas.melt()](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)

Podemos derretir (melt) el DataFrame para comparar las características `x` e `y` en el mismo gráfico.

```python
melted = pd.melt(quartets, id_vars='quartet', var_name='variable', value_name='value')
display(melted.head())

fig, ax = plt.subplots(1, 1, figsize=(16, 4))
sns.boxplot(x='variable', y='value', hue='quartet', data=melted, ax=ax, palette=palette)
ax.set_title("Características unificadas de los cuartetos");
```

**⚠️ El problema con el gráfico anterior** es que estamos forzando características diferentes (como `x` e `y`) a compartir el mismo eje Y. 

Por lo tanto, otra forma de lograr el objetivo es iterar por columna:

```python
fig, axes = plt.subplots(1, 2, figsize=(16, 4))
for i, col in enumerate(['x', 'y']):
    sns.boxplot(x='quartet', y=col, data=quartets, ax=axes[i], palette=palette)
    axes[i].set_title(f'variable {col}')
```

---
##### 🛠️ Práctica 1: Boxplots Modificados
El rango por defecto de los bigotes (whiskers) en un boxplot es `1.5 * IQR`. Tu tarea es graficar los diagramas de caja de los 4 cuartetos con Seaborn (usando la variable `y`), pero esta vez extiende los bigotes **hasta el máximo y mínimo absolutos** de los datos para que no queden valores atípicos (puntos sueltos).
*(Pista: revisa el parámetro `whis`)*

```python
# Escribe tu código aquí
fig, ax = plt.subplots(figsize=(10, 4))
# sns.boxplot(x=..., y=..., data=..., whis=...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
sns.boxplot(x='quartet', y='y', data=quartets, ax=ax, whis=float('inf'), palette=palette)
```
</details>

---
### 2. Histogramas 📊

Los histogramas proporcionan una representación visual de la distribución de una variable continua. Los datos se dividen en contenedores (bins), y la altura de cada barra representa la frecuencia o recuento de observaciones dentro de ese contenedor.

#### 2.1 Histogramas en Pandas
Pandas nos permite graficar fácilmente el histograma de las características de cada cuarteto en una sola línea de código.

```python
quartets.groupby('quartet').hist(figsize=(10, 6));
```

Los histogramas nos permiten empezar a ver algunas diferencias entre los grupos.

#### 2.2 Histogramas en Seaborn
📚 **Documentación:** [seaborn.histplot()](https://seaborn.pydata.org/generated/seaborn.histplot.html)

Podemos hacer lo mismo con Seaborn agrupando y dibujando la curva KDE (estimación de densidad de kernel):

```python
for quartet, g in quartets.groupby('quartet'):
    fig, axes = plt.subplots(1 , 2, figsize=(8, 2.5))
    sns.histplot(data=g, x="x", hue='quartet', ax=axes[0], palette=palette, bins=10, kde=True)
    sns.histplot(data=g, x="y", hue='quartet', ax=axes[1], palette=palette, bins=10, kde=True)
    plt.suptitle(f'Quartet {quartet}')
```

#### 2.3 Histogramas Superpuestos
Podemos graficar todas las características `x` e `y` de los cuartetos en dos gráficos diferentes, superponiéndolos usando el parámetro `element='step'` y aplicando transparencia (`alpha`).

```python
# El parámetro 'element' define la representación visual. Puede ser 'bars', 'step' o 'poly'.
element = 'step'
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
legends = []

for quartet, g in quartets.groupby('quartet'):
    legends.append(f'quartet {quartet}')
    sns.histplot(data=g, x="x", hue='quartet', ax=axes[0], palette=palette, bins=10, kde=False, alpha=.2, element=element)
    sns.histplot(data=g, x="y", hue='quartet', ax=axes[1], palette=palette, bins=10, kde=False, alpha=.2, element=element)

axes[0].legend(legends)
axes[1].legend(legends);
```

---
##### 🛠️ Práctica 2: Jugando con Bins y KDE
Grafica un histograma con Seaborn para la variable `y` de todo el dataset completo (sin separar por cuartetos). Configura `20` contenedores (bins) y enciende la curva KDE. 
Observa cómo cambia la resolución de la forma de campana.

```python
# Escribe tu código aquí
fig, ax = plt.subplots(figsize=(8, 4))
# sns.histplot(data=..., x=..., bins=..., kde=...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
sns.histplot(data=quartets, x='y', bins=20, kde=True, ax=ax, color='teal')
```
</details>

---
### 3. FacetGrid ✨

Esta es una herramienta poderosa que se puede usar en combinación con los métodos de graficación de Seaborn o Matplotlib para crear múltiples subgráficos basados en una relación condicional.

📚 **Documentación:** [seaborn.FacetGrid()](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html): Cuadrícula multiplano para graficar relaciones condicionales.

#### 3.1 Cuadrícula de Histogramas

```python
for feature in ['x', 'y']:
    # Creamos la grilla con la condición quartet
    g = sns.FacetGrid(quartets, col="quartet", palette=palette, col_wrap=4)
    # Para cada condición creamos un subplot (histplot) para la columna "feature"
    g.map(sns.histplot, feature, bins=10)
    # col_wrap define el número de columnas. Cambia el valor a 3 o 2 para entenderlo.
```

#### 3.2 FacetGrid Maestro con pd.melt()
Podemos crear un `FacetGrid` para **todo** de una sola vez. Para ello, convertimos el dataframe para acceder a los valores basados en condiciones tanto de filas como de columnas.

```python
melted = pd.melt(quartets, id_vars='quartet', var_name='variable', value_name='value')

# Creamos la grilla con los cuartetos como columnas y las variables como filas
g = sns.FacetGrid(melted, row="variable", col='quartet', palette=palette, sharex=False)
g.map(sns.histplot, 'value', bins=10);

# Nota: Necesitamos establecer sharex=False para evitar distorsionar las formas entre las filas.
```

---
##### 🛠️ Práctica 3: FacetGrid de Cajas
El FacetGrid no es exclusivo de los histogramas. Utiliza el dataframe `melted` y crea un `FacetGrid` separando por columnas los `quartet`, pero mapea la función `sns.boxplot` para visualizar los rangos de la columna `value`.

```python
# Escribe tu código aquí
# g = sns.FacetGrid(melted, col=...)
# g.map(sns.boxplot, ...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
g = sns.FacetGrid(melted, col='quartet', palette=palette, height=4)
g.map(sns.boxplot, 'value')
```
</details>

---
### 4. Diagramas de Dispersión (Scatter plots) 🌌

Sabiendo que tenemos las características `x` e `y`, podemos pensar en usar otro tipo de gráfico útil. ¿Por qué no un scatter plot?

#### 4.1 Scatter Plots con Pandas

```python
quartets.groupby('quartet').plot.scatter(x='x', y='y', s=50);
```

#### 4.2 Scatter Plots con Seaborn
Podemos combinar matplotlib con seaborn para mejorar la estética.

```python
fig, axes = plt.subplots(2, 2, figsize=(7, 7))
axes = axes.flatten().tolist()

for quartet, g in quartets.groupby('quartet'):
    ax = axes.pop(0)
    sns.scatterplot(data=g, x='x', y='y', ax=ax)
    ax.set_title(f'quartet {quartet}')
    
plt.subplots_adjust(hspace=0.3);
```

#### 4.3 Scatter Plots con FacetGrid
FacetGrid es excelente para evitar escribir demasiadas líneas de código de matplotlib. En este caso forzaremos a la grilla a compartir los dominios X e Y para simplificar la comparación.

```python
g = sns.FacetGrid(quartets, col='quartet', palette=palette, col_wrap=2, sharex=True, sharey=True, height=3)
g.map(sns.scatterplot, 'x', 'y', s=100, color="#4c72b0");
```

#### 🤯 ¡MISTERIO RESUELTO!

¿Recuerdas que la estadística descriptiva decía que **estos 4 datasets eran idénticos**?
- **Cuarteto I:** Relación lineal simple.
- **Cuarteto II:** Curva parabólica perfecta.
- **Cuarteto III:** Línea recta perfecta con **un gran outlier**.
- **Cuarteto IV:** Constante con un outlier masivo.

¡Esta es la demostración definitiva de por qué jamás se debe saltar la visualización!

---
### 5. Gráficos de Líneas (Line plots) 📈

Podríamos usar un lineplot, pero para hacerlo necesitamos saber que los puntos deben estar ordenados en el eje X.

#### 5.1 Gráficos de Líneas con Pandas

```python
quartets.sort_values(by='x').groupby('quartet').plot(x='x', y='y', marker='o', lw=.7);
```

#### 5.2 Todos en uno (Pandas/Matplotlib)
También podemos usar matplotlib para graficar todos los grupos en el mismo gráfico.

```python
# creamos una figura de 1 x 1
fig, ax = plt.subplots(1, 1, figsize=(16, 6))

# graficamos los 4 cuartetos en el mismo ax
quartets.sort_values(by='x').groupby('quartet').plot(x='x', y='y', marker='o', ms=10, lw=.7, alpha=.7, ax=ax)
plt.ylabel('y')
plt.title('Todos los cuartetos en uno');
```

#### 5.3 Gráficos de Líneas con Seaborn
📚 **Documentación:** [Seaborn.lineplot()](https://seaborn.pydata.org/generated/seaborn.lineplot.html)

Seaborn simplifica la creación del mismo gráfico.

```python
fig, ax = plt.subplots(1, 1, figsize=(16, 6))
sns.lineplot(data=quartets, x='x', y='y', hue='quartet', marker='o', ms=10, lw=.7, alpha=.7, ax=ax)
plt.title('Todos los cuartetos en uno (Seaborn)');
```

Y podemos graficar todos los cuartetos juntos removiendo el condicional `hue` para Seaborn, notando la diferencia de cómo calculan los intervalos.

```python
fig, axes = plt.subplots(1, 2, figsize=(16, 4))
sns.lineplot(data=quartets, x='x', y='y', lw=.7, ax=axes[0])
axes[0].set_title('Una línea con Seaborn')

quartets.plot(x='x', y='y', lw=.7, ax=axes[1])
axes[1].set_title('Una línea con Matplotlib');
```

---
##### 🛠️ Práctica 4: Imitando comportamientos
Seaborn está construido sobre Matplotlib, así que modificando los parámetros de la función debería permitirte llegar a la misma gráfica plana.

Modifica los parámetros de la función `sns.lineplot()` para que los dos gráficos se vean visualmente similares (apaga el intervalo de confianza y el estimador estadístico).
*(Pista: revisa en internet el parámetro `errorbar` o `ci`)*

```python
# Escribe tu código aquí
fig, ax = plt.subplots(1, 1, figsize=(8,4))
# Modifica esta línea:
sns.lineplot(data=quartets, x='x', y='y', ax=ax)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
sns.lineplot(data=quartets, x='x', y='y', ax=ax, errorbar=None, estimator=None)
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
