from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from DB.genera_table import Usuario, Publicacion,Reaccion

# se importa información del archivo configuracion
from Puente.configuracion import cadena_base_datos 
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Leemos los archivos
with open('data/datos_clubs.txt', 'r', encoding='utf-8') as f:
    lineas_clubs = f.readlines()

with open('data/datos_jugadores.txt', 'r', encoding='utf-8') as f:
    lineas_jugadores = f.readlines()

# Creamos los objetos Club
clubs_dict = {}  

for linea in lineas_clubs:
    partes = linea.strip().split(';')
    #tomamos el valor de cada columna
    nombre, deporte, fundacion = partes
    #creamos el club
    club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
    #lo añadimos a la seecion
    session.add(club)
    #guardamos en el diccionario para busqueda posterior
    clubs_dict[nombre.strip()] = club  



for linea in lineas_jugadores:
    partes = linea.strip().split(';')
    #tomamos cada valor por cada columna de jugador
    nombre_club, posicion, dorsal, nombre_jugador = partes
    #tomamos el nombre del club mas importante
    nombre_club = nombre_club.strip()
    # Buscar el club correspondiente accediendo al key del diccionario de clubs
    club = clubs_dict.get(nombre_club)
    #creamos el objeto jugador
    jugador = Jugador(nombre=nombre_jugador.strip(),posicion=posicion.strip(),dorsal=int(dorsal),club=club)
    #lo añadimos a la seecion
    session.add(jugador)

# Guardamos los jugadores en la base
session.commit()

# Mostrar resultados
print("CLUBES")
for club in session.query(Club).all():
    print(f"{club.nombre} - {club.deporte} - {club.fundacion}")

print("\nJUGADORES")
for jugador in session.query(Jugador).all():
    print(f"{jugador.nombre} - {jugador.posicion} - {jugador.dorsal} - Club: {jugador.club.nombre}")