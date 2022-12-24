from django.db import models


class Level(models.Model):
    name = models.CharField(
        'Имя',
        max_length=255,
        choices=(
            ('Beginner', 'Beginner'),
            ('Pre-intermediate', 'Pre-intermediate'),
            ('Intermediate', 'Intermediate'),
            ('Upper-intermediate', 'Upper-intermediate'),
        )
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'


class Group(models.Model):
    level = models.ForeignKey(
        Level,
        verbose_name='Уровень',
        on_delete=models.CASCADE,
    )

    weekdays = models.CharField(
        'День недели',
        max_length=255,
        choices=(
            ('Понедельник - Среда - Пятница', 'Понедельник - Среда - Пятница'),
            ('Вторник - Четверг - Суббота', 'Вторник - Четверг - Суббота'),
        )
    )

    time = models.TimeField(
        'Время начала занятия',
    )

    def __str__(self):
        return f"{self.level} {self.weekday} {self.time}"

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Student(models.Model):
    email = models.EmailField('Почта')
    name = models.CharField(
        'Имя',
        max_length=255,
    )

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Teacher(models.Model):
    email = models.EmailField('Почта')
    name = models.CharField(
        'Имя',
        max_length=255,
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name='Группы',
    )

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'


class Chat(models.Model):
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        on_delete=models.CASCADE,
    )

    chat = models.URLField(
        "Ссылка на чат",
    )

    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        on_delete=models.CASCADE,
    )

    teacher = models.ForeignKey(
        Teacher,
        verbose_name='Куратор',
        on_delete=models.CASCADE,
    )

    students = models.ManyToManyField(
        Student,
        verbose_name='Ученики',
    )

    def __str__(self):
        return f"{self.group} № {self.id}"

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
