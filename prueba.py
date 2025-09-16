import pandas as pd
import json
import os

def excel_2024_to_json(excel_path, output_json_path):
    """
    Convierte el Excel específico de 2024 a JSON
    
    Args:
        excel_path (str): Ruta completa del archivo Excel
        output_json_path (str): Ruta donde guardar el JSON
    """
    
    try:
        # Leer el archivo Excel
        print(f"Leyendo archivo: {excel_path}")
        df = pd.read_excel(excel_path)
        
        # Mostrar información del archivo
        print(f"Columnas disponibles: {list(df.columns)}")
        print(f"Total de filas: {len(df)}")
        
        # Verificar las columnas (ajusta estos nombres según tu Excel)
        # Si tus columnas se llaman diferente, cambia 'name' y 'url' por los nombres correctos
        name_column = 'Nombre'  # Cambiar por el nombre real de la columna de nombres
        url_column = 'URL'    # Cambiar por el nombre real de la columna de URLs
        
        if name_column not in df.columns or url_column not in df.columns:
            print("ERROR: No se encontraron las columnas esperadas")
            print("Por favor revisa los nombres de las columnas en tu Excel:")
            for i, col in enumerate(df.columns, 1):
                print(f"{i}. {col}")
            return False
        
        # Crear la estructura JSON
        json_data = {
            "2014-2016": []
        }
        
        # Contadores
        total_rows = 0
        processed_rows = 0
        
        # Procesar cada fila
        for index, row in df.iterrows():
            total_rows += 1
            
            # Saltar filas vacías
            if pd.isna(row[name_column]) or pd.isna(row[url_column]):
                continue
            
            # Crear el item
            item = {
                "gestion": 2014-2016,
                "name": str(row[name_column]).strip(),
                "url": str(row[url_column]).strip(),
                "type": 5  # Tipo constante
            }
            
            json_data["2014-2016"].append(item)
            processed_rows += 1
        
        # Guardar el JSON
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)
        
        # Resultados
        print("\n" + "═" * 50)
        print("CONVERSIÓN COMPLETADA EXITOSAMENTE")
        print("═" * 50)
        print(f"Archivo procesado: {os.path.basename(excel_path)}")
        print(f"Filas totales en Excel: {total_rows}")
        print(f"Filas procesadas: {processed_rows}")
        print(f"Filas omitidas (vacías): {total_rows - processed_rows}")
        print(f"Archivo JSON guardado en: {output_json_path}")
        print(f"Total documentos en JSON: {len(json_data['2024'])}")
        
        # Mostrar primeros 3 items como ejemplo
        print("\nPrimeros 3 documentos:")
        for i, item in enumerate(json_data["2024"][:3], 1):
            print(f"{i}. {item['name'][:50]}...")
            
        return True
        
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo {excel_path}")
        return False
    except Exception as e:
        print(f"ERROR inesperado: {e}")
        return False

# Versión con detección automática de columnas
def excel_2024_auto_detect(excel_path, output_json_path):
    """
    Versión que intenta detectar automáticamente las columnas
    """
    
    try:
        print(f"Leyendo archivo: {excel_path}")
        df = pd.read_excel(excel_path)
        
        print("Columnas encontradas:")
        for i, col in enumerate(df.columns, 1):
            print(f"{i}. {col}")
        
        # Intentar detectar automáticamente las columnas
        name_column = None
        url_column = None
        
        # Buscar columnas que probablemente contengan nombres
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in ['nombre', 'name', 'documento', 'resolucion', 'titulo']):
                name_column = col
                break
        
        # Buscar columnas que probablemente contengan URLs
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in ['url', 'enlace', 'link', 'pdf', 'direccion']):
                url_column = col
                break
        
        if not name_column or not url_column:
            print("No se pudieron detectar automáticamente las columnas.")
            print("Por favor usa la función manual especificando los nombres de columnas.")
            return False
        
        print(f"Columna detectada para nombres: {name_column}")
        print(f"Columna detectada para URLs: {url_column}")
        
        # Crear JSON
        json_data = {"2014-2016": []}
        
        for index, row in df.iterrows():
            if pd.isna(row[name_column]) or pd.isna(row[url_column]):
                continue
                
            item = {
                "gestion": 2014-2016,
                "name": str(row[name_column]).strip(),
                "url": str(row[url_column]).strip(),
                "type": 5
            }
            json_data["2014-2016"].append(item)
        
        # Guardar
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)
        
        print(f"\nJSON creado exitosamente: {output_json_path}")
        print(f"Total documentos: {len(json_data['2024'])}")
        
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

# EJECUCIÓN PRINCIPAL
if __name__ == "__main__":
    # Configuración
    EXCEL_PATH = r"D:\excel pdf\2014-2016.xlsx"  # Tu archivo
    OUTPUT_JSON = r"D:\excel pdf\2014-2016.json"  # Donde guardar el resultado
    
    print("CONVERSOR DE EXCEL A JSON")
    print("=" * 50)
    
    # Opción 1: Detección automática
    print("Intentando detección automática de columnas...")
    success = excel_2024_auto_detect(EXCEL_PATH, OUTPUT_JSON)
    
    if not success:
        print("\n" + "=" * 50)
        print("DETECCIÓN AUTOMÁTICA FALLÓ")
        print("Por favor ejecuta el código manual especificando los nombres de columnas")
        
        # Mostrar columnas disponibles para que puedas identificarlas
        try:
            df = pd.read_excel(EXCEL_PATH)
            print("\nColumnas disponibles en tu Excel:")
            for i, col in enumerate(df.columns, 1):
                print(f"{i}. {col}")
                
            print("\nEjemplo de cómo usar la función manual:")
            print('excel_2024_to_json(r"D:\\excel pdf\\2024.xlsx", r"D:\\excel pdf\\2024_output.json")')
            print('(Pero primero necesito que me digas los nombres exactos de tus columnas)')
            
        except:
            print("No se pudo leer el archivo Excel")