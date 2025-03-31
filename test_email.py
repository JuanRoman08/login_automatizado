import os
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv

# Cargar .env
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_DEST = os.getenv("EMAIL_DEST")

print("📧 EMAIL_USER:", EMAIL_USER)
print("🔑 EMAIL_PASS:", EMAIL_PASS)
print("📨 EMAIL_DEST:", EMAIL_DEST)

msg = MIMEText("Este es un correo de prueba desde Python.")
msg["Subject"] = "🧪 Prueba SMTP desde Python"
msg["From"] = EMAIL_USER
msg["To"] = EMAIL_DEST

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
    print("✅ ¡Correo enviado con éxito!")
except smtplib.SMTPAuthenticationError as e:
    print("❌ Error de autenticación SMTP:", e)
except Exception as e:
    print("❌ Otro error ocurrió:", e)
