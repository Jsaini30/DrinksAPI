from unicodedata import name
from django.db import models
from django.db.models import Model


class Drink(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name + " " + self.desc

class Writer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name 


class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='Books_Written')
    totalpages = models.IntegerField()
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title
