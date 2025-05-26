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


# Obtener la publicación por su contenido 
publicacion = session.query(Publicacion).filter(Publicacion.contenido == 'Bruno Fernandes del Liverpool fue expulsado por doble amarilla en el debut de la temporada.').first()

# Obtener todas las reacciones que pertenecen a esa publicación utilizamos el filter para buscar la publicacion asociada a es areaccion
reacciones = session.query(Reaccion).filter(Reaccion.publicacion_id == publicacion.id).all()

# se presneta el tipo de reacción y el nombre del usuario que reaccionó
for reaccion in reacciones:
    print(f"{reaccion.emocion} - {reaccion.usuario.nombre}")


