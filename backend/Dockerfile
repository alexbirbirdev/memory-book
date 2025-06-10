FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip setuptools && pip install -r requirements.txt

COPY . .

RUN python ./manage.py collectstatic --noinput

RUN mkdir -p /app/mediafiles /app/backend/mediafiles && \
    chown -R appuser:appuser /app/mediafiles /app/backend/mediafiles

USER appuser

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
