from django.shortcuts import render
from rest_framework import generics, mixins, authentication, permissions
from .models import Serial, Episode
from .serializers import SeasonSerializer, SerialSerializer, EpisodeSerializer

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
    lookup_field = 'serial_no'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args,**kwargs):
        serial_no = kwargs.get("serial_no")
        if serial_no is not None:
            return self.retrieve(request, *args, **kwargs)        
        return self.list(request, *args, **kwargs)
    


EpisodeView = EpisodeMixinAPIView.as_view()