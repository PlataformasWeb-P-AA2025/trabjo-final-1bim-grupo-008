FROM python:3.10-slim

WORKDIR /app

COPY . .

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY start.sh /start.sh
RUN chmod +x /start.sh

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/start.sh"]