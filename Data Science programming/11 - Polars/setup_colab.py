import os, urllib.request, urllib.parse

def load_dataset(filename, module_name="11 - Polars"):
    """
    Carga o descarga de forma segura el dataset para ejecución local o en Google Colab.
    Si no se encuentra localmente ni en GitHub, lo genera automáticamente.
    """
    candidates = [
        os.path.join("data", filename),
        os.path.join(module_name, "data", filename),
        os.path.join("..", "data", filename),
        os.path.join("..", module_name, "data", filename),
        os.path.join("Data Science programming", module_name, "data", filename),
        os.path.join("..", "Data Science programming", module_name, "data", filename),
        filename
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
            
    os.makedirs("data", exist_ok=True)
    target_path = os.path.join("data", filename)
    folder_path = f"Data Science programming/{module_name}"
    encoded_folder = urllib.parse.quote(folder_path)
    encoded_file = urllib.parse.quote(filename)
    
    urls = [
        f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/{encoded_folder}/data/{encoded_file}",
        f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/master/{encoded_folder}/data/{encoded_file}"
    ]
    
    print(f"📥 Intentando descargar '{filename}' desde el repositorio oficial...")
    for url in urls:
        try:
            with urllib.request.urlopen(url, timeout=3) as response:
                if response.status == 200:
                    with open(target_path, 'wb') as out_f:
                        out_f.write(response.read())
                    print(f"✅ Dataset '{filename}' descargado exitosamente.")
                    return target_path
        except Exception:
            continue
            
    print(f"⚙️ Generando '{filename}' sintéticamente para ejecución inmediata...")
    import polars as pl
    import numpy as np
    np.random.seed(42)
    
    n_clientes = 1000
    df_c = pl.DataFrame({
        'id_cliente': [f'CLI-{i:04d}' for i in range(1, n_clientes + 1)],
        'nombre': [f'Cliente_{i}' for i in range(1, n_clientes + 1)],
        'segmento': np.random.choice(['Corporativo', 'Pyme', 'Consumo', 'Gobierno'], n_clientes),
        'edad': np.random.randint(18, 70, n_clientes),
        'ciudad_residencia': np.random.choice(['Tunja', 'Bogotá', 'Medellín', 'Cali', 'Bucaramanga'], n_clientes),
        'ingreso_anual': np.random.normal(45000000, 15000000, n_clientes).round(2)
    })
    
    n_ventas = 60000
    cats = ['Tecnología', 'Mobiliario', 'Material de Oficina', 'Servicios']
    prods = ['Laptop Pro', 'Monitor 4K', 'Silla Ergonómica', 'Escritorio', 'Papel A4', 'Tóner', 'Mantenimiento']
    ciudades = ['Tunja', 'Bogotá', 'Medellín', 'Cali', 'Barranquilla']
    
    cant = np.random.randint(1, 10, n_ventas)
    pu = np.random.choice([25000.0, 120000.0, 450000.0, 1200000.0, 3500000.0], n_ventas)
    desc = np.random.choice([0.0, 0.05, 0.10, 0.15], n_ventas)
    tot = (cant * pu * (1 - desc)).round(2)
    
    df_v = pl.DataFrame({
        'id_venta': [f'VNT-{i:06d}' for i in range(1, n_ventas + 1)],
        'fecha': [f'2024-{np.random.randint(1,13):02d}-{np.random.randint(1,29):02d}' for _ in range(n_ventas)],
        'id_cliente': np.random.choice(df_c['id_cliente'], n_ventas),
        'categoria': np.random.choice(cats, n_ventas),
        'producto': np.random.choice(prods, n_ventas),
        'cantidad': cant,
        'precio_unitario': pu,
        'descuento': desc,
        'ciudad_venta': np.random.choice(ciudades, n_ventas),
        'total_venta': tot
    })
    
    c_csv_path = os.path.join("data", "clientes.csv")
    c_pq_path = os.path.join("data", "clientes.parquet")
    v_csv_path = os.path.join("data", "ventas.csv")
    v_pq_path = os.path.join("data", "ventas.parquet")
    
    if not os.path.exists(c_csv_path): df_c.write_csv(c_csv_path)
    if not os.path.exists(c_pq_path): df_c.write_parquet(c_pq_path)
    if not os.path.exists(v_csv_path): df_v.write_csv(v_csv_path)
    if not os.path.exists(v_pq_path): df_v.write_parquet(v_pq_path)
    
    print(f"✅ Datasets preparados exitosamente en '{target_path}'.")
    return target_path

if __name__ == '__main__':
    load_dataset('ventas.csv')
