from robokassa.signals import result_received
from robokassa.models import SuccessNotification
from django.db import models
from django.contrib.auth import get_user_model

from django.core.mail import EmailMultiAlternatives
from django.contrib.postgres.fields import JSONField

from apps.speaking_clubs.helpers import generate_success_url
from speaking_club.settings import EMAIL_HOST_USER

from apps.speaking_clubs.helpers import calculate_levels

User = get_user_model()

WEEKDAYS = (
    ("Понедельник - Пятница", "Понедельник - Пятница"),
    ("Среда - Суббота", "Среда - Суббота"),
    ("Среда - Пятница", "Среда - Пятница"),
    ("Понедельник - Суббота", "Понедельник - Суббота"),
    ("Понедельник - Четверг", "Понедельник - Четверг"),
    ("Вторник - Воскресенье", "Вторник - Воскресенье"),
    ("Вторник - Пятница", "Вторник - Пятница"),
    ("Вторник - Четверг", "Вторник - Четверг"),
)

TEST = {
    "nav-Writing": -1,
    "nav-Listening": -1,
    "nav-Vocabulary": -1,
    "nav-Grammar": -1,
    "nav-Reading": -1,
}


def get_test():
    return TEST


class Level(models.Model):
    name = models.CharField(
        "Имя",
        max_length=255,
        choices=(
            ("A1", "A1"),
            ("A2", "A2"),
            ("B1", "B1"),
            ("B2", "B2"),
        ),
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"


class Stream(models.Model):
    name = models.CharField(
        "Название",
        max_length=255,
        blank=False,
        null=False,
    )

    gc_name = models.CharField(
        "Название в заказе",
        max_length=255,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Поток"
        verbose_name_plural = "Потоки"


class Group(models.Model):
    level = models.ForeignKey(
        Level,
        verbose_name="Уровень",
        on_delete=models.CASCADE,
    )

    weekdays = models.CharField(
        "День недели",
        max_length=255,
        choices=WEEKDAYS,
    )

    time = models.CharField(
        "Время начала занятия",
        max_length=255,
    )

    def __str__(self):
        return f"{self.level} {self.weekdays} {self.time}"

    def get_time(self) -> str:
        return f"{int(self.time)}:00 - {int(self.time)+1}:00" if self.time else ""

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


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

    def __str__(self):
        return f"{self.period} {self.price}"

    class Meta:
        verbose_name = "Пакет"
        verbose_name_plural = "Пакеты"


class OrderGC(models.Model):
    email = models.EmailField(
        "Эл. почта",
    )
    invoice_number = models.BigIntegerField(
        "Номер заказа",
    )
    user_id = models.CharField(
        "ID c GetCourse",
        max_length=255,
    )
    stream = models.ForeignKey(
        Stream,
        verbose_name="Поток",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    product = models.CharField(
        "Назваание предложения",
        max_length=255,
    )

    def __str__(self) -> str:
        return f"{self.invoice_number} {self.email}"

    @property
    def hours_paid(self) -> int | None:
        if self.product.lower().startswith("elite"):
            splitter = "|" if "|" else "•"
            return int(self.product.split(splitter)[1].split()[0].strip())

    class Meta:
        verbose_name = "Заказ c GetCourse"
        verbose_name_plural = "Заказы c GetCourse"


class Order(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )

    invoice_number = models.PositiveIntegerField(
        "Номер заказа",
    )

    offer = models.ForeignKey(
        Offer,
        on_delete=models.CASCADE,
        verbose_name="Пакет",
    )

    name = models.CharField(
        "Имя",
        max_length=255,
    )

    email = models.EmailField(
        "Эл. почта",
    )

    time = models.CharField(
        "Время начала занятия",
        max_length=255,
        null=True,
        blank=True,
    )

    weekdays = models.CharField(
        "Дни недели",
        max_length=255,
        choices=WEEKDAYS,
        null=True,
        blank=True,
    )

    order_from_gc = models.OneToOneField(
        OrderGC,
        on_delete=models.CASCADE,
        verbose_name="Заказ с GetCourse",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.user} {self.invoice_number}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


def payment_received(sender: SuccessNotification, **kwargs):
    order = Order.objects.filter(invoice_number=kwargs.get("InvId")).first()

    if order:
        url = generate_success_url(
            cost=kwargs.get("OutSum"), number=kwargs.get("InvId")
        )

        msg = f"""Успешная оплата, ваш заказ можно получить по ссылке: {url}"""
        subject, from_email, to = "Успешная оплата", EMAIL_HOST_USER, order.email
        msg = EmailMultiAlternatives(subject, msg, from_email, [to])
        msg.send()


result_received.connect(payment_received)


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )

    email = models.EmailField(
        "Почта",
        null=True,
        blank=True,
    )
    name = models.CharField(
        "Имя",
        max_length=255,
    )

    test = JSONField(
        "Результаты тестов",
        default=get_test(),
        blank=False,
        null=False,
    )

    is_paid = models.BooleanField(
        "С оплатой",
        default=True,
        blank=False,
        null=False,
    )

    stream = models.ForeignKey(
        Stream,
        verbose_name="Поток",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    is_done_by_manager = models.BooleanField(
        "Обработан",
        blank=False,
        null=False,
        default=False,
    )

    is_test_2 = models.BooleanField(
        "Перешел к тесту 2",
        default=False,
    )

    finished_test_1 = models.DateTimeField(
        "Время завершения 1 теста",
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} {self.email}"

    def _get_user_chat(self):
        return self.chat.first()

    def get_user_level(self):
        chat = self._get_user_chat()
        if chat:
            return chat.group.level
        if self.test:
            return calculate_levels(self.test, self.is_test_2)[-1].get("total")
        return None

    def get_user_teacher(self):
        chat = self._get_user_chat()
        return chat.teacher if chat else None

    def get_user_chat_url(self):
        chat = self._get_user_chat()
        return chat.chat if chat else None

    def get_user_tg(self):
        return f"@{self.user.username}" if self.user.username else None

    @property
    def gc_user(self) -> str | None:
        if self.is_paid:
            return self.user.order.order_from_gc.user_id

    @property
    def hours_paid(self) -> str | None:
        if self.is_paid and self.user.order.order_from_gc.hours_paid:
            return self.user.order.order_from_gc.hours_paid

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Teacher(models.Model):
    email = models.EmailField("Почта")
    name = models.CharField(
        "Имя",
        max_length=255,
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name="Группы",
    )

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = "Куратор"
        verbose_name_plural = "Кураторы"


class Chat(models.Model):
    chat = models.URLField(
        "Ссылка на чат",
    )

    group = models.ForeignKey(
        Group,
        verbose_name="Группа",
        on_delete=models.CASCADE,
    )

    teacher = models.ForeignKey(
        Teacher,
        verbose_name="Куратор",
        on_delete=models.CASCADE,
    )

    students = models.ManyToManyField(
        Student,
        verbose_name="Ученики",
        related_name="chat",
        blank=True,
    )

    stream = models.ForeignKey(
        Stream,
        verbose_name="Поток",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def students_count(self):
        return self.students.count()

    def __str__(self):
        return f"{self.group} № {self.id}"

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"


class Answer(models.Model):
    users = models.ManyToManyField(
        Student,
        verbose_name="Пользователь",
        blank=True,
    )

    quiz_id = models.UUIDField("№ задания")

    answer = JSONField("Ответ")

    def __str__(self):
        return f"{self.quiz_id} {self.answer}"

    class Meta:
        verbose_name = "Ответ ученика"
        verbose_name_plural = "Ответы учеников"
