from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def show(request, username):
    
    titles = ['The breakfast', 'Shooting stars', 'I have many cap of popcorn']
    context = {'titles':titles}
    
    return render(request, 'show.html', context)

@login_required
def show_contents(request, username, title):
    
    #That title already have been generated
    bool_generated = True
    
    Edit_Mode = False
    
    if bool_generated == True:
    
        context = {'title':title}
        
        return render(request, 'show_contents.html', context)
    
    else:
        return redirect('show:show')