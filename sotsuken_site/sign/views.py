from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from urllib.parse import urlencode
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def sign(request):
     
    if 'e_code' in request.GET:
        e_code = request.GET.get['e_code']
        e_message=''

        if e_code == '1':
            #no match
            e_message = 'Username and Password don\'t match.'
        elif e_code == '2':
            #account blocked
            e_message = 'This account is blocked.'
        elif e_code == '3':
            ##could not send
            e_message = 'This request couldn\'t send properly. Please try agein.'
        
        return render(request, 'sign.html', {'error' : e_message})      
      
    return render(request, 'sign.html')


@csrf_exempt
def signin(request):
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

            return signin_certificate(request, user)
    
    #failed
    return signin_failed()


def signin_certificate(request, user):
    if user:
        if user.is_active:
            #succeeded
            login(request,user)
            request.session['username'] = user.username
            return signin_success(request)
        else:
            #account blocked error
            redirect_url = reverse('sign:sign')
            parameters = urlencode({'e_code':'2'})
            return redirect(f'{redirect_url}?{parameters}', permanent=True)
    else:
        #no match error
        redirect_url = reverse('sign:sign')
        parameters = urlencode({'e_code':'1'})
        return redirect(f'{redirect_url}?{parameters}', permanent=True)
  
    
def signin_failed():
        #could not send error
        redirect_url = reverse('sign:sign')
        parameters = urlencode({'e_code':'3'})
        return redirect(f'{redirect_url}?{parameters}', permanent=True)


def signin_success(request):
     url_name = request.session.get('username', None)
     if url_name:
         redirect_url = reverse('user:user', kwargs={'username':url_name})
         return redirect(redirect_url)
     return signin_failed()

@csrf_exempt
def signout(request):
    logout(request)
    return redirect('sign:sign', permanent=True)
