import sqlite3

def actualizar_usuario(id_acceso, nuevo_usuario):
    conn = sqlite3.connect('accesos.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE accesos SET usuario = ? WHERE id = ?", (nuevo_usuario, id_acceso))
    conn.commit()
    conn.close()
    print(f"✏️ Usuario con ID {id_acceso} actualizado a {nuevo_usuario}")

# Ejecutar función
actualizar_usuario(1, "nuevo_usuario@ejemplo.com")
