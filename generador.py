import os
import json
import hashlib
from urllib.parse import quote

# Reemplaza TU_USUARIO y servidor-mc-mods por los datos reales de tu repo
# Nota: Verifica si tu rama principal se llama "main" o "master"
BASE_URL = "https://raw.githubusercontent.com/JacsonAulla/servidor-mc-mods/main"

def get_md5(filepath):
    h = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

manifest = {"mods": [], "resourcepacks": [], "config": []}

for folder in ["mods", "resourcepacks", "config"]:
    os.makedirs(folder, exist_ok=True)
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            # quote() asegura que si un mod tiene espacios o símbolos en el nombre, la URL no falle
            safe_filename = quote(filename)
            manifest[folder].append({
                "name": filename,
                "url": f"{BASE_URL}/{folder}/{safe_filename}",
                "md5": get_md5(filepath)
            })

with open("manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

print("¡Archivo manifest.json generado con éxito!")