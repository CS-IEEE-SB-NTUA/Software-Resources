from django.db import models

# Create your models here.



class Society(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, primary_key=True)
    info = models.TextField(max_length=10000)

    def __str__(self):
        return self.name



class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, primary_key=True)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    info = models.TextField(max_length=10000)
    date = models.DateField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.title
