from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.user, name='user'),
    #path('<slug:slug>', views.user_index, name='user_index'),
]
