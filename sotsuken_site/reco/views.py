from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def reco(request, username):
    
    sentences = ['I walk', 'around my house', 'all day long.']
    context = {'sentences':sentences}
    
    return render(request, 'reco.html', context)