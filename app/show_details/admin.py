from django.contrib import admin
from .models import *
# Register your models here.


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ["title","original_air_date","viewer_rating","serial"]

class SerialAdmin(admin.ModelAdmin):
    list_display = ["title","season","serial_no","story"]

class SeasonAdmin(admin.ModelAdmin):
    list_display = ["season_no","start_yr","end_yr"]

class ActorAdmin(admin.ModelAdmin):
    list_display = ['name','gender']

admin.site.register(Serial,SerialAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Actor, ActorAdmin)