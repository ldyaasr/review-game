from django.contrib import admin
from blog.models import *
# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'time', 'desc', 'key']
admin.site.register(Game, GameAdmin)