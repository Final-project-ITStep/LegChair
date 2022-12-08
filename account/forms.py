from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50, 
        label="Ім'я*"
    )
    last_name = forms.CharField(
        max_length=50, 
        label='Прізвище'
    )
    email = forms.EmailField(
        max_length=100, 
        required=True, 
        label='E-mail*'
    )
    password1 = forms.CharField(
        label='Пароль*',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label='Підтвердження пароля*',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = { 'username': 'Номер телефону*' }