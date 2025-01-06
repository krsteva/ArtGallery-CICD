from django.db import models

# Create your models here.
from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Painting(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    medium = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='paintings')

    def __str__(self):
        return self.title
