from django.db import models


class Document(models.Model):
    """Документ"""
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    file = models.FileField(upload_to='documents/', verbose_name='Файл')
    document_number = models.CharField(max_length=100, blank=True, verbose_name='Номер документа')
    start_date = models.DateField(null=True, blank=True, verbose_name='Дата начала действия')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания действия')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['-upload_date']

    def __str__(self):
        return self.title

    @property
    def file_size(self):
        """Размер файла в удобочитаемом формате"""
        if self.file:
            size = self.file.size
            if size < 1024:
                return f"{size} Б"
            elif size < 1024 * 1024:
                return f"{size / 1024:.1f} КБ"
            else:
                return f"{size / (1024 * 1024):.1f} МБ"
        return "0 Б"