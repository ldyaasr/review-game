from django.db import models

# Create your models here.
class ngame(models.Model):
    nama = models.CharField(max_length=50, blank=True, null=True)
    rilis = models.DateField()
    pengembang = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Game(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    time = models.CharField(max_length=1000, null=True)
    desc = models.TextField(blank=True, null=True)
    key = models.TextField(null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title
