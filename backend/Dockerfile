FROM python:3.12-slim

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Создаем не-root пользователя и рабочую директорию
RUN useradd -m appuser && \
    mkdir -p /app/media && \
    chown -R appuser:appuser /app

WORKDIR /app

# Копируем и устанавливаем зависимости
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

# Копируем весь проект с сохранением прав
COPY --chown=appuser:appuser . .

# Создаем статику
RUN python manage.py collectstatic --noinput

# Меняем владельца медиа папки
RUN chown -R appuser:appuser /app/media

RUN mkdir -p /app/backend/mediafiles && \
    chown -R appuser:appuser /app/backend/mediafiles


# Переключаемся на не-root пользователя
USER appuser

# Команда запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]