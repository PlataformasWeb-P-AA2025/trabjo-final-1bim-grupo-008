from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os,sys
sys.path.insert(0,os.path.abspath(os.path.join(__file__,"..","..")))


from DB.genera_table import Usuario, Publicacion,Reaccion
from Puente.configuracion import cadena_base_datos 
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Leemos los archivos
with open('DATA/usuarios_red_x.csv', 'r', encoding='utf-8') as f:
    usuarios = f.readlines()

with open('DATA/usuarios_publicaciones.csv', 'r', encoding='utf-8') as f:
    publicaciones = f.readlines()    

with open('DATA/usuario_publicacion_emocion.csv', 'r', encoding='utf-8') as f:
    reacciones = f.readlines()    


#llenamos usuario
for usu in usuarios:
    usuario = Usuario(nombre=usu.strip()[1:])





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

