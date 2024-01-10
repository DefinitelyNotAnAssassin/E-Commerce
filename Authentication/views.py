from django.shortcuts import render, redirect, HttpResponse
from Models.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from Authentication.forms import UserForm, LoginForm
# Create your views here.


def register_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('index')
        
        form = UserForm()
        items = {
            'form': form
        }
        return render(request, 'Authentication/register.html', context = items)
    
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False) 
            user.set_password(user.password)
            user.save()
            return redirect('index')
        else: 
            return render (request, 'Authentication/register.html', {'form': form})

def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        items = {
            'form': form
        }
        return render(request, 'Authentication/login.html', context = items)
    elif request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')
        
def logout_view(request):
    logout(request)
    return redirect('login')
