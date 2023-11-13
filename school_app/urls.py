from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('form/', views.form_page, name='form_page'),
    path('submit_form/', views.submit_form, name='submit_form'),
]
