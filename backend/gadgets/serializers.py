from rest_framework import serializers
from .models import *

class GadgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gadget
        fields = ['name','description','debue_date']
        