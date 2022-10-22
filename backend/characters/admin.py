from django.contrib import admin
from .models import *

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ["title","original_air_date","viewer_rating","serial"]

class SerialAdmin(admin.ModelAdmin):
    list_display = ["title","season","serial_no","story"]

class SeasonAdmin(admin.ModelAdmin):
    list_display = ["season_no","start_yr","end_yr"]

class CompanionAdmin(admin.ModelAdmin):
    list_display = ["name","nickname","image"]

class VillainAdmin(admin.ModelAdmin):
    list_display = ["name","nickname","image","description"]

class DoctorAdmin(admin.ModelAdmin):
    list_display = ["number","fav_clothing","image"]

class AlienRaceAdmin(admin.ModelAdmin):
    list_display = ["name","image","description"]

class ActorAdmin(admin.ModelAdmin):
    list_display = ['name','gender']

admin.site.register(Serial,SerialAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Companion, CompanionAdmin)
admin.site.register(Villain, VillainAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(AlienRace, AlienRaceAdmin)
admin.site.register(Actor, ActorAdmin)