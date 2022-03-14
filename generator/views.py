from django.shortcuts import render
from django.http import HttpResponse
# это библиотеки для написания более универсального пути к файлу
import pathlib
from pathlib import Path
# для генерации случайных чисел
import random 

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):
    
    characters=list('abcdefghijklmnopqrstuvwxyz')   # для нихнего регистра
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))   # если установлена птичка верхнего регистра
        
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))   # если установлена птичка спецсимволов  
        
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))   # если установлена птичка цифры 
                     
    length=int(request.GET.get('length', 12)) # длина выбранного пароля
    
    thepassword= ''     # перенесем и пока оставим пустым

    for x in range (length):
        thepassword+= random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    theabout= ''
    return render(request,'generator/about.html', {'about':theabout})
    