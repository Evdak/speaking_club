from django.contrib import admin
from speaking_clubs import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
    )
    list_filter = list_display


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
    )
    list_filter = list_display


@admin.register(models.Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    list_filter = list_display


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'level',
        'weekdays',
        'time',
    )

    list_filter = list_display


@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = (
        'group',
        'chat',
        'group',
        'teacher',
    )
    list_filter = list_display
