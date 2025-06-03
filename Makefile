# Makefile - automatización para entorno de base de datos

# Levantar contenedor Docker con PostgreSQL
docker-up:
	docker-compose up -d

# Parar contenedor Docker
docker-down:
	docker-compose down

# Crear las tablas en la base de datos
crear-tablas:
	python DB/genere_table_Postgres.py

# Llenar las tablas con los datos CSV
llenar-datos:
	python Registros/ingreso_datosPostgres.py

# Eliminar datos creados en el volumen (si se quiere reiniciar)
borrar-datos:
	docker-compose down -v

# Ejecutar todo: docker + crear tablas + llenar datos
todo: docker-up crear-tablas llenar-datos
