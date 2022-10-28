from rest_framework import serializers
from api.serializers import *
from .models import *

class CompanionSerializer(serializers.ModelSerializer):

    class Meta:
        actor = ActorSerializer(read_only=True, many=True)
        episode = EpisodeSerializer(read_only=True, many=True)
        model = Companion
        fields = '__all__'


