from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from user.forms import SignUpForm, SignInForm


# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    ctx = {
        'form': form
    }

    return render(request, 'user/sign-up.html', ctx)


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = SignInForm(request.POST)
        print(1)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')

    form = SignInForm()

    ctx = {
        'form': form
    }

    return render(request, 'user/sign-in.html', ctx)


def Logout(request):
    logout(request)
    return redirect('index')
