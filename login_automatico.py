from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()
USUARIO = os.getenv("USUARIO")
CONTRASENA = os.getenv("CONTRASENA")

def login_automatico():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.dropbox.com/login")
        print("🌐 Página cargada...")

        # Cerrar cookies
        try:
            page.wait_for_selector("text=Aceptar todo", timeout=6000)
            page.locator("text=Aceptar todo").click()
            print("🍪 Cookies aceptadas.")
        except:
            print("⚠️ No se mostró el banner de cookies o ya estaba cerrado.")

        # Escribir correo
        page.wait_for_selector("input[type='email']", timeout=10000)
        page.fill("input[type='email']", USUARIO)
        print("✉️ Correo ingresado.")

        # Click en Continuar
        page.click("button:has-text('Continuar')")
        print("➡️ Click en 'Continuar'...")

        # Esperar navegación (cambio de URL)
        page.wait_for_url("**/start_auth_flow**", timeout=10000)

        # Esperar campo de contraseña visible
        page.wait_for_selector("input[type='password']:not([id*='autofill'])", timeout=10000)
        page.fill("input[type='password']:not([id*='autofill'])", CONTRASENA)
        print("🔐 Contraseña ingresada.")

        # Click en iniciar sesión
        page.click("button[type='submit']")
        print("🚀 Intentando iniciar sesión...")

        # Esperar 5-10 segundos para ver el resultado
        page.wait_for_timeout(8000)
        page.screenshot(path="login_resultado.png")
        print("📸 Screenshot tomada: login_resultado.png")

        browser.close()

if __name__ == "__main__":
    login_automatico()
