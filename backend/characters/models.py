from pydoc import synopsis
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Writer(models.Model):
    name=models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Season(models.Model):
    season_no = models.SmallIntegerField(primary_key=True)
    start_yr = models.DateField()
    end_yr = models.DateField()

class Serial(models.Model):
    # order = models.IntegerField()
    title = models.CharField(max_length=85)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    serial_no = models.PositiveSmallIntegerField()
    story = models.TextField()

    def __str__(self):
        if self.season.season_no<11200:
            return "Season {} Serial {}: {}".format(self.season.season_no, self.serial_no, self.title)
        return "Season {} Series {}: {}".format(self.season.season_no-11200, self.serial_no, self.title)

class Episode(models.Model):
    EPISODE_CHOICES = (
        ("Special","Special"),
        ("Regular","Regular"),
    )
    title = models.CharField(max_length=80)
    episode_type = models.CharField(max_length=7,choices=EPISODE_CHOICES,default="Regular")
    original_air_date = models.DateField(null=True, blank=True)
    #writer = models.ManyToManyField(Writer)
    viewer_rating = models.DecimalField(validators=[
            MaxValueValidator(5.0),
            MinValueValidator(0.0)
        ],max_digits=2, decimal_places=1)
    serial = models.ForeignKey(Serial, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=70)
    gender = models.CharField(max_length=6,default="male")

    def __str__(self):
        return self.name

class AlienRace(models.Model):
    name = models.CharField(max_length=70)
    featured_in = models.ManyToManyField(Serial)
    description = models.TextField()
    image=models.ImageField(blank=True, null=True,upload_to='images/Races')
    # played_by = models.ManyToManyField(Actor)
  
    class Meta:
        verbose_name_plural = 'Alien Races'
        
    def __str__(self):
        return self.name

class Companion(models.Model):
    name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=65, null=True, blank=True)
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
        ones_digit = self.number % 10
        str = ""
        if ones_digit == 1 and self.number%100 !=11:
            str="st"
        elif ones_digit == 2 and self.number%100 !=12:
            str="nd"
        elif ones_digit == 3 and self.number%100 !=13:
            str="rd"
        else:
            str="th"
        return "{}{} Doctor".format(self.number,str)
