from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os,sys
sys.path.insert(0,os.path.abspath(os.path.join(__file__,"..","..")))

from DB.genera_table import *
from Puente.configuracionPostgres import cadena_base_datos 
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

"""
#llenamos usuario

for usu in usuarios[1:]:
    usuario = Usuario(nombre=usu.strip())
    session.add(usuario)

#llenamos publicaciones

for publi in publicaciones[1:]:
    partes = publi.strip().split('|')
    usu,publicacion = partes
    usuario = session.query(Usuario).filter_by(nombre=usu).first()
    if usuario:
        publicacion = Publicacion(contenido=publicacion, usuario=usuario)
        session.add(publicacion)

#llenamos Reacciones

for reac in reacciones[1:]:
    partes = reac.strip().split('|',2)
    usu,publi,reaccion = partes
    usuario = session.query(Usuario).filter_by(nombre=usu).first()
    publicacion = session.query(Publicacion).filter_by(contenido=publi).first()
    if usuario and publicacion:
        reaccion = Reaccion(usuario=usuario, publicacion=publicacion, emocion=reaccion)
        session.add(reaccion)
"""
# Guardamos todo en la base
session.commit()

