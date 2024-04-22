"""
Definition of views.
"""

from datetime import datetime
from os import name
from django.shortcuts import render
from django.http import HttpRequest
from .forms import PollForm 
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Домашняя страница',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Ваша страница для контактов.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Ваше описание приложения.',
            'year':datetime.now().year,
        }
    )

def links (request):
    """Renders the links page."""
    return render(
        request,
        'app/links.html',
        {
            'title':'Ссылки',
            'message':'Ваша страница для ссылок.',
            'year':datetime.now().year,
        }
    )

def poll(request):
    assert isinstance(request, HttpRequest)
    data = None
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            form = None
    else:
        form = PollForm()
    return render(
        request,
        'app/poll.html',
        {
            'form':form,
            'data':data
        }
    )

def registration(request):
     assert isinstance(request, HttpRequest)
     if request.method == "POST": # после отправки формы
         regform = UserCreationForm (request.POST)
         if regform.is_valid(): #валидация полей формы
             reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
             reg_f.is_staff = False # запрещен вход в административный раздел
             reg_f.is_active = True # активный пользователь
             reg_f.is_superuser = False # не является суперпользователем
             reg_f.date_joined = datetime.now() # дата регистрации
             reg_f.last_login = datetime.now() # дата последней авторизации
             reg_f.save() # сохраняем изменения после добавления данных
             return redirect('home') # переадресация на главную страницу после регистрации
     else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
     
     assert isinstance(request,HttpRequest)
     return render(
        request,
        'app/registration.html',
         {
            'regform': regform, # передача формы в шаблон веб-страницы
            'year':datetime.now().year,
         }
     )
    
