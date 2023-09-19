from django.contrib import admin
from django.contrib.admin.decorators import register

from individual_lessons.models import *


@register(IndividualTopic)
class IndividualTopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'level',
    )

    list_filter = list_display


@register(IndividualTeacher)
class IndividualTeacherAdmin(admin.ModelAdmin):
    list_display = (
        'gc_user',
        'first_name',
    )

    list_filter = list_display


@register(IndividualStudent)
class IndividualStudentAdmin(admin.ModelAdmin):
    list_display = (
        'gc_user',
        # 'first_name',
        'hours_paid',
        'teacher',
        # 'level',
    )

    list_filter = list_display


@register(IndividualLesson)
class IndividualLessonAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'time',
        'teacher',
        'student',
        'topic',
    )

    list_filter = list_display
