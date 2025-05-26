from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,func # se importa el operador and
import os,sys
sys.path.insert(0,os.path.abspath(os.path.join(__file__,"..","..")))

from DB.genera_table import *
from Puente.configuracion import cadena_base_datos 
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#Consulta 1
# join permite acceder a Reaccion desde Usuario
# group_by agrupa por nombre del usuario
# count(Reaccion.id) cuenta cuántas reacciones hizo
reporte = session.query(Usuario.nombre,func.count(Reaccion.id)).join(Reaccion).group_by(Usuario.nombre).all()

print("\nConsulta 1: Reacciones por usuario")
for nombre, total in reporte:
    print(f"{nombre} hizo {total} reacciones")


#Segunda Consulta
# join permite acceder a usuario.nombre
# ilike('%mar%') busca "mar" en cualquier parte del nombre
reacciones = session.query(Reaccion).join(Usuario).filter(Usuario.nombre.ilike('%mar%')).all()

print("\nConsulta 2: Reacciones de usuarios cuyo nombre contiene 'mar'")
for reaccion in reacciones:
    print(f"{reaccion.usuario.nombre} reaccionó con '{reaccion.emocion}'")


#Consulta 3
# ~Usuario.nombre.ilike('%a') NIEGA que termine en "a"
# el comodin ~ niega la expresion
# Se aplica a todas las vocales

reacciones = session.query(Reaccion).join(Usuario).filter(
    ~Usuario.nombre.ilike('%a'),
    ~Usuario.nombre.ilike('%e'),
    ~Usuario.nombre.ilike('%i'),
    ~Usuario.nombre.ilike('%o'),
    ~Usuario.nombre.ilike('%u')
).all()

print("\nConsulta 3: Reacciones de usuarios cuyos nombres no terminan en vocal")
for reaccion in reacciones:
    print(f"{reaccion.usuario.nombre} - {reaccion.emocion}")

#Consulta 4
# join para acceder a Reaccion
# filtramos por emocion == 'pensativo'
# distinct() evita nombres duplicados

usuarios = session.query(Usuario.nombre).join(Reaccion).filter(Reaccion.emocion == "pensativo").distinct().all()

print("\nConsulta 4: Usuarios que reaccionaron con 'pensativo'")
for nombre in usuarios:
    print(nombre[0])


#Consulta 5
# join une la tabla Publicacion con Reaccion
# agrupamos por el contenido de cada publicación
# contamos cuántas reacciones recibió cada publicación

reporte = session.query(Publicacion.contenido,func.count(Reaccion.id)).join(Reaccion).group_by(Publicacion.contenido).all()

print("\nConsulta 5: Reacciones por publicación")
for contenido, total in reporte:
    print(f"'{contenido[:30]}...' recibió {total} reacciones")

