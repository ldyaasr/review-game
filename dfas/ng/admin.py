from django.contrib import admin
from ng.models import *

# Register your models here.
admin.site.register(Genre)
class NewAdmin(admin.ModelAdmin):
    list_display = ['nama', 'rilis', 'pengembang', 'platform']
admin.site.register(New, NewAdmin)