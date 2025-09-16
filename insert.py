import json
import mysql.connector
from datetime import datetime

db_config = {
    "host": "localhost",     
    "user": "root",          
    "database": "json"    
}

# LEER JSON 
json_path = r"D:\excel pdf\2013.json" 
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# CONEXIÓN A MYSQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

#FUNCIÓN PARA INSERTAR 
def insertar_registro(item):
    titulo = item["name"]
    url = item["url"]
    gestion = item["gestion"]
    #tipo = item["type"]

    # Insertar en wp_posts
    sql_post = """
    INSERT INTO wp_posts (post_author, post_date, post_title, guid, post_status, post_type, post_mime_type)
    VALUES (%s, %s, %s, %s, 'publish', 'attachment', 'application/pdf')
    """
    valores_post = (1, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), titulo, url)

    cursor.execute(sql_post, valores_post)
    post_id = cursor.lastrowid 

    # Insertar metadatos (gestion y type)
    sql_meta = """
    INSERT INTO wp_postmeta (post_id, meta_key, meta_value)
    VALUES (%s, %s, %s)
    """
    if "/uploads/" in url:
        short_url = url.split("/uploads/")[1] 
    else:
        short_url = url
    
    attachment_metadata = 'a:1:{s:8:"filesize";i:10;}'

    # Insertar metadatos 
    sql_meta = """
    INSERT INTO wp_postmeta (post_id, meta_key, meta_value)
    VALUES (%s, %s, %s)
    """
    metas = [
       # (post_id, "gestion", str(gestion)),
        #(post_id, "type", str(tipo)),
        (post_id, "_wp_attached_file", short_url),
        (post_id, "_wp_attachment_metadata", attachment_metadata)
    ]

    cursor.executemany(sql_meta, metas)
# nuevo 1 
    sql_doc = """
    INSERT INTO wp_posts (post_author, post_date, post_title, guid, post_status, post_type, post_mime_type)
    VALUES (%s, %s, %s, %s, 'publish', 'documentos', 'application/pdf')
    """
    valores_doc = (1, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), titulo, "temp")
    cursor.execute(sql_doc, valores_doc)
    doc_id = cursor.lastrowid

    #  4) Actualizar guid con el ID real del nuevo documento ===
    guid38 = '38'
    guid_final = f"http://oopptest.oopp.gob.bo/?post_type=documentos&#{guid38};p={doc_id}"
    cursor.execute("UPDATE wp_posts SET guid = %s WHERE ID = %s", (guid_final, doc_id))

# nuevo 2 
    sql_meta_doc = """
    INSERT INTO wp_postmeta (post_id, meta_key, meta_value)
    VALUES (%s, %s, %s)
    """
    metas_doc = [
        (doc_id, "anio", str(gestion)),
        (doc_id, "_anio", "field_doc_672ce03b5e0c0"),
        (doc_id, "descripcion", titulo),
        (doc_id, "_descripcion", "field_doc_672ce0445e0c1"),
        (doc_id, "documento", post_id),
        (doc_id, "_documento", "field_doc_672ce0765e0c4"),
    ]
    cursor.executemany(sql_meta_doc, metas_doc)

#numero 3
    cursor.execute(
        "UPDATE wp_posts SET post_parent = %s WHERE ID = %s",
        (doc_id, post_id)
    )
# nueva tabla
    sql_meta_term="""
    INSERT INTO wp_term_relationships (object_id, term_taxonomy_id, term_order)
    VALUES (%s, %s, %s) """
    taxonomi = '12'
    metas_term = [
        (post_id, taxonomi, 0)
    ]
    cursor.executemany(sql_meta_term, metas_term)


    print(f"✔ Insertado: {titulo} (ID={post_id})")

for item in data:
    insertar_registro(item)

conn.commit()

cursor.close()
conn.close()

print("✅ Todos los registros fueron insertados correctamente.")
