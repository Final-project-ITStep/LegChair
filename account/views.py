from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def signup(request):
    if request.method == "GET":
        return render(request, 'account/signup.html', {
            'page_title': 'Реєстрація',
            'page': 4
        })
    elif request.method == 'POST':
        # ...
        return render(request, 'account/reg_res.html', {})


def confirm(request):
    return render(request, 'account/confirm.html', {})


def signin(request):
    return render(request, 'account/signin.html', {
        'page_title': 'Вхід',
        'page': 4
    })


def exit(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'account/profile.html', {
        'page_title': 'Профайл',
        'page': 4
    })


def reset(request):
    return render(request, 'account/reset.html', {
        'page_title': 'Зкидання пароля',
        'page': 4
    })
