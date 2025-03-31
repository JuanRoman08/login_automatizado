import json
import sqlite3
import time
from datetime import datetime
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import dropbox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# ----------------------------
# 📝 Configurar logging
# ----------------------------
logging.basicConfig(
    filename='registro_errores.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ----------------------------
# 🔒 Validar .env
# ----------------------------
load_dotenv()

VARIABLES_REQUERIDAS = [
    "DROPBOX_TOKEN",
    "USUARIO",
    "MAILTRAP_USER",
    "MAILTRAP_PASS",
    "EMAIL_FROM",
    "EMAIL_TO"
]

def validar_env():
    faltantes = [var for var in VARIABLES_REQUERIDAS if not os.getenv(var)]
    if faltantes:
        print("❌ Faltan variables en tu archivo .env:")
        for var in faltantes:
            print(f"   - {var}")
        print("🛠️ Por favor, completa el archivo `.env` antes de continuar.")
        exit()

validar_env()

# ----------------------------
# 📦 Variables del entorno
# ----------------------------
USUARIO = os.getenv("USUARIO")
DROPBOX_TOKEN = os.getenv("DROPBOX_TOKEN")
EMAIL_USER = os.getenv("MAILTRAP_USER")
EMAIL_PASS = os.getenv("MAILTRAP_PASS")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_DEST = os.getenv("EMAIL_TO")

# ----------------------------
# 🐳 Registrar acceso en SQLite
# ----------------------------
def registrar_acceso(usuario):
    try:
        conn = sqlite3.connect('accesos.db')
        cursor = conn.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO accesos (usuario, fecha) VALUES (?, ?)", (usuario, fecha))
        conn.commit()
        conn.close()
        print(f"✅ Acceso registrado automáticamente para: {usuario}")
        return fecha
    except Exception as e:
        logging.error("Error al registrar acceso: %s", e)
        raise

# ----------------------------
# ☁️ Subir archivo a Dropbox
# ----------------------------
def subir_a_dropbox(ruta_local, ruta_remota):
    try:
        print("🔐 Usando token:", DROPBOX_TOKEN[:25], "...")
        dbx = dropbox.Dropbox(DROPBOX_TOKEN)
        dbx.users_get_current_account()

        with open(ruta_local, "rb") as f:
            dbx.files_upload(f.read(), ruta_remota, mode=dropbox.files.WriteMode("overwrite"), mute=True)

        print("📄 Archivo subido a Dropbox.")
    except dropbox.exceptions.AuthError as e:
        logging.error("❌ Token inválido o expirado: %s", e)
        print("❌ Token inválido o expirado. Verifica que sea reciente y válido.")
    except Exception as e:
        logging.error("Error al subir archivo a Dropbox: %s", e)
        raise

# ----------------------------
# 📧 Enviar correo personalizado con HTML
# ----------------------------
def enviar_correo(usuario, fecha):
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "📩 Nuevo Acceso Detectado en Dropbox"
        msg["From"] = EMAIL_FROM
        msg["To"] = EMAIL_DEST

        html = f"""
        <html>
        <body style="font-family: Arial, sans-serif;">
            <h2>🔐 Acceso Detectado</h2>
            <p>Se ha registrado un nuevo acceso automático al sistema con las siguientes credenciales:</p>
            <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; margin-top: 10px;">
                <tr style="background-color: #f2f2f2;">
                    <th>👤 Usuario</th><th>🕒 Fecha y Hora</th>
                </tr>
                <tr>
                    <td>{usuario}</td><td>{fecha}</td>
                </tr>
            </table>
            <p style="margin-top: 15px;">📂 El archivo de sesión fue subido a Dropbox exitosamente.</p>
            <p>Saludos,<br><b>🤖 Bot de Automatización</b></p>
        </body>
        </html>
        """

        parte_html = MIMEText(html, "html")
        msg.attach(parte_html)

        print("📧 Conectando con Mailtrap SMTP...")
        server = smtplib.SMTP("sandbox.smtp.mailtrap.io", 587, timeout=15)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_FROM, EMAIL_DEST, msg.as_string())
        server.quit()

        print("✉️ Correo enviado con éxito.")
    except Exception as e:
        logging.error("Error al enviar correo: %s", e)
        raise

# ----------------------------
# 👀 Usar cookies y automatizar
# ----------------------------
def usar_cookies():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()

            with open("cookies_dropbox.json", "r", encoding="utf-8") as f:
                cookies = json.load(f)
                context.add_cookies(cookies)

            page = context.new_page()
            page.goto("https://www.dropbox.com/home")

            print("✅ Sesión restaurada con cookies.")
            fecha = registrar_acceso(USUARIO)

            archivo_local = "dropbox_result.png"
            archivo_remoto = f"/{archivo_local}"
            if os.path.exists(archivo_local):
                subir_a_dropbox(archivo_local, archivo_remoto)

            time.sleep(1)
            enviar_correo(USUARIO, fecha)

            input("Presiona ENTER para cerrar el navegador...")
            browser.close()

    except Exception as error_general:
        print("❌ Ocurrió un error. Revisa 'registro_errores.log'.")
        logging.error("Error general en el flujo principal: %s", error_general)

        log_local = "registro_errores.log"
        log_remoto = f"/errores/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_log.txt"
        try:
            subir_a_dropbox(log_local, log_remoto)
            print("🗂️ Log de errores subido a Dropbox.")
        except Exception as e:
            print("⚠️ No se pudo subir el log a Dropbox.")
            logging.error("Error al subir log de errores: %s", e)

# ----------------------------
# ▶️ Ejecutar script
# ----------------------------
if __name__ == "__main__":
    usar_cookies()
