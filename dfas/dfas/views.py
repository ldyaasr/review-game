from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.template import RequestContext
from ng.models import *
from blog.models import *
import requests

def home(request):
    template_name = 'front/home.html'
    context = {
        'title': 'ini adalah halaman home'
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'front/about.html'
    context = {
        'title': 'ini adalah halaman about'
    }
    return render(request, template_name, context)
    
def game(request):
    list_data = Game.objects.all()
    template_name = 'front/game.html'
    context = {
        'title': 'ini adalah halaman news game ',
        'game': list_data
    }
    return render(request, template_name, context)
    
def Detail_berita(request, id):       

    ambil_content = Game.objects.get(id=id)
    template_name = 'front/detail_berita.html'
    context = {
        'title': 'ini adalah halaman detail game',
        'list_data': ambil_content
    }
    return render(request, template_name, context)
    
def login(request):
    if request.user.is_authenticated:
        print('sudah login')
        redirect('base')
        
    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('username benar')
            auth_login(request, user)
            return redirect('base')
        else:
            print('username salah')
       
    context = {
        'title': 'ini adalah halaman login'
    }
    return render(request, template_name, context)

def ngame(request):
    template_name = "front/ngame.html"
    ng = New.objects.all()
    context = {
        'title': 'ngame',
        'nlist':ng
    }
    return render(request, template_name, context)

def logout_views(request):
    logout(request)
    return redirect('home')

