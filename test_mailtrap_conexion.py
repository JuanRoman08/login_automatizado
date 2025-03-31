import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_USER = os.getenv("MAILTRAP_USER")
EMAIL_PASS = os.getenv("MAILTRAP_PASS")

try:
    server = smtplib.SMTP("sandbox.smtp.mailtrap.io", 587)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL_USER, EMAIL_PASS)
    print("✅ Conexión exitosa con Mailtrap SMTP.")
    server.quit()
except Exception as e:
    print("❌ Falló la conexión:", e)
