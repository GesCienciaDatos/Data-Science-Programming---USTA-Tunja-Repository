# 02_Estadistica_Descriptiva_EDA

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Estadística Descriptiva para Ciencia de Datos 📊
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/04%20-%20EDA/02_Estadistica_Descriptiva_EDA.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## El engaño de los números: El Cuarteto de Anscombe 

Como vimos en el cuaderno anterior, nuestro dataset `quartets.csv` tiene 4 grupos distintos de datos, cada uno con 11 registros. Vamos a analizarlos estadísticamente para ver en qué se diferencian. 

Utilizaremos el método `.agg()` (aggregate), el cual nos permite aplicar múltiples operaciones estadísticas (como la media y la desviación estándar) al mismo tiempo.

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

**¡Sorpresa!** 😲

Los 4 grupos de datos tienen **exactamente la misma media (promedio) y desviación estándar** (9.0 y 3.31 para X; 7.5 y 2.03 para Y).

Si solo nos guiamos por este resumen numérico básico, concluiríamos sin lugar a dudas que las muestras de todos los cuartetos son idénticas o provienen del mismo lugar.

Como son conjuntos de datos muy pequeños, podemos imprimir un par de ellos para comprobarlo:

```python
display(quartets[quartets['quartet'] == 'I'].head())
display(quartets[quartets['quartet'] == 'II'].head())
```

¡Son datos completamente distintos! Esto se conoce históricamente como el **Cuarteto de Anscombe**, creado por el estadístico Francis Anscombe en 1973 para demostrar una lección invaluable en la Ciencia de Datos:

> ⚠️ **La estadística descriptiva por sí sola puede ser extremadamente engañosa si no se acompaña de gráficos.**

---
### La herramienta principal: `.describe()` 🛠️

Antes de ver cómo solucionar el problema de Anscombe, debemos dominar las herramientas descriptivas. En Pandas, la forma más rápida y poderosa de obtener un resumen estadístico completo de un DataFrame numérico es usando el método `.describe()`.

```python
# describe() nos da conteo, media, std, mínimos, cuartiles y máximos de forma automática
quartets.describe()
```

Pero... ¿Qué significan exactamente todos esos números? Vamos a desglosar los conceptos estadísticos más importantes que necesitas dominar en el EDA.

---
### 1. Medidas de Tendencia Central 🎯

Estas métricas buscan resumir un conjunto de datos encontrando su punto "medio" o típico.

#### Media (Promedio - Mean)
Es la suma de todos los valores dividida por el número total de datos. Representa el centro de gravedad numérico. En Pandas se calcula con `.mean()`.

```python
# Solo seleccionamos las columnas numéricas para evitar errores
quartets[['x', 'y']].mean()
```

#### Mediana (Median)
Si ordenaras todos tus datos de menor a mayor, la mediana es el número que queda **exactamente en la mitad**. Es sumamente valiosa porque es **inmune a los valores atípicos (outliers)**. Si Bill Gates entra a un bar, la riqueza *media* de todos sube a miles de millones, pero la *mediana* apenas se mueve.

En Pandas se calcula con `.median()`.

```python
quartets[['x', 'y']].median()
```

#### Moda (Mode)
Es el valor que ocurre con **mayor frecuencia** (el que más se repite). Es especialmente útil para datos categóricos (textos), aunque también se aplica a números. En Pandas se usa `.mode()`.

```python
quartets['x'].mode()
```

---
### 2. Medidas de Dispersión 🌪️

Saber el promedio no sirve de mucho si no sabemos qué tan dispersos (separados) están los datos entre sí.

#### Rango (Range)
Es la diferencia matemática entre el valor más grande y el más pequeño. Es fácil de entender pero súper frágil ante los outliers. 

Pandas no tiene un método directo `.range()`, se calcula restando el mínimo del máximo:

```python
rango_x = quartets['x'].max() - quartets['x'].min()
print(f"El rango de X es: {rango_x}")
```

#### Varianza (Variance) y Desviación Estándar (Std)
- **Varianza (`.var()`):** Mide el promedio de las distancias al cuadrado desde cada dato hasta la media. Una varianza enorme indica datos muy caóticos.
- **Desviación Estándar (`.std()`):** Es la raíz cuadrada de la varianza. Es la métrica reina del análisis de datos porque, a diferencia de la varianza, se lee en las **mismas unidades** originales que tus datos (ej. Dólares, Metros, Años).

```python
print("Varianza de Y:", quartets['y'].var())
print("Desviación Estándar de Y:", quartets['y'].std())
```

#### Rango Intercuartílico (IQR)
Imagina que cortas tus datos en 4 partes iguales (cuartiles: 25%, 50%, 75%, 100%). El IQR es la diferencia entre el cuartil 3 (75%) y el cuartil 1 (25%). 

Es la mejor forma de medir la dispersión porque representa **dónde vive el 50% central y más normal de tus datos**, ignorando por completo los extremos locos.

En Pandas usamos la función `.quantile()`:

```python
Q1 = quartets['y'].quantile(0.25)
Q3 = quartets['y'].quantile(0.75)
IQR = Q3 - Q1

print(f"El Rango Intercuartil de Y es: {IQR:.2f}")
```

---
### Reglas Generales de Interpretación en EDA 💡

Tener los números es fácil, el arte está en interpretarlos:

1. **Simetría:** Si la media, la mediana y la moda están muy cerca unas de otras (casi idénticas), es altamente probable que tu distribución sea hermosa y simétrica (como una campana de Gauss).
2. **Sesgos (Skew):** Si la media es bastante **mayor** que la mediana, cuidado: tus datos tienen un sesgo hacia la derecha. (Significa que un par de valores gigantes están arrastrando tu promedio hacia arriba).
3. **Volatilidad:** Una desviación estándar gigante en comparación a la media te advierte que la variable es muy inestable.

---
##### 🛠️ Práctica: Calculando Asimetría
Utilizando todo el DataFrame `quartets` (sin agrupar):
1. Extrae la **media** de la columna `x` y guárdala en una variable `mean_x`.
2. Extrae la **mediana** de la columna `x` y guárdala en una variable `median_x`.
3. Compáralas imprimiéndolas. ¿Qué nos dice esto sobre la asimetría de la columna `x` basándonos en la regla 2?

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
mean_x = quartets['x'].mean()
median_x = quartets['x'].median()

print(f"Media de X: {mean_x}")
print(f"Mediana de X: {median_x}")

# Al ser exactamente iguales (ambas son 9.0), significa que X es perfectamente simétrica y no tiene sesgo.
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
