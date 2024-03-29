# Generated by Django 2.2.27 on 2023-12-07 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speaking_clubs', '0022_auto_20231103_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='weekdays',
            field=models.CharField(choices=[('Понедельник - Пятница', 'Понедельник - Пятница'), ('Среда - Суббота', 'Среда - Суббота'), ('Понедельник - Суббота', 'Понедельник - Суббота'), ('Понедельник - Четверг', 'Понедельник - Четверг'), ('Вторник - Воскресенье', 'Вторник - Воскресенье'), ('Вторник - Пятница', 'Вторник - Пятница')], max_length=255, verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='order',
            name='weekdays',
            field=models.CharField(blank=True, choices=[('Понедельник - Пятница', 'Понедельник - Пятница'), ('Среда - Суббота', 'Среда - Суббота'), ('Понедельник - Суббота', 'Понедельник - Суббота'), ('Понедельник - Четверг', 'Понедельник - Четверг'), ('Вторник - Воскресенье', 'Вторник - Воскресенье'), ('Вторник - Пятница', 'Вторник - Пятница')], max_length=255, null=True, verbose_name='Дни недели'),
        ),
    ]
