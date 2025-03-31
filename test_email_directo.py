import smtplib
from email.mime.text import MIMEText

# Usa directamente tu contraseña de aplicación aquí 👇
EMAIL_USER = "juandiegoromansalazar08@gmail.com"
EMAIL_PASS = "kewdzbklvurribwr"
EMAIL_DEST = "didita7244@deenur.com"

print("📧 EMAIL_USER:", EMAIL_USER)
print("🔑 EMAIL_PASS:", EMAIL_PASS)
print("📨 EMAIL_DEST:", EMAIL_DEST)

msg = MIMEText("Este es un correo de prueba enviado SIN .env.")
msg["Subject"] = "🔒 Prueba SMTP sin .env"
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
