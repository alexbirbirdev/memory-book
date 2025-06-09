from django.db import models

class News(models.Model):
    """Новость"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    short_description = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Содержание')
    preview_image = models.ImageField(
        upload_to='news/previews/',
        verbose_name='Изображение для анонса'
    )
    detail_image = models.ImageField(
        upload_to='news/details/',
        null=True,
        blank=True,
        verbose_name='Детальное изображение'
    )
    publish_date = models.DateTimeField(verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-publish_date']

    def __str__(self):
        return self.title