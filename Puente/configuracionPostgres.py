# este módulo será usado para posibles configuraciones
#
# cadena conector a la base de datos
import os
#
cadena_base_datos = f"postgresql+psycopg2://{os.getenv('DB_USER', 'proyectouser')}:{os.getenv('DB_PASSWORD', '09081999')}@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'proyecto')}"


