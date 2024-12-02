from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


# Из задания task4
def platform(request):
    return render(request, 'platform.html')


def games_store(request):
    games = Games.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'games.html', context)


def cart_of_store(request):
    return render(request, 'cart.html')


# Из задания task5
def sign_up_by_django(request):
    buyers = Buyer.objects.all()
    users = [i.name for i in buyers]
    info = {}
    form = UserRegister()
    context = {
        'info': info,
        'form': form,
        'users': users,
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f"Приветствуем, {username}!")
            if password != repeat_password:
                info.update({'error1': 'Пароли не совпадают'})
            if int(age) < 18:
                info.update({'error2': 'Вы должны быть старше 18'})
            if username in users:
                info.update({'error3': 'Пользователь уже существует'})
        else:
            form = UserRegister()
    return render(request, 'registration_page.html', context)