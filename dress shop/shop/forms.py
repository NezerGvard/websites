from itertools import count
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

form = 'form_a'

class InputForm(forms.Form):
    count = forms.IntegerField()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': form, 'placeholder': 'Логин'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': form, 'placeholder':'Пароль'}))


class UserRegister(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': form, 'placeholder': 'Логин'}), max_length=150)
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': form, 'placeholder': 'Почта'}), max_length=150)
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': form, 'placeholder':'Пароль'}), max_length=150)
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': form, 'placeholder':'Подтвердить'}), max_length=150)
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')