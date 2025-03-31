import sqlite3
from datetime import datetime

def insertar_acceso(usuario):
    conn = sqlite3.connect('accesos.db')
    cursor = conn.cursor()

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO accesos (usuario, fecha) VALUES (?, ?)", (usuario, fecha))
    conn.commit()
    conn.close()
    print(f"✅ Acceso guardado para: {usuario}")

# Ejecutar función
insertar_acceso("didita7244@deenur.com")
