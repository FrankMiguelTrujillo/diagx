🔧 Git — comandos esenciales
Comando	Qué hace
git status	Muestra qué archivos cambiaron desde el último commit
git add .	Prepara TODOS los cambios para el commit ("staging")
git commit -m "mensaje"	Guarda una foto local con un mensaje descriptivo
git push	Sube los commits locales a GitHub
git log	Ve el historial de commits (fecha, mensaje, autor)
git branch	Muestra en qué rama estás parado

Flujo típico de cada sesión:

bash
git status          # ver qué cambió
git add .            # preparar cambios
git commit -m "feat: descripción corta de lo que hiciste"
git push             # subir a GitHub

Prefijos de mensaje de commit (conventional commits):

feat: → algo nuevo
fix: → corregiste un bug
refactor: → reorganizaste sin cambiar comportamiento
docs: → cambios de documentación
🚀 Uvicorn / FastAPI — comandos esenciales
Comando	Qué hace
uvicorn main:app --reload	Corre el servidor de FastAPI (busca la variable app dentro de main.py); --reload reinicia solo al guardar cambios

URLs útiles mientras el servidor corre:

http://127.0.0.1:8000/ → tu endpoint raíz
http://127.0.0.1:8000/docs → Swagger UI (probar endpoints sin Postman)

Errores comunes que ya viviste:

Attribute "app" not found in module "main" → el archivo está vacío (¿lo guardaste con Ctrl+S?) o la variable no se llama app.
Un archivo con el mismo nombre que una librería (ej. fastapi.py) puede tapar la librería real — nunca nombres tus archivos igual que un paquete instalado.
Si algo no actualiza después de corregirlo, borrá la carpeta __pycache__ y probá de nuevo.

Postgres local (Docker): usuario=postgres, password=diagx123, db=diagx, puerto=5432