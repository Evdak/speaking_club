from robokassa.signals import result_received
from robokassa.models import SuccessNotification
from robokassa.forms import _RedirectPageForm
from django.db import models
from django.contrib.auth import get_user_model

from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.postgres.fields import JSONField

from apps.speaking_clubs.helpers import generate_success_form
from speaking_club.settings import EMAIL_HOST_USER

User = get_user_model()

WEEKDAYS = (
    ('Понедельник - Среда - Пятница', 'Понедельник - Среда - Пятница'),
    ('Вторник - Четверг - Суббота', 'Вторник - Четверг - Суббота'),
)

TEST = {
    "nav-Writing": [],
    "nav-Listening": [],
    "nav-Vocabulary": [],
    "nav-Grammar": [],
    "nav-Reading": []
}


def get_test():
    return TEST


class Level(models.Model):
    name = models.CharField(
        'Имя',
        max_length=255,
        choices=(
            ('A1', 'A1'),
            ('A2', 'A2'),
            ('B1', 'B1'),
            ('B2', 'B2'),
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
        choices=WEEKDAYS,
    )

    time = models.CharField(
        'Время начала занятия',
        max_length=255,
    )

    def __str__(self):
        return f"{self.level} {self.weekdays} {self.time}"

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Offer(models.Model):
    period = models.CharField(
        "Период",
        max_length=255,
    )

    description = models.TextField(
        "Описание",
    )

    price = models.PositiveIntegerField(
        "Цена",
    )

    class Meta:
        verbose_name = 'Пакет'
        verbose_name_plural = 'Пакеты'


class Order(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )

    invoice_number = models.PositiveIntegerField(
        "Номер закза",
    )

    offer = models.ForeignKey(
        Offer,
        on_delete=models.CASCADE,
        verbose_name="Пакет",
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )

    name = models.CharField(
        "Имя",
        max_length=255,
    )

    email = models.EmailField(
        "Эл. почта",
    )

    time = models.CharField(
        'Время начала занятия',
        max_length=255,
    )

    weekdays = models.CharField(
        "Дни недели",
        max_length=255,
        choices=WEEKDAYS,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


def payment_received(sender: SuccessNotification, **kwargs):
    print('init')
    order = Order.objects.filter(invoice_number=kwargs.get("InvId")).first()

    if order:

        form = generate_success_form(
            cost=kwargs.get("OutSum"),
            number=kwargs.get("InvId")
        )

        msg = render_to_string('email.html', {'form': form})
        plain_message = strip_tags(msg)
        print(msg)
        subject, from_email, to = 'Успешная оплата', EMAIL_HOST_USER, order.email
        text_content = strip_tags(msg)
        html_content = msg
        msg = EmailMultiAlternatives(subject, "text_content", from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        # send_mail('Успешная оплата', plain_message, EMAIL_HOST_USER,
        #           [order.email], html_message=msg)


result_received.connect(payment_received)


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )

    email = models.EmailField('Почта')
    name = models.CharField(
        'Имя',
        max_length=255,
    )

    test = JSONField(  # TOJSON
        "Результаты тестов",
        default=get_test,
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
        related_name="chat",
        blank=True,
    )

    def students_count(self):
        return len(self.students)

    def __str__(self):
        return f"{self.group} № {self.id}"

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
