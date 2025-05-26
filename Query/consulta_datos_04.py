from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and
import os,sys
from sqlalchemy import func
sys.path.insert(0,os.path.abspath(os.path.join(__file__,"..","..")))

from DB.genera_table import *
from Puente.configuracion import cadena_base_datos 
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Consulta: agrupar las reacciones por tipo y contar cuántas veces aparece cada tipo.
# Seleccionamos la columna emocion de la tabla Reaccion.
# Contamos cuántas veces aparece cada emocion usando la función SQL COUNT.
# Agrupamos los resultados por el campo emocion para que cuente por grupo.
# Ejecutamos la consulta y obtenemos todos los resultados.
reporte = session.query(Reaccion.emocion,func.count(Reaccion.emocion)).group_by(Reaccion.emocion).all()                        

# Mostramos cada tipo de reacción y su cantidad
for tipo, cantidad in reporte:
    print(f"{tipo} = {cantidad}")



