from django.contrib import admin
from .models import *

class CompanionAdmin(admin.ModelAdmin):
    list_display = ["name","nickname","image"]

class VillainAdmin(admin.ModelAdmin):
    list_display = ["name","nickname","image","description"]

class DoctorAdmin(admin.ModelAdmin):
    list_display = ["number","fav_clothing","image"]

class AlienRaceAdmin(admin.ModelAdmin):
    list_display = ["name","image","description"]

admin.site.register(Companion, CompanionAdmin)
admin.site.register(Villain, VillainAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(AlienRace, AlienRaceAdmin)