import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# Lista de variables requeridas
VARIABLES_REQUERIDAS = [
    "DROPBOX_TOKEN",
    "USUARIO",
    "MAILTRAP_USER",
    "MAILTRAP_PASS",
    "EMAIL_FROM",
    "EMAIL_TO"
]

def validar_variables():
    faltantes = []

    for var in VARIABLES_REQUERIDAS:
        valor = os.getenv(var)
        if not valor:
            faltantes.append(var)

    if faltantes:
        print("❌ Las siguientes variables faltan en tu archivo .env:")
        for var in faltantes:
            print(f"   - {var}")
        print("🛠️ Por favor, agrégalas a tu archivo `.env`.")
        return False

    print("✅ Todas las variables del entorno están presentes.")
    return True

if __name__ == "__main__":
    validar_variables()
