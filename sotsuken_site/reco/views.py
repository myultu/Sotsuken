from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def reco(request):
    return render(request, 'reco.html')
