FROM python:3.11-slim

WORKDIR /app

ENV DB_HOST=db-container
ENV DB_USER=postgres
ENV DB_NAME=postgres
ENV DB_PORT=5432
ENV DB_PASS=""

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["tail", "-f", "/dev/null"]