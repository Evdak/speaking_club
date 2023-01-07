from django.contrib import admin
from speaking_clubs import models


if not hasattr(admin, "display"):
    def display(description):
        def decorator(fn):
            fn.short_description = description
            return fn
        return decorator
    setattr(admin, "display", display)


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'test',
    )
    list_filter = (
        'email',
        'name',
    )


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
        'id',
        'group',
        'teacher',
        'get_students_count'
    )
    
    list_filter  = (
        'group__level',
        'group__weekdays',
        'group__time',
        'teacher',
    )

    @admin.display(description='Кол-во учеников')
    def get_students_count(self, obj):
        return f"{obj.students_count()}/5"


@admin.register(models.Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'period',
        'description',
        'price',
    )
    list_filter = list_display


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_number',
        'offer',
        'user',
        'email',
        'time',
        'weekdays',
    )
    list_filter = list_display
