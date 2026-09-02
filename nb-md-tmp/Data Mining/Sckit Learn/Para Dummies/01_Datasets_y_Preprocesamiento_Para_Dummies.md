# 01_Datasets_y_Preprocesamiento_Para_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Carga y Preprocesamiento Para Dummies: La Cocina de Datos 💡
      </h1>
      <p style="margin: 6px 0 0 0; color: #f59e0b; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Minería de Datos (Data Mining) — Edición Para Dummies 💡
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #f59e0b; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Módulo: Scikit-Learn #01
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #d97706; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Mining/Sckit%20Learn/Para%20Dummies/01_Datasets_y_Preprocesamiento_Para_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## La Gran Verdad: Los Datos en la Vida Real Vienen Sucios 🧹

En los libros de matemáticas, los datos son perfectos y limpios. En el mundo real, los datos son como verduras recién cosechadas de la tierra: **vienen con barro, algunas están mordidas por insectos y otras vienen en bolsas sin marcar**.

Si metes ingredientes sucios al horno, tu pastel saldrá incomible (*"Basura entra, Basura sale" / Garbage In, Garbage Out*).

El **Preprocesamiento** es el arte de lavar, pelar, pesar y cortar los ingredientes antes de cocinar.

```
  [ Datos Sucios ] ───> [ 1. Lavar Nulos ] ───> [ 2. Pesar Escalas ] ───> [ 3. Traducir Texto ] ───> [ Datos Listos ]
  (Con barro y NaNs)     (SimpleImputer)         (StandardScaler)        (OneHotEncoder)          (Para el Modelo)
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Carguemos el dataset más famoso del mundo: Las Flores Iris
flores = load_iris(as_frame=True)
df_flores = flores.frame

print("🌸 Dataset Iris cargado con éxito. Primeras 5 flores:")
df_flores.head()
```

---
## 1. Tratamiento de Huecos Vacíos con `SimpleImputer` 🧩

¿Qué pasa cuando un cliente no quiso responder su edad en un formulario? En la base de datos queda un valor vacío llamado `NaN` (*Not a Number*).

La mayoría de modelos matemáticos se rompen y arrojan error si ven un `NaN`.

Para solucionarlo, usamos el bloque **`SimpleImputer`**:
* **`strategy='mean'` (Promedio):** Rellena los huecos con la media de la columna.
* **`strategy='median'` (Mediana):** Rellena los huecos con el valor central (la mejor opción si hay personas multimillonarias o valores extremos).
* **`strategy='most_frequent'` (Moda):** Rellena con la categoría más repetida (ideal para texto).

```python
from sklearn.impute import SimpleImputer

# Tabla con huecos vacíos (np.nan)
datos_pacientes = np.array([
    [25.0],
    [np.nan], # ¡Falta la edad!
    [35.0],
    [np.nan], # ¡Falta la edad!
    [40.0]
])

# Rellenamos los huecos con el promedio de las edades conocidas ( (25 + 35 + 40)/3 = 33.33 )
imputador_edad = SimpleImputer(strategy='mean')
edades_completas = imputador_edad.fit_transform(datos_pacientes)

print("Edades con huecos:\n", datos_pacientes.ravel())
print("\n✨ Edades reparadas automáticamente:\n", edades_completas.ravel().round(1))
```

---
## 2. Pesar en la Misma Balanza: `StandardScaler` vs `RobustScaler` ⚖️

Imagina que estás comparando dos variables de una persona:
* Su **Edad**: de 18 a 80 años.
* Su **Salario Anual**: de $20,000 a $500,000 dólares.

Para una computadora, el salario parece **10,000 veces más importante** que la edad simplemente porque los números son más grandes. ¡Eso es un error gravísimo!

Debemos poner todo en la misma balanza:
1. **`StandardScaler`:** Convierte cualquier columna para que su promedio sea `0` y su dispersión sea `1`.
2. **`RobustScaler`:** Es el hermano fuerte de `StandardScaler`. Si hay valores locos o multimillonarios (*outliers*), `RobustScaler` no se deja engañar porque usa la mediana.

```python
from sklearn.preprocessing import StandardScaler, RobustScaler

# Salarios con un multimillonario extravagante (Outlier)
salarios = np.array([
    [2000.0],
    [2200.0],
    [2500.0],
    [2100.0],
    [2400.0],
    [500000.0] # ¡Elon Musk entró al dataset!
])

escalador_estandar = StandardScaler().fit_transform(salarios)
escalador_robusto = RobustScaler().fit_transform(salarios)

print("Salarios escalados con StandardScaler (Distorsionado por el multimillonario):")
print(escalador_estandar.ravel().round(2))

print("\nSalarios escalados con RobustScaler (Protegido contra valores extremos):")
print(escalador_robusto.ravel().round(2))
```

---
## 3. Traducir Palabras a Números: `OneHotEncoder` 🏷️

Las computadoras no entienden la palabra `"Bogotá"`, `"Tunja"` o `"Medellín"`. Solo entienden ceros y unos.

¿Cómo traducimos ciudades a números sin inventar un orden falso?
Si le pones `Tunja = 1`, `Bogotá = 2`, `Medellín = 3`, el algoritmo pensará erróneamente que Medellín vale el triple que Tunja.

La solución elegante se llama **One-Hot Encoding (Casillas de Votación)**:
Crea una columna nueva para cada ciudad con un `1` si la persona es de esa ciudad y `0` en las demás.

```python
from sklearn.preprocessing import OneHotEncoder

df_tienda = pd.DataFrame({
    'Ciudad': ['Tunja', 'Bogotá', 'Tunja', 'Medellín'],
    'Metodo_Pago': ['Tarjeta', 'Efectivo', 'Transferencia', 'Tarjeta']
})

# Traemos el OneHotEncoder
ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
ciudades_binarias = ohe.fit_transform(df_tienda[['Ciudad']])

nombres_columnas = ohe.get_feature_names_out(['Ciudad'])
df_ciudades_ohe = pd.DataFrame(ciudades_binarias, columns=nombres_columnas)

print("Tabla Original:")
display(df_tienda[['Ciudad']])

print("\nTabla Traducida a Ceros y Unos (One-Hot):")
display(df_ciudades_ohe)
```

---
## 4. Actividades y Desafíos Prácticos Guiados 🧪

### 🛠️ Práctica 2.1: Limpieza de un Historial Clínico
Tienes un registro médico con estaturas donde hay dos pacientes sin estatura registrada (`np.nan`).
1. Rellena los huecos vacíos usando la **mediana**.
2. Escala las estaturas resultantes usando `StandardScaler`.
3. Imprime las estaturas finales limpias y escaladas.

```python
# Escribe tu solución aquí
estaturas_clinica = np.array([
    [165.0],
    [np.nan],
    [172.0],
    [180.0],
    [np.nan],
    [158.0]
])

# 1. Imputar con SimpleImputer(strategy='median')
# 2. Escalar con StandardScaler()
# 3. Mostrar resultado final
```

---
### 🛠️ Práctica 2.2: Codificar Tipos de Vehículo
Tienes una lista con tipos de vehículos: `['Carro', 'Moto', 'Camión', 'Carro', 'Bicicleta']`.
Aplica `OneHotEncoder` y muestra las columnas creadas con `.get_feature_names_out()`.

```python
# Escribe tu solución aquí
vehiculos = pd.DataFrame({'Tipo': ['Carro', 'Moto', 'Camión', 'Carro', 'Bicicleta']})

# ohe_vehiculos = OneHotEncoder(...)
```

---
## 5. Preguntas de Autoevaluación 🧠

1. **¿Por qué no debemos borrar simplemente todas las filas que tengan un valor nulo (`NaN`)?**  
   *Respuesta:* Porque perderíamos muchísima información valiosa de las otras columnas de esa persona. Imputar permite salvar el registro.
2. **¿Cuándo es mejor usar `RobustScaler` en lugar de `StandardScaler`?**  
   *Respuesta:* Siempre que haya sospecha o certeza de valores extremos anormales (*outliers*), como ingresos millonarios o errores de digitación.
3. **¿Qué hace el parámetro `handle_unknown='ignore'` en `OneHotEncoder`?**  
   *Respuesta:* Evita que el sistema colapse si en el futuro llega un cliente con una ciudad que nunca antes habíamos visto; simplemente le pone ceros en todas las columnas.

---
## 📌 Resumen de Herramientas de Limpieza

| Herramienta | ¿Cuándo usarla? | Lo que hace en palabras simples |
|---|---|---|
| **`SimpleImputer`** | Cuando hay celdas vacías (`NaN`). | Tapa los huecos con el promedio o la mediana. |
| **`StandardScaler`** | Datos numéricos sin outliers extremos. | Pone los números en la misma escala (media 0). |
| **`RobustScaler`** | Datos numéricos con outliers locos. | Escala usando la mediana para no dejarse engañar. |
| **`OneHotEncoder`** | Variables de texto o categorías. | Crea casillas de sí/no (1 o 0) para cada categoría. |
