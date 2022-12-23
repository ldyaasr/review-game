from django.db import models

# Create your models here.
class Genre(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class New(models.Model):
    nama = models.CharField(max_length=50)
    rilis = models.DateField()
    pengembang = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nama