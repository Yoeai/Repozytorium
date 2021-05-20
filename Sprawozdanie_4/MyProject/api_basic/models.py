from django.db import models

# Create your models here.

class Game(models.Model):
    tytul = models.CharField(max_length=100)
    wydawca = models.CharField(max_length=100)
    gatunek = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.tytul