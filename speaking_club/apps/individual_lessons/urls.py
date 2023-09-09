from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('<str:gc_user>/', views.index, name='individual_lessons_index'),
    path('<str:gc_user>/date/', views.get_date, name='individual_lessons_get_date'),
    path('<str:gc_user>/change_teacher/', views.change_teacher, name='individual_lessons_change_teacher'),
    path('<str:gc_user>/delete_lesson/', views.delete_lesson, name='individual_lessons_delete_lesson'),
]
