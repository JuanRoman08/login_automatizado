import smtplib
from email.mime.text import MIMEText

# ✉️ Configuración de Mailtrap
SMTP_HOST = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 587
SMTP_USER = "e348199c7681a1"  # tu nombre de usuario de Mailtrap
SMTP_PASS = "adfccf838a066f"  # reemplaza esto con la contraseña completa (sin los asteriscos)
EMAIL_FROM = "juandiegoromansalazar08@gmail.com"
EMAIL_TO = "didita7244@deenur.com"

# Crear mensaje
msg = MIMEText("🚀 Este es un correo de prueba enviado desde Python con Mailtrap.")
msg["Subject"] = "📨 Prueba de correo con Mailtrap"
msg["From"] = EMAIL_FROM
msg["To"] = EMAIL_TO

# Enviar correo
try:
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
    print("✅ ¡Correo enviado exitosamente a Mailtrap!")
except smtplib.SMTPAuthenticationError as e:
    print("❌ Error de autenticación SMTP:", e)
except Exception as e:
    print("❌ Otro error:", e)
