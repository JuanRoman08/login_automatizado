import os
from dotenv import load_dotenv

load_dotenv()

print("Usuario:", os.getenv("MAILTRAP_USER"))
print("Contraseña:", os.getenv("MAILTRAP_PASS"))
