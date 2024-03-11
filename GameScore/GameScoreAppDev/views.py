from django.shortcuts import render
from .forms import LoginForm


def mainPage(request):

    return render(request, 'index.html')


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
