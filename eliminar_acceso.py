import sqlite3

def eliminar_acceso(id_acceso):
    conn = sqlite3.connect('accesos.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM accesos WHERE id = ?", (id_acceso,))
    conn.commit()
    conn.close()
    print(f"🗑 Registro con ID {id_acceso} eliminado")

# Ejecutar función
eliminar_acceso(1)
