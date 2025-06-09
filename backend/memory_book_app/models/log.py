from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class LogEntry(models.Model):
    """Запись лога"""
    ACTION_CHOICES = [
        ('create', 'Создание'),
        ('update', 'Обновление'),
        ('delete', 'Удаление'),
        ('login', 'Вход'),
        ('logout', 'Выход'),
        ('error', 'Ошибка'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Пользователь',
        related_name='custom_log_entries'
    )
    action = models.CharField(
        max_length=10,
        choices=ACTION_CHOICES,
        verbose_name='Действие'
    )
    model = models.CharField(max_length=100, verbose_name='Модель')
    object_id = models.PositiveIntegerField(null=True, blank=True, verbose_name='ID объекта')
    details = models.TextField(blank=True, verbose_name='Детали')
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name='IP-адрес')
    user_agent = models.CharField(max_length=255, blank=True, verbose_name='User Agent')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время события')

    class Meta:
        verbose_name = 'Запись лога'
        verbose_name_plural = 'Записи логов'
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.get_action_display()} {self.model} by {self.user or 'system'}"