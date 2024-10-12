from rest_framework import serializers
from .models import *

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ('name'),

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('season_no','start_yr','end_yr',)

class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        season = SeasonSerializer(read_only=True, many=True)
        fields = ('title', 'season','serial_no','story')

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'
