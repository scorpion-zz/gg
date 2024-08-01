from django import forms
from django.contrib.auth.models import User

from main.models import Car


class AddCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'



class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    password2 = forms.CharField(label='Повтор пароля',widget=forms.PasswordInput())
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    # 1 sposob reg pol
    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError('Пароли не совподают')
        else:
            return cd.get('password2')

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

class NewLoginForm(forms.Form):
    username = forms.CharField(label='Новый логин')


class NewPasswordForm(forms.Form):
    password = forms.CharField(label='Новый пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор нового пароля', widget=forms.PasswordInput())

