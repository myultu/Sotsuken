from django.urls import path

from . import views

urlpatterns = [
    path('', views.reco, name='reco'),
    path('templates/', views.reco, name='reco_template'),
]