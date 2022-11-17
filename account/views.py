from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def logon(request):
    if request.method == "GET":
        return render(request, 'account/logon.html', {
            'page_title': 'Реєстрація',
            'page': 4
        })
    elif request.method == 'POST':
        # ...
        return render(request, 'account/reg_res.html', {})


def confirm(request):
    return render(request, 'account/confirm.html', {})


def login(request):
    return render(request, 'account/login.html', {
        'page_title': 'Вхід',
        'page': 4
    })


def exit(request):
    return render(request, 'account/exit.html', {})


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
