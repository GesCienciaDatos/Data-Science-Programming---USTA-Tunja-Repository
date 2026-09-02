# 02_NumPy_Hands_On

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Ejercicios Prácticos de NumPy
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
        Taller Práctico • Módulo 02
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/02_NumPy_Hands_On.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

Los siguientes ejercicios son una selección de [este conjunto más amplio.](https://github.com/rougier/numpy-100)

**1. Importa el paquete numpy bajo el nombre np**

```python
### TU CÓDIGO AQUÍ ###
```

**2. Crea un vector de ceros de tamaño 10**

```python
### TU CÓDIGO AQUÍ ###
```

**3. Crea un vector de ceros de tamaño 10 cuyo quinto valor sea 1**

```python
### TU CÓDIGO AQUÍ ###
```

**4. Crea un vector con valores en un rango del 10 al 49**

```python
### TU CÓDIGO AQUÍ ###
```

**5. Invierte el vector 'Z' dado (el primer elemento se convierte en el último)**

```python
Z = np.arange(50)

### TU CÓDIGO AQUÍ ###
```

**6. Crea una matriz de 3x3 con valores en un rango del 0 al 8**

```python
### TU CÓDIGO AQUÍ ###
```

**7. Encuentra los índices de los elementos que no sean cero en `[1,2,0,0,4,0]`**

*Nota*: Busca la función `nonzero()` en la documentación: [https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html)

```python
### TU CÓDIGO AQUÍ ###
```

**8. Crea una matriz identidad de 3x3**

```python
### TU CÓDIGO AQUÍ ###
```

**9. Crea un arreglo (array) de 3x3x3 con valores aleatorios (muestreados de una distribución "uniforme continua")**

```python
### TU CÓDIGO AQUÍ ###
```

**10. Crea un arreglo de 10x10 con valores aleatorios y encuentra los valores mínimo y máximo**

```python
### TU CÓDIGO AQUÍ ###
```

**11. Crea un vector aleatorio de tamaño 30 y encuentra el valor promedio (media)**

```python
### TU CÓDIGO AQUÍ ###
```

**12. Crea un arreglo 2D con 1's en los bordes y 0's en el interior**

```python
### TU CÓDIGO AQUÍ ###
```

**13. Añade un borde (relleno de ceros) alrededor del arreglo Z**

*Nota*: busca la función `pad()` de NumPy en la documentación oficial

```python
Z = np.ones((5,5))

### TU CÓDIGO AQUÍ ###
```

**14. Añade un borde (relleno de ceros) dentro del arreglo Z**

*Nota*: utiliza indexación avanzada (fancy indexing)

```python
Z = np.ones((5,5))

### TU CÓDIGO AQUÍ ###
```

**15. Crea una matriz de 5x5 con los valores 1, 2, 3, 4 justo debajo de la diagonal**

*Nota*: busca la función `diag()`

```python
### TU CÓDIGO AQUÍ ###
```

**Vamos ahora a crear un arreglo con el cual trabajar**

```python
rng = np.random.default_rng(seed=16) 
random_integers = rng.integers(low=1, high=500000, size=(20, 5)) 
random_integers
```

**16. Calcula el valor promedio de la segunda columna**

```python
### TU CÓDIGO AQUÍ ###
```

**17. Calcula el valor promedio de cada una de las primeras 5 filas considerando únicamente la tercera y cuarta columnas**

```python
### TU CÓDIGO AQUÍ ###
```
