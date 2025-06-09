from django.db import models


class Banner(models.Model):
    """Баннер на главной странице"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image_desktop = models.ImageField(
        upload_to='banners/desktop/',
        verbose_name='Изображение для десктопа'
    )
    image_tablet = models.ImageField(
        upload_to='banners/tablet/',
        verbose_name='Изображение для планшета',
        null=True,
        blank=True
    )
    image_mobile = models.ImageField(
        upload_to='banners/mobile/',
        verbose_name='Изображение для мобильного',
        null=True,
        blank=True
    )
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ['order']

    def __str__(self):
        return self.title