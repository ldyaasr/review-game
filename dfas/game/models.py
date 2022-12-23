from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    time = models.DateField()

    def __str__(self):
        return self.nama