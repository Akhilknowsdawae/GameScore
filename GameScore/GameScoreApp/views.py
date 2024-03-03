from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm


def mainPage(request):

    return render(request, 'index.html')

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/SignUp.html', { 'form': form})
