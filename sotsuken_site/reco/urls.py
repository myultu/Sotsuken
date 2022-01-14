from django.urls import path

from . import views

urlpatterns = [
    path('', views.reco, name='reco'),
    path('templates/', views.reco_template, name='reco_template'),
]