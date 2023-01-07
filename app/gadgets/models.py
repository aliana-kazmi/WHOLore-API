from django.db import models

# Create your models here.

class Gadget(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)
    debue_date = models.DateField()


