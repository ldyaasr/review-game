from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sinkron_game(request):
    URL = "https://the-lazy-media-api.vercel.app/api/games?page=1"
    
    r = request.get(url = URL)        
    data = r.json()        
    
    for d in data["results"]:
        print(d['key'])
        cek_game = Game.objects.filter(key=d['key'])
        if cek_game.exists():
            game = cek_game.first()
            game.title = d['title']
            game.thumb = d['thumb']
            game.author = d['author']
            game.tag = d['tag']
            game.time = d['time']
            game.desc = d['desc']
            game.key = d['key']         
            game.save()
        else:
            Game.objects.create(
                title = d['title'],
                thumb = d['thumb'],
                author = d['author'],
                tag = d['tag'],
                time = d['time'],
                desc = d['desc'],
                key = d['key'],
            )
    ambil_game = Game.objects.all()
   
    for ambil in ambil_game:
        url_detil_game = "https://the-lazy-media-api.vercel.app/api/detail/2021/01/28/balan-wonderworld-preview{}".format(ambil.key)
        print(url_detil_game)
        r = request.get(url_detil_game,ambil.key)     
        data = r.json()['results']        
        ambil.desc = data['desc']
        ambil.ingredient = data['ingredient']
        ambil.save()
    return HttpResponse("<h1>berhasil sinkron</h1>")

def game(request):
    template_name = "front/game.html"
    game = game.object.all()
    context = {
        'title' : 'ini halaman game news',
        'game' : game,
    }
    return render(request, template_name, context)