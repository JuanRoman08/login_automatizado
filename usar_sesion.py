from playwright.sync_api import sync_playwright

def usar_sesion_guardada():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="sesion_autenticada.json")
        page = context.new_page()

        page.goto("https://www.dropbox.com/home")

        print("✅ Acceso exitoso. Ya estás dentro de tu cuenta Dropbox.")
        input("🟢 Presiona ENTER para cerrar el navegador...")

        browser.close()

if __name__ == "__main__":
    usar_sesion_guardada()
