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

# Creamos una lista con los tipos de reacción que nos interesan
emociones = ["alegre", "enojado", "pensativo"]

# Filtrar las reacciones que coincidan con los tipos dados
# y cuyos usuarios no tengan nombres que inicien con vocal
# Hacemos un JOIN con la tabla Usuario usando la relación Reaccion.usuario
# Filtramos para que solo considere las reacciones cuyo tipo esté en la lista
# Excluimos usuarios cuyo nombre comience con 'a' (sin importar mayúsculas/minúsculas)
reacciones = session.query(Reaccion).join(Usuario).filter(Reaccion.emocion.in_(emociones),                     
    ~Usuario.nombre.ilike('a%'),                
    ~Usuario.nombre.ilike('e%'),
    ~Usuario.nombre.ilike('i%'),
    ~Usuario.nombre.ilike('o%'),
    ~Usuario.nombre.ilike('u%')
).all()

# Mostramostipo de reacción y nombre del usuario
for reaccion in reacciones:
    print(f"{reaccion.emocion} - {reaccion.usuario.nombre}")
