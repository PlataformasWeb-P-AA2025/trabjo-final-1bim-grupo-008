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
usuario = session.query(Usuario).filter(Usuario.nombre == 'Shelley').first()

# Obtener todas las reacciones realizadas por ese usuario utilizando el filter
reacciones = session.query(Reaccion).filter(Reaccion.usuario_id == usuario.id).all()

# Mostramos el contenido de la publicación a la que reaccionó
for reaccion in reacciones:
    print(reaccion.publicacion.contenido)


