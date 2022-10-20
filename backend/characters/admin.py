from django.contrib import admin
from .models import *

class companionAmin(admin.ModelAdmin):
    list_display = ["name","nickname","image"]

admin.site.register(Companion, companionAmin)
