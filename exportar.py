import json
from pymongo import MongoClient
from bson import json_util

# Conectar a la base de datos local de MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["abd"]

colecciones = ["Recinto", "Artista", "Evento", "Asistente"]

# Recorrer cada colección y volcar los datos en un archivo JSON
for col_name in colecciones:
    documentos = list(db[col_name].find({}))
    with open(f"./{col_name}.json", "w", encoding="utf-8") as f:
        f.write(json_util.dumps(documentos, indent=4, ensure_ascii=False))
    print(f"Generado correctamente: {col_name}.json")