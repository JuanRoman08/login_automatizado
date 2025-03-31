import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

REMITENTE = os.getenv("EMAIL_USER")
CLAVE = os.getenv("EMAIL_PASS")
DESTINATARIO = os.getenv("EMAIL_DEST")

def enviar_correo(usuario, fecha):
    msg = MIMEText(f"Nuevo acceso:\nUsuario: {usuario}\nFecha: {fecha}")
    msg["Subject"] = "📩 Nuevo acceso registrado"
    msg["From"] = REMITENTE
    msg["To"] = DESTINATARIO

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(REMITENTE, CLAVE)
        server.send_message(msg)

    print("✉️ Correo enviado con éxito.")

if __name__ == "__main__":
    enviar_correo("usuario@correo.com", "2025-03-28 11:00:00")
