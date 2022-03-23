from ast import Return
from urllib import request
#from django.http import HttpResponse
from django.shortcuts import render
import random

def welcome(request):
    return render(request, 'generator/welcome.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password =""
     
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('!@$%^&*'))
        
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
            
    
    for x in range(length):
        generated_password += random.choice (characters)
        
    
    return render(request, 'generator/password.html', {'password': generated_password})
    
