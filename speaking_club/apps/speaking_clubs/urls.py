from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='main'),
    path('order/', views.pay_with_robokassa),
    path('profile/', views.profile, name='profile'),
    path('update_session/', views.update_session),
    path('test/', views.test, name='test'),
    path('register_answer/', views.register_answer),
    path('get_answer/', views.get_answer),
    path('get_result/', views.get_result, name='result'),
    path('my_order/', views.my_order, name='my_order'),
]
