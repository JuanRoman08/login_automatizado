from dotenv import load_dotenv
import os

load_dotenv()

print("🔍 Verificando variables del entorno:")
print("✅ USUARIO:", os.getenv("USUARIO"))
print("📤 DROPBOX_TOKEN:", os.getenv("DROPBOX_TOKEN")[:10] + "...")
print("📧 MAILTRAP_USER:", os.getenv("MAILTRAP_USER"))
print("🔑 MAILTRAP_PASS:", os.getenv("MAILTRAP_PASS")[:6] + "...")
print("📨 EMAIL_FROM:", os.getenv("EMAIL_FROM"))
print("📥 EMAIL_TO:", os.getenv("EMAIL_TO"))
