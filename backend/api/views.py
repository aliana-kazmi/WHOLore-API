from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from characters.models import *
from characters.serializers import *
from rest_framework import generics

BASE_URL= 'http://127.0.0.1:8000/api/'

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    data_here = {
        'Doctors':'{}doctors/'.format(BASE_URL),
        'Companions':'{}companions/'.format(BASE_URL),
        'Villains':'{}villains/'.format(BASE_URL),
        'Alien Race':'{}alien-races/'.format(BASE_URL), 
        'Gadgets':'{}gadgets/'.format(BASE_URL),  
        'Serials':'{}serials/'.format(BASE_URL),
        'episodes':'{}episodes/'.format(BASE_URL)
    }
    return Response(data_here)

class AllSerialsAPIView(generics.ListAPIView):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer

class AllEpisodesAPIView(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

