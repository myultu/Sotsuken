from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from urllib.parse import urlencode

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def user(request):
    if request.method == 'POST':
        #if the request is for signin, check username and password
        """if(request.POST.get('User_sign_in', None) == 'user'):
            name = request.POST.get('username')
            pasw = request.POST.get('password')
            user = authenticate(username=name, password=pasw)
            
            return user_certificate(request, user)"""
        if(request.POST.get('Guest_sign_in', None) == 'guest'):
            name = 'guest'
            pasw = 'g1234pass'
            user = authenticate(username=name, password=pasw)

            return user_certificate(request, user)
        #signout
        if(request.POST.get('User_sign_out', None) == 'signout'):
            return user_signout(request)
            
    #the other
    return user_accept(request)

def user_certificate(request, user):
    if user:
        if user.is_active:
            #succeeded
            login(request,user)
            request.session['username'] = user.username
            return user_accept(request)
        else:
            #account blocked error
            redirect_url = reverse('signin:signin')
            parameters = urlencode({'e_code':'2'})
            return redirect(f'{redirect_url}?{parameters}')
    else:
        #no match error
        redirect_url = reverse('signin:signin')
        parameters = urlencode({'e_code':'1'})
        return redirect(f'{redirect_url}?{parameters}')

@login_required
def user_accept(request):
    url_name = request.session.get('username', 'nameless')
    redirect_url = reverse('user_index', kwargs={'slug':url_name})
    return redirect(redirect_url)

@login_required
def user_signout(request):
    logout(request)
    return redirect('signin:signin', permanent=True)

@csrf_exempt
@login_required
def user_index(request, **kwargs):
    context = {}
    context['username'] = request.session.get('username', 'nameless')
    return render(request, 'user_index.html', context)
    