import dropbox
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("DROPBOX_TOKEN")

def subir_a_dropbox(ruta_local, ruta_remota):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    with open(ruta_local, "rb") as f:
        dbx.files_upload(f.read(), ruta_remota, mute=True)
    print("📤 Archivo subido a Dropbox.")

if __name__ == "__main__":
    subir_a_dropbox("archivo_descargado.xlsx", "/archivo_en_dropbox.xlsx")
