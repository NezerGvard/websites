from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

form = 'p-4 rounded transition ease-in-out m-0 block form-control px-3 py-1.5 text-lg hover:bg-white active:bg-white rounded-lg shadow-2xl w-full h-10 border-2 border-gray-500 bg-gray-100 mt-4'

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': form, 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': form, 'placeholder':'Пароль'}))


class UserRegister(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': form, 'placeholder': 'Имя пользователя'}), max_length=150)
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': form, 'placeholder': 'Email'}), max_length=150)
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': form, 'placeholder':'Пароль'}), max_length=150)
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': form, 'placeholder':'Пароль'}), max_length=150)
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')