from django.contrib import admin
from .models import Gadget
# Register your models here.

class GadgetAdmin(admin.ModelAdmin):
    list_display = ['name','description','debue_date']

admin.site.register(Gadget,GadgetAdmin)