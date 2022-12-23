from django.shortcuts import render, redirect
from blog.models import *
from ng.models import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse
import requests
# Create your views here.
login_required
def base(request):
    list_game = New.objects.all()
    template_name = "back/base.html"
    context = {
        'title': 'dashboard',
        'nlist':list_game
    }
    return render(request, template_name, context)

def TabelList(request):
    template_name = "back/nlist.html"
    context = {
        'title': 'nlist',
        
    }
    return render(request, template_name, context)

def game_add(request):
    genre = Genre.objects.all()
    template_name = "back/game_add.html"
    if request.method == "POST":
        input_genre = request.POST.get('genre')
        input_nama = request.POST.get('nama')
        input_rilis = request.POST.get('rilis')
        input_pengembang = request.POST.get('pengembang')
        input_platfrom = request.POST.get('platform')

        get_genre = Genre.objects.get(nama=input_genre)
        New.objects.create(
            nama = input_nama,
            rilis = input_rilis,
            pengembang = input_pengembang,
            platform = input_platfrom,
            genre = get_genre,
        )
        return redirect(base)

        print(input_genre, input_nama, input_rilis, input_pengembang, input_platfrom)
    context = {
        'title': 'game add',
        'genre':genre

    }
    return render(request, template_name, context)

def game_update(request, id):
    genre = Genre.objects.all()
    get_new = New.objects.get(id=id)
    template_name = "back/game_add.html"
    if request.method == "POST":
        input_genre = request.POST.get('genre')
        input_nama = request.POST.get('nama')
        input_rilis = request.POST.get('rilis')
        input_pengembang = request.POST.get('pengembang')
        input_platfrom = request.POST.get('platform')

        get_genre = Genre.objects.get(nama=input_genre)
        get_new.nama = input_nama
        get_new.rilis = input_rilis
        get_new.pengembang = input_pengembang
        get_new.platform = input_platfrom
        get_new.genre = get_genre
        get_new.save()
        return redirect(base)
    context = {
        'title': 'game add',
        'genre':genre,
        'get_new':get_new,

    }
    return render(request, template_name, context)

def game_delete(request, id):
    New.objects.get(id=id).delete()
    return redirect(base)

def Sinkron_game(request):    
    r = requests.get("https://the-lazy-media-api.vercel.app/api/games/review")        
    data = r.json()        
    
    for d in data:
        cek_game = Game.objects.filter(key=d['key'])
        if cek_game.exists():
            game = cek_game.first()
            game.title = d['title']
            game.author = d['author']
            game.time = d['time']
            game.desc = d['desc']
            game.key = d['key']         
            game.save()
        else:
            Game.objects.create(
                title = d['title'],
                author = d['author'],
                time = d['time'],
                desc = d['desc'],
                key = d['key'],
            )
    ambil_game = Game.objects.all()
    for i in ambil_game:
        r = requests.get(f"https://the-lazy-media-api.vercel.app/api/detail/{i.key}")
        data = r.json()['results']
        i.content = data['content']
        i.save()
    return redirect(base)

def game(request):
    template_name = "front/game.html"
    list_game = Game.object.all()
    context = {
        'title' : 'ini halaman game news',
        'game' : list_game,
    }
    return render(request, template_name, context)