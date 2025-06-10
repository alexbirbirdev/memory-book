FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Создаем пользователя appuser
RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip setuptools && pip install -r requirements.txt

COPY . .

RUN python ./manage.py collectstatic --noinput

# Создаем папку для медиа и меняем владельца
RUN mkdir -p /app/mediafiles && chown -R appuser:appuser /app/mediafiles

# Переключаемся на пользователя appuser
USER appuser

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
