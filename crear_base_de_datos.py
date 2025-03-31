import sqlite3

def crear_base_de_datos():
    conn = sqlite3.connect('accesos.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accesos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Base de datos y tabla 'accesos' creadas.")

crear_base_de_datos()
