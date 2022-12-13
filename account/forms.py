from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label="Ім'я*")
    last_name = forms.CharField( max_length=50,  label='Прізвище' )
    email = forms.EmailField( max_length=100, required=True, label='E-mail*' )
    password1 = forms.CharField( label='Пароль*', strip=False,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(label='Підтвердження пароля*', strip=False,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = { 'username': 'Номер телефону*' }

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Номер телефону: 0xx-xxx-xxxx',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50, required=True, label='Пароль*',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
        labels = { 'username': 'Номер телефону*' }