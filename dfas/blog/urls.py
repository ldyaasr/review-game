from django.urls import path, include
from . views import *

urlpatterns = [
    path('', base, name='base'),  
    path('', TabelList, name='nlist'),
    path('add/', game_add, name='game_add'),
    path('update/<int:id>', game_update, name='game_update'),
    path('delete/<int:id>', game_delete, name='game_delete'),
    path('sinkron_game/', Sinkron_game, name='sinkron_game'),
    path('game/detil/<str:key>', game, name='game'),
]

