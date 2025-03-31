import sqlite3

def leer_accesos():
    conn = sqlite3.connect('accesos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM accesos")
    filas = cursor.fetchall()

    print("📋 Registros de accesos:")
    for fila in filas:
        print(f"ID: {fila[0]} | Usuario: {fila[1]} | Fecha: {fila[2]}")

    conn.close()

# Ejecutar función
leer_accesos()
