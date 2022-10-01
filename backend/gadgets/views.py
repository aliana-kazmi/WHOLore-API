from django.shortcuts import render
from django.db import models
# Create your views here.

class Episode(models.Model):
    name = models.CharField(max_length=35)
    date_aired = models.DateField()
    season = models.PositiveSmallIntegerField()
    episode = models.PositiveSmallIntegerField()
    

class Gadget(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)
    debue_date = models.DateField()


