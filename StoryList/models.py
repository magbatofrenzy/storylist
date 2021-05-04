from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    ngender = models.TextField(default='')
    nname = models.TextField(default='')
    nCategory = models.TextField(default='')
    nTitle = models.TextField(default='')
    nAuthor = models.TextField(default='')
    nSynopsis = models.TextField(default='') 
    list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)











# Create your models here.



