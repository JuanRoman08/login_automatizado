import sqlite3
from datetime import datetime

DB = 'accesos.db'

def crear_acceso():
    usuario = input("Correo del usuario: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accesos (usuario, fecha) VALUES (?, ?)", (usuario, fecha))
    conn.commit()
    conn.close()
    print("✅ Acceso registrado manualmente.")

def leer_accesos():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accesos")
    accesos = cursor.fetchall()
    conn.close()
    print("\n📋 Lista de accesos:")
    for acc in accesos:
        print(f"ID: {acc[0]} | Usuario: {acc[1]} | Fecha: {acc[2]}")
    print()

def actualizar_acceso():
    id = input("ID del acceso a actualizar: ")
    nuevo_usuario = input("Nuevo correo de usuario: ")
    nueva_fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("UPDATE accesos SET usuario = ?, fecha = ? WHERE id = ?", (nuevo_usuario, nueva_fecha, id))
    conn.commit()
    conn.close()
    print("✅ Acceso actualizado.")

def eliminar_acceso():
    id = input("ID del acceso a eliminar: ")
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM accesos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print("🗑️ Acceso eliminado.")

def menu():
    while True:
        print("""
📌 MENÚ CRUD - ACCESOS
1. Crear nuevo acceso
2. Ver todos los accesos
3. Actualizar un acceso
4. Eliminar un acceso
5. Salir
""")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_acceso()
        elif opcion == "2":
            leer_accesos()
        elif opcion == "3":
            actualizar_acceso()
        elif opcion == "4":
            eliminar_acceso()
        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
