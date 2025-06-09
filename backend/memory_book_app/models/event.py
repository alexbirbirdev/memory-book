from django.db import models


class Event(models.Model):
    """Мероприятие"""
    STATUS_CHOICES = [
        ('planned', 'Запланировано'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено'),
    ]

    FORMAT_CHOICES = [
        ('online', 'Онлайн'),
        ('offline', 'Оффлайн'),
        ('hybrid', 'Гибридный'),
    ]

    title = models.CharField(max_length=255, verbose_name='Название')
    short_description = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Содержание')
    preview_image = models.ImageField(
        upload_to='events/previews/',
        verbose_name='Изображение для анонса'
    )
    detail_image = models.ImageField(
        upload_to='events/details/',
        null=True,
        blank=True,
        verbose_name='Детальное изображение'
    )
    start_date = models.DateTimeField(verbose_name='Дата и время начала')
    end_date = models.DateTimeField(verbose_name='Дата и время окончания')
    location = models.CharField(max_length=255, blank=True, verbose_name='Место проведения')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='planned',
        verbose_name='Статус'
    )
    format = models.CharField(
        max_length=10,
        choices=FORMAT_CHOICES,
        default='offline',
        verbose_name='Формат'
    )
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['-start_date']

    def __str__(self):
        return self.title