from django.urls import path
from . import views

app_name = 'show'

urlpatterns = [
    path('', views.show, name='show'),
    path('<str:title>/', views.show_contents, name='show_contents'),
]