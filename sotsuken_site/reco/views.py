from django.shortcuts import render

# Create your views here.
def reco(request):
    return render(request, 'reco.html')