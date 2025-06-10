
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/media && \
    chmod -R 775 /app/media

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]