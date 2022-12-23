from django.db import models

# Kita akan membuat relasi antara tabel user bawaan yang kita buat
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Biodata(models.Model):
    #CASCADE berarti ketika User kita delete maka Biodatanya juka akan terhapus
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    telp = models.CharField(max_length=16, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)

def _str_(self):
    return "{}".format(self.nama)

#agar penulisan didashboard admin tidak ada penambahan s seperti biodatas
class Meta:
    verbose_name_plural ="Biodata"