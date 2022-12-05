from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.http import JsonResponse
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail

from .forms import SignUpForm
from .tokens import account_activation_token


def activation_sent(request):
    return render(request, 'activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'activation_invalid.html')


def checkinput(request):
    if request.method == 'GET':
        input_val = request.GET.get('input_val', None)
        if request.GET.get('whattocheck', None) == 'email':
            valid = User.objects.filter(email=input_val).exists()
        else:
            valid = User.objects.filter(username=input_val).exists()
        return JsonResponse({'valid': valid}, status = 200)
    return JsonResponse({}, status = 400)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('f_name')
            user.profile.last_name = form.cleaned_data.get('l_name')
            user.profile.email = form.cleaned_data.get('email')
            user.is_active = False
            user.save()
            subject = 'Підтвердження реєстрації на сайті LegChair'
            body = render_to_string('activation_request.html', {
                'user': user,
                'domain': get_current_site(request),
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            report = dict()
            success = send_mail(subject, '', 'Site LegChair', [user.profile.email], fail_silently=False, html_message=body)
            if not success:
                report['info'] = 'Ваша пошта недійсна!'
            else:
                report['msg'] ='Ви успішно зареєстровані!'
                report['info'] = f'На вказаний Вами при реєстрації Email: {user.profile.email}\n відправлено повідомлення для його підтвердження'
            return render(request, '/account/activation_sent.html', report)
        else:
            print(form.errors)
    return render(request, 'account/signup.html', {
        'page_title': 'Реєстрація',
        'form': SignUpForm(),
        'page': 4
    })


def confirm(request):
    return render(request, 'account/confirm.html', {})


def signin(request):
    if request.method == 'POST':
        _login = request.POST.get('name')
        _pass = request.POST.get('password')
        user = authenticate(request, username=_login, password=_pass)
        if user is None:
            msg ='Користувач на знайдений!'
        else:
            msg ='Ви успішно авторизовані!'
            login(request, user)
        return redirect('/')
    
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
