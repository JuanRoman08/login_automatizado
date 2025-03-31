# 🤖 Proyecto de Login Automatizado con Playwright

Este proyecto realiza un **inicio de sesión automatizado en Dropbox** utilizando cookies persistentes con **Playwright**, guarda un registro en SQLite, **sube un archivo a Dropbox** y luego **envía una notificación por correo electrónico (HTML con emojis y tabla)** usando **Mailtrap SMTP**.

---

## 🚀 Funcionalidades

- ✅ Restauración automática de sesión en Dropbox mediante cookies (`cookies_dropbox.json`)
- 🗂️ Registro de accesos en una base de datos SQLite (`accesos.db`)
- ☁️ Subida automática de archivo (`dropbox_result.png`) a tu cuenta de Dropbox
- 📧 Envío de notificación de acceso vía Mailtrap (correo HTML personalizado)
- 📄 Subida de logs de errores a Dropbox en caso de fallo

---

## 🧪 Tecnologías Usadas

- `Python 3.10+`
- `Playwright` (automatización web)
- `SQLite3` (base de datos local)
- `Dropbox SDK`
- `smtplib` (correo SMTP)
- `dotenv` (gestión de variables del entorno)

---

## 🔧 Configuración Inicial

1. Clona el repositorio:

```bash
git clone https://github.com/JuanRoman08/login_automatizado.git
cd login_automatizado
```

2. Crea un archivo `.env` y añade tus credenciales:

DROPBOX_TOKEN=sl.xxxxxxx
USUARIO=tu_correo_dropbox@ejemplo.com

MAILTRAP_USER=xxxxxxxx
MAILTRAP_PASS=xxxxxxxx
EMAIL_FROM=tu_correo@gmail.com
EMAIL_TO=destinatario@correo.com

3. Instala los paquetes necesarios:

   pip install -r requirements.txt
4. Ejecuta el script principal:

   python usar_cookies.py

   ## 🖼️ Capturas de Pantalla

   | Restauración de Sesión | Subida a Dropbox | Notificación HTML |
   | ------------------------ | ---------------- | ------------------ |
   |                          |                  |                    |

   ---

   ## 🧠 Autor

   **Juan Diego Román Salazar**

   📧 `juandiegoromansalazar08@gmail.com`

   🔗 GitHub: [@JuanRoman08](https://github.com/JuanRoman08)

   ---

   ## 🛡️ Licencia

   Este proyecto está bajo la licencia MIT.

   ¡Siéntete libre de usarlo, mejorarlo o compartirlo!

---
### ✅ ¿Qué debes hacer ahora?

1. Crea una carpeta `screenshots` en tu proyecto:
```bash
mkdir screenshots
---
2. Guarda capturas como:

* `screenshots/sesion.png`
* `screenshots/dropbox.png`
* `screenshots/correo.png`
  3. Crea el archivo:

  code README.md

  4. Pega el contenido y guarda. Luego haz:

  git add README.md screenshots/
  git commit -m "📝 Agregado README profesional y screenshots"
  git push
