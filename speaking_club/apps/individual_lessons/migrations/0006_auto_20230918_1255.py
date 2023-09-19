# Generated by Django 2.2.27 on 2023-09-18 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speaking_clubs', '0020_auto_20230918_1248'),
        ('individual_lessons', '0005_auto_20230909_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individualstudent',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='individualstudent',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='individualstudent',
            name='level',
        ),
        migrations.AddField(
            model_name='individualstudent',
            name='student',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='speaking_clubs.Student', verbose_name='Ученик'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='individualtopic',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speaking_clubs.Level', verbose_name='Уровень'),
        ),
    ]
