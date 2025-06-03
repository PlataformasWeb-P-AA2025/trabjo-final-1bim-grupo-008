FROM python:3.10-slim

# Crea directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto
COPY . .

# Copia y da permisos al script de espera
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto (se puede sobrescribir desde docker-compose)
CMD ["python3"]
