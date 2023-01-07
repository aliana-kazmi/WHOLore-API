from rest_framework import serializers
from api.serializers import *
from .models import *

class CompanionSerializer(serializers.ModelSerializer):

    class Meta:
        actor = ActorSerializer(read_only=True, many=True)
        episode = EpisodeSerializer(read_only=True, many=True)
        model = Companion
        fields = '__all__'

class AlienSerializer(serializers.ModelSerializer):

    class Meta:
        featured_in = EpisodeSerializer(read_only=True, many=True)
        model = AlienRace
        fields = '__all__'

class VillainSerializer(serializers.ModelSerializer):
    class Meta:
        played_by = ActorSerializer(read_only=True,many=True)
        featured_in = EpisodeSerializer(read_only=True, many=True)
        race = AlienSerializer(read_only=True, many=True)

        model = Villain
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        companions = CompanionSerializer(read_only=True,many=True)
        played_by = ActorSerializer(read_only=True,many=True)
        featured_in = EpisodeSerializer(read_only=True, many=True)
        race = AlienSerializer(read_only=True, many=True)

        model = Doctor
        fields = '__all__'

