from django.apps import AppConfig


class MemoryBookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'memory_book_app'

    def ready(self):
        # Импорт сигналов только после загрузки приложения
        from . import signals  # noqa