from playwright.sync_api import sync_playwright

def guardar_sesion():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()  # Ya no le pasamos storage_state aquí ❌
        page = context.new_page()

        page.goto("https://www.dropbox.com/login")

        print("\n🔐 Inicia sesión manualmente (correo, contraseña y captcha si hay).")
        print("⚠️ NO cierres el navegador tú mismo.")
        input("⏳ Presiona ENTER cuando ya hayas iniciado sesión completamente...")

        # Aquí recién guardamos la sesión correctamente ✅
        context.storage_state(path="sesion_autenticada.json")
        print("✅ Sesión guardada correctamente como sesion_autenticada.json")

        browser.close()

if __name__ == "__main__":
    guardar_sesion()
