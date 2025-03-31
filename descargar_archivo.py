import requests

def descargar_archivo(url, destino):
    response = requests.get(url)
    with open(destino, "wb") as f:
        f.write(response.content)
    print(f"✅ Archivo descargado: {destino}")

# Ejemplo de uso directo
if __name__ == "__main__":
    url = "https://example.com/archivo.xlsx"
    descargar_archivo(url, "archivo_descargado.xlsx")
