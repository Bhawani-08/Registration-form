from django.shortcuts import render,redirect
from .form import RegistrationForm 
from django.http import HttpResponse
# Create your views here.

def fun1(request):
    return HttpResponse("this is the site")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.save())
            
            return redirect('registration_success/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def registration_success(request):
    return render(request, 'registration_success.html')       
