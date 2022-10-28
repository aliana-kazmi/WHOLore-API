from django.db import models
from api.models import Writer, Season, Serial, Actor

class AlienRace(models.Model):
    name = models.CharField(max_length=70)
    featured_in = models.ManyToManyField(Serial)
    description = models.TextField()
    image=models.ImageField(blank=True, null=True,upload_to='images/Races')
     
    class Meta:
        verbose_name_plural = 'Alien Races'
        
    def __str__(self):
        return self.name


class Companion(models.Model):
    name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/Companions')
    played_by = models.ManyToManyField(Actor)
    featured_in = models.ManyToManyField(Serial, blank=True)
    race = models.ManyToManyField(AlienRace)

    def __str__(self):
        return self.name


class Villain(models.Model):
    name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=65, null=True, blank=True)
    image = models.ImageField(upload_to='images/Companions')
    played_by = models.ManyToManyField(Actor)
    featured_in = models.ManyToManyField(Serial, blank=True)
    description = models.TextField(blank=True)
    race = models.ManyToManyField(AlienRace)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    number = models.CharField(primary_key=True,max_length=10)
    fav_clothing = models.TextField()
    companions = models.ManyToManyField(Companion)
    image = models.ImageField(upload_to='images/Doctor')
    played_by = models.ManyToManyField(Actor)
    featured_in = models.ManyToManyField(Season)

    def __str__(self):
        if self.number.isnumeric():
            ones_digit = int(self.number) % 10
            two_digits = int(self.number) % 100
            str = ""
            if ones_digit == 1 and  two_digits != 11:
                str="st"
            elif ones_digit == 2 and two_digits != 12:
                str="nd"
            elif ones_digit == 3 and two_digits != 13:
                str="rd"
            else:
                str="th"
            return "{}{} Doctor".format(self.number,str)
        else:
            return "{} Doctor".format(self.number)