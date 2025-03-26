from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def Iniciar(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print(email)
            login(request, user)
            return redirect('main')
        else:
            return redirect('login')  
    return render(request, 'index.html')

def salir(request):
    logout(request)
    return redirect('main')