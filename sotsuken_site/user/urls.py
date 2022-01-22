from django.urls import include, path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.user, name='user'), 
    path('reco/', include('reco.urls')),
    path('show/', include('show.urls')),
]
