import os
from dotenv import load_dotenv
import dropbox

load_dotenv()

token = os.getenv("DROPBOX_TOKEN")
dbx = dropbox.Dropbox(token)

try:
    cuenta = dbx.users_get_current_account()
    print("✅ Token válido. Usuario:", cuenta.name.display_name)
except Exception as e:
    print("❌ Token inválido o expirado:", e)
