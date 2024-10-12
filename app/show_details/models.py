from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Writer(models.Model):
    name=models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'characters_writer'

class Season(models.Model):
    season_no = models.SmallIntegerField(primary_key=True)
    start_yr = models.DateField()
    end_yr = models.DateField()

    class Meta:
        db_table = 'characters_season'


class Serial(models.Model):
    # order = models.IntegerField()
    title = models.CharField(max_length=85)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    serial_no = models.PositiveSmallIntegerField()
    story = models.TextField()

    class Meta:
        db_table = 'characters_serial'

    def __str__(self):
        if self.season.season_no<11200:
            return "Season {} Serial {}: {}".format(self.pk,self.season.season_no, self.serial_no, self.title)
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

    class Meta:
        db_table = 'characters_episode'

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=70)
    gender = models.CharField(max_length=6,default="male")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'characters_actor'
