from django.db import models
from django.utils import timezone


class IndividualLevel(models.Model):
    name = models.CharField(
        'Уровень',
        max_length=255,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'


class IndividualTopic(models.Model):
    name = models.CharField(
        'Название',
        max_length=255,
    )

    level = models.ForeignKey(
        IndividualLevel,
        on_delete=models.CASCADE,
        verbose_name='Уровень',
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class IndividualTeacher(models.Model):
    gc_user = models.IntegerField(
        'ID с GetCourse',
    )

    first_name = models.CharField(
        'Имя',
        max_length=255,
    )

    last_name = models.CharField(
        'Фамилия',
        max_length=255,
    )

    photo = models.ImageField(
        'Фото профиля',
        upload_to='individual_lessons/img/teacher_photo',
        null=False,
        blank=False,
    )

    zoom_key = models.CharField(
        'Ключ Zoom',
        max_length=500,
    )
    zoom_sec = models.CharField(
        'Секретный ключ Zoom',
        max_length=500,
    )
    zoom_client = models.CharField(
        'Client ID Zoom',
        max_length=500,
    )

    def __str__(self) -> str:
        return " ".join((el for el in (self.first_name, self.last_name) if el))

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class IndividualStudent(models.Model):
    gc_user = models.IntegerField(
        'ID с GetCourse',
    )

    first_name = models.CharField(
        'Имя',
        max_length=255,
    )

    last_name = models.CharField(
        'Фамилия',
        max_length=255,
    )

    hours_paid = models.PositiveIntegerField(
        'Занятий оплачено',
        default=0,
        blank=False,
        null=False,
    )

    teacher = models.ForeignKey(
        IndividualTeacher,
        on_delete=models.CASCADE,
        verbose_name='Преподаватель',
        null=True,
        blank=True,
    )

    level = models.ForeignKey(
        IndividualLevel,
        on_delete=models.CASCADE,
        verbose_name='Уровень',
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class IndividualLesson(models.Model):
    status = models.CharField(
        "Статус",
        max_length=255,
        blank=False,
        null=False,
        choices=(
            ("Создан", "Создан"),
            ("Почти отменен", "Почти отменен"),
            ("Забронирован", "Забронирован"),
        ),
        default="Создан",
    )
    date = models.DateField(
        'Дата',
        blank=False,
        null=False,
    )

    time = models.TimeField(
        'Время',
        blank=False,
        null=False,
    )

    teacher = models.ForeignKey(
        IndividualTeacher,
        on_delete=models.CASCADE,
        verbose_name='Преподаватель',
        null=True,
        blank=True,
    )

    student = models.ForeignKey(
        IndividualStudent,
        on_delete=models.CASCADE,
        verbose_name='Ученик',
        null=True,
        blank=True,
    )

    topic = models.ForeignKey(
        IndividualTopic,
        on_delete=models.CASCADE,
        verbose_name='Тема',
        null=True,
        blank=True,
    )

    zoom_id = models.CharField(
        'ID встречи',
        blank=True,
        null=True,
        max_length=50,
    )
    zoom_url = models.URLField(
        'Ссылка на встречу',
        blank=True,
        null=True,
    )
    zoom_password = models.CharField(
        'Пароль встречи',
        max_length=20,
        blank=True,
        null=True,
    )

    def datetime(self) -> timezone.datetime:
        return timezone.datetime(
            year=self.date.year,
            month=self.date.month,
            day=self.date.day,
            hour=self.time.hour,
            minute=self.time.minute,
            second=self.time.second,
            microsecond=self.time.microsecond,
        )

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
