from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and
import os,sys
sys.path.insert(0,os.path.abspath(os.path.join(__file__,"..","..")))

from DB.genera_table import *
from Puente.configuracion import cadena_base_datos 
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Obtener el usuario por su nombre
usuario = session.query(Usuario).filter(Usuario.nombre == 'Larry').first()

# Obtener todas las publicaciones asociadas a ese usuario utilizamos el filter para encontrar el usuario relacionado a la publicacion
publicaciones = session.query(Publicacion).filter(Publicacion.usuario_id == usuario.id).all()

# Mostrar cada contenido de las publicaciones del usuario
for pub in publicaciones:
    print(pub.contenido)


