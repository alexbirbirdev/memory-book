from django.db import models


class MilitaryRank(models.Model):
    """Воинское звание"""
    RANK_CHOICES = [
        ('private', 'Рядовой'),
        ('corporal', 'Ефрейтор'),
        ('mlsergeant', 'Мл.Сержант'),
        ('sergeant', 'Сержант'),
        ('stsergeant', 'Ст.Сержант'),
        ('pettyofficer', 'Старшина'),
        ('mllieutenant', 'Мл.Лейтенант'),
        ('lieutenant', 'Лейтенант'),
        ('stlieutenant', 'Ст.Лейтенант'),
        ('captain', 'Капитан'),
        ('major', 'Майор'),
        ('lieutenantcolonel', 'Подполковник'),
        ('colonel', 'Полковник'),
        ('majorgeneral', 'Генерал-майор'),
        ('lieutenantgeneral', 'Генерал-лейтенант'),
        ('colonelgeneral', 'Генерал-полковник'),
        ('armygeneral', 'Генерал армии'),
        ('marshal', 'Маршал'),
    ]

    rank = models.CharField(
        max_length=20,
        choices=RANK_CHOICES,
        unique=True,
        verbose_name='Звание'
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок сортировки')

    class Meta:
        verbose_name = 'Воинское звание'
        verbose_name_plural = 'Воинские звания'
        ordering = ['order']

    def __str__(self):
        return self.get_rank_display()


class BranchOfService(models.Model):
    """Род войск"""
    BRANCH_CHOICES = [
        ('ground', 'Сухопутные войска'),
        ('navy', 'Военно-морской флот'),
        ('air', 'Военно-воздушные силы'),
        ('pvo', 'Войска противовоздушной обороны'),
        ('border', 'Погранвойска'),
        ('nkvd', 'Войска НКВД'),
        ('medical', 'Военно-медицинская служба'),
    ]

    branch = models.CharField(
        max_length=20,
        choices=BRANCH_CHOICES,
        unique=True,
        verbose_name='Род войск'
    )

    class Meta:
        verbose_name = 'Род войск'
        verbose_name_plural = 'Рода войск'

    def __str__(self):
        return self.get_branch_display()


class Conflict(models.Model):
    """Военный конфликт"""
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Конфликт'
        verbose_name_plural = 'Конфликты'

    def __str__(self):
        return self.name


class Battle(models.Model):
    """Сражение"""
    name = models.CharField(max_length=255, verbose_name='Название')
    conflict = models.ForeignKey(Conflict, on_delete=models.CASCADE, verbose_name='Конфликт')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания', null=True, blank=True)

    class Meta:
        verbose_name = 'Сражение'
        verbose_name_plural = 'Сражения'

    def __str__(self):
        return f"{self.name} ({self.conflict})"


class Reward(models.Model):
    """Награда"""
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'

    def __str__(self):
        return self.name


class Veteran(models.Model):
    """Ветеран"""
    TYPE_CHOICES = [
        ('combat', 'Ветеран боевых действий'),
        ('homefront', 'Труженик тыла'),
    ]

    # Основная информация
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    death_date = models.DateField(verbose_name='Дата смерти', null=True, blank=True)
    biography = models.TextField(blank=True, verbose_name='Биография')
    photo = models.ImageField(upload_to='veterans/photos/', null=True, blank=True, verbose_name='Фотография')
    veteran_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default='combat',
        verbose_name='Тип ветерана'
    )

    # Военная служба
    military_rank = models.ForeignKey(
        MilitaryRank,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Воинское звание'
    )
    branch_of_service = models.ForeignKey(
        BranchOfService,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Род войск'
    )
    conflict = models.ForeignKey(
        Conflict,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Конфликт'
    )
    battles = models.ManyToManyField(Battle, blank=True, verbose_name='Сражения')
    rewards = models.ManyToManyField(Reward, through='VeteranReward', blank=True, verbose_name='Награды')

    # Места службы
    call_place = models.CharField(max_length=255, blank=True, verbose_name='Место призыва')
    service_place = models.CharField(max_length=255, blank=True, verbose_name='Место службы')
    military_unit = models.CharField(max_length=255, blank=True, verbose_name='Воинское формирование')

    # Дополнительная информация
    is_approved = models.BooleanField(default=False, verbose_name='Одобрено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')



    class Meta:
        verbose_name = 'Ветеран'
        verbose_name_plural = 'Ветераны'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()

    @property
    def full_name(self):
        """Полное имя ветерана"""
        return str(self)


class VeteranReward(models.Model):
    """Награда ветерана с дополнительными полями"""
    veteran = models.ForeignKey(Veteran, on_delete=models.CASCADE, verbose_name='Ветеран')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, verbose_name='Награда')
    document_number = models.CharField(max_length=100, blank=True, verbose_name='Номер наградного документа')
    award_date = models.DateField(null=True, blank=True, verbose_name='Дата награждения')

    class Meta:
        verbose_name = 'Награда ветерана'
        verbose_name_plural = 'Награды ветеранов'

    def __str__(self):
        return f"{self.veteran} - {self.reward}"