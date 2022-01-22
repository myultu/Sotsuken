from django.urls import path
from . import views

app_name = 'sign'

urlpatterns = [
    path('', views.sign, name='sign'),
    path('in/', views.signin, name='signin'),
    path('out/', views.signout, name='signout'),
]
