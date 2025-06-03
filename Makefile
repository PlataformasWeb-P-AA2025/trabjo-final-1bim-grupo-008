# Levantar contenedor Docker con PostgreSQL y el contenedor de la app
docker-up:
	docker compose up -d --build

# Parar contenedores
docker-down:
	docker compose down

# Crear tablas
crear-tablas:
	docker exec proyecto-app python3 DB/genere_table_Postgres.py

# Llenar datos
llenar-datos:
	docker exec proyecto-app python3 Registros/ingreso_datosPostgres.py

# Todo
todo: docker-up crear-tablas llenar-datos
