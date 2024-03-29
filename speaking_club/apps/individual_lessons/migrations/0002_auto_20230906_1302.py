# Generated by Django 2.2.27 on 2023-09-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individual_lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='individuallesson',
            options={'verbose_name': 'Занятие', 'verbose_name_plural': 'Занятия'},
        ),
        migrations.AlterModelOptions(
            name='individuallevel',
            options={'verbose_name': 'Уровень', 'verbose_name_plural': 'Уровни'},
        ),
        migrations.AlterModelOptions(
            name='individualstudent',
            options={'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
        migrations.AlterModelOptions(
            name='individualteacher',
            options={'verbose_name': 'Преподаватель', 'verbose_name_plural': 'Преподаватели'},
        ),
        migrations.AlterModelOptions(
            name='individualtopic',
            options={'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
        migrations.AlterField(
            model_name='individualstudent',
            name='hours_paid',
            field=models.PositiveIntegerField(default=0, verbose_name='Часов оплачено'),
        ),
    ]
