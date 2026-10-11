from pymongo import MongoClient
import ODM

def poblar():
    # 1. Limpiar la base de datos previa para evitar duplicados de clave única
    client = MongoClient("mongodb://localhost:27017/")
    client.drop_database("abd")

    # 2. Inicializar el ODM
    ODM.initApp(definitions_path="./models.yml", db_name="abd", scope=ODM.__dict__)

    print("Insertando Recintos...")
    r1 = ODM.Recinto(
        nombre="WiZink Center", 
        direccion="Avenida Felipe II, Madrid", 
        aforo=17453, 
        servicios=["Parking", "Bar"]
    )
    r1.save()

    r2 = ODM.Recinto(
        nombre="Sant Jordi Club", 
        direccion="Passeig Olímpic 5, Barcelona", 
        aforo=4600, 
        servicios=["Accesibilidad PMR"]
    )
    r2.save()

    print("Insertando Artistas...")
    a1 = ODM.Artista(
        nombre="Estopa", 
        generos=["Rumba", "Rock"], 
        pais="España", 
        ano_ini_act=1999
    )
    a1.save()

    a2 = ODM.Artista(
        nombre="Rosalía", 
        generos=["Flamenco", "Pop"], 
        pais="España", 
        ano_ini_act=2017
    )
    a2.save()

    print("Insertando Eventos...")
    e1 = ODM.Evento(
        titulo="Estopa Gira 25 Aniversario", 
        artistas=["Estopa"], 
        recinto="WiZink Center", 
        horario="2026-11-20T21:00:00", 
        precio={"pista": 45.0, "grada": 55.0}, 
        n_entradas_vend=15000
    )
    e1.save()

    e2 = ODM.Evento(
        titulo="Rosalía Motomami Tour", 
        artistas=["Rosalía"], 
        recinto="Sant Jordi Club", 
        horario="2026-12-05T20:30:00", 
        precio={"pista": 60.0}, 
        n_entradas_vend=4500
    )
    e2.save()

    print("Insertando Asistentes...")
    u1 = ODM.Asistente(
        nombre="Alejandro Soria", 
        correo_electronico="alex@gmail.com", 
        fecha_alta="2024-01-15", 
        direccion="Calle Gran Vía 12, Madrid", 
        pref_genero=["Rock", "Pop"]
    )
    u1.save()

    u2 = ODM.Asistente(
        nombre="Alonso López", 
        correo_electronico="alonso@gmail.com", 
        fecha_alta="2024-02-10", 
        direccion="Calle Alcala 50, Madrid", 
        pref_genero=["Rumba"]
    )
    u2.save()

    print("¡Base de datos poblada con éxito!")

if __name__ == '__main__':
    poblar()