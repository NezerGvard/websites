from django.shortcuts import redirect, render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import json

from .models import *
from .forms import *
from .fun import *


def index(request):
    product =  Product.objects.all()
    return render(request, 'prototype/main.html', {'product': product})


def get_product(request, product_id):
    product = Product.objects.filter(id=product_id)
    return render(request, 'prototype/product.html', {'products': product})


def user_logout(request):
    logout(request)
    return redirect('/prototype/login')

@csrf_exempt
def user_login(request):
    print(request.headers)
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно авторезировались')
            return redirect('/prototype')
        else:
            messages.error(request, 'Ошибка авторизации')
    else: 
        form = UserLoginForm()
    return render(request, 'prototype/login.html', {'form': form})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            print(request.POST)
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('/prototype')
        else:
            messages.error(request, 'Ошибка регистрации')
    else: 
        form = UserRegister()
    return render(request, 'prototype/register.html', {'form': form})


def register_telegram(request, username, password, email):
    form_user = UserLoginForm(data={'username':username, "password":password})
    print(form_user)
    if form_user.is_valid():
        user = form_user.get_user()
        login(request, user)
        messages.success(request, 'Вы успешно авторезировались')
        return redirect('/prototype')
    else:
        form_register = {'username': username, 'email': email, 'password1': password, 'password2': password}
        form = UserRegister(form_register)
        print(form_register)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('/prototype')
        else:
            return HttpResponse("<h1>Ошибка, неверные данные</h1>")