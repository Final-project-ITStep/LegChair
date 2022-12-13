from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.http import JsonResponse
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.contrib import messages
"""
from .forms import SignUpForm, LoginForm
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
"""

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
        next = request.POST.get('next')
        mail = request.POST.get('email')
        new_user = User.objects.create_user(username=request.POST.get('username'),
                                            password=request.POST.get('password1'),
                                            email=mail,
                                            first_name=request.POST.get('first_name'),
                                            last_name=request.POST.get('last_name'))
        if new_user is None:
            messages.info(request, f'Вам відмолено у реєстрації!')
        else:
            url = f'http://127.0.0.1:8000/account/confirm?email={mail}'
            subject = 'Підтвердження реєстрації на сайті LegChair'
            body = f"""
                <hr/>
                <h3>Для підтвердження реєстрації перейдіть за посиланням:</h3>
                <div>
                    <a href="{url}">{url}</a>
                </div>
                <hr/>
                <p>З повгою, <br/>адміністрація сайту <a href="www.legchair.ua">www.legchair.ua</a></p> """
            if not send_mail(subject, '', 'Site Univer', [mail], fail_silently=False, html_message=body):
                messages.info(request, f'Ваша пошта не дійсна!')
            else:
                messages.success(request, f'Вітаємо з успішною реєстрацією!\nНа вказаний Вами при реєстрації Email: {mail}<br>відправлено повідомлення для його підтвердження')
                new_user.is_active = True
                login(request, new_user)
                return redirect(next)
    return render(request, 'account/signup.html', {'page_title': 'Реєстрація', 'page': 4 })
    """
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
        'page': 4
    })
"""


def confirm(request):
    return render(request, 'account/confirm.html', {})

def signin(request):
    if request.method == 'POST':
        check_user = authenticate(
                username=request.POST.get('username'),
                password=request.POST.get('password')
            )
        if check_user is None:
            messages.info(request, f'Користувача із таким номером телефону не знайдено!')
        else:
            login(request, check_user)
            messages.success(request, f'Вітаємо Вас на нашому сайті!!!')
            return redirect('/')
    return render(request, 'account/signin.html', { 'page_title': 'Вхід', 'page': 4 })

"""
def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        if form.is_valid():
            form = LoginForm(request.POST or None)
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if not form.cleaned_data['remember_me']:
                request.session.set_expiry(0)
                request.session.modified = True
            if user is None:
                messages.info(request, f'Користувача із таким номером телефону не знайдено!')
            else:
                messages.success(request, f'Вітаємо Вас на нашому сайті!!!')
                login(request, user)
                return redirect('/')
        else:
            messages.info(request, f'Щось пішло не так!')
            print(form.errors.as_data())
    return render(request, 'account/signin.html', { 'page_title': 'Вхід', 'form': form, 'page': 4 })
"""

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
