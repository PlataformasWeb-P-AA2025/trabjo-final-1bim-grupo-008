#!/bin/bash

# Espera a que PostgreSQL esté listo
/wait-for-it.sh postgres:5432 --timeout=30

# Crea las tablas
python3 DB/genere_table_Postgres.py

# Mantén el contenedor en ejecución
exec tail -f /dev/null