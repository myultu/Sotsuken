from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def reco(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def reco_template(request):
    return render(request, 'reco.html')