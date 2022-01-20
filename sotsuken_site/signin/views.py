from django.shortcuts import render

# Create your views here.
def signin(request):
    e_message=''
    
    if 'e_code' in request.GET:
        e_code = request.GET['e_code']

        if e_code == '1':
            #no match
            e_message = 'Username and Password do not match.'
        elif e_code == '2':
            #account blocked
            e_message = 'This account is blocked.'
            
    return render(request, 'signin.html', {'error' : e_message})
