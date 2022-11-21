from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from characters.models import *
from characters.serializers import *
from rest_framework import generics, mixins, authentication, permissions

BASE_URL= 'http://127.0.0.1:8000/api/'

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    data_here = {
        'Doctors':'{}characters/doctors/'.format(BASE_URL),
        'Companions':'{}characters/companions/'.format(BASE_URL),
        'Villains':'{}characters/villains/'.format(BASE_URL),
        'Alien Race':'{}characters/alien-races/'.format(BASE_URL), 
        'Gadgets':'{}gadgets/'.format(BASE_URL),  
        'Serials':'{}serials/'.format(BASE_URL),
        'episodes':'{}episodes/'.format(BASE_URL)
    }
    return Response(data_here)

class SerialMixinAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Serial.objects.all()
    serializer_class = SerialSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args,**kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)        
        return self.list(request, *args, **kwargs)

SerialView = SerialMixinAPIView.as_view()


class EpisodeMixinAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args,**kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)        
        return self.list(request, *args, **kwargs)


EpisodeView = EpisodeMixinAPIView.as_view()