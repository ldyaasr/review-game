from django.contrib import admin
from .models import Biodata

class BiodataAdmin(admin.ModelAdmin):
    list_display = ('user','nama','telp','alamat')
    search_fields= ('user','nama')

admin.site.register(Biodata, BiodataAdmin)