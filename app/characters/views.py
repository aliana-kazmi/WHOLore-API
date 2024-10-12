from django.shortcuts import render,get_object_or_404
from rest_framework import generics, mixins,authentication, permissions
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CompanionMixinAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Companion.objects.all()
    serializer_class = CompanionSerializer
    lookup_field = 'name'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args,**kwargs):
        name = kwargs.get("name")
        if name is not None:
            return self.retrieve(request, *args, **kwargs)        
        return self.list(request, *args, **kwargs)


CompanionView = CompanionMixinAPIView.as_view()


class AlienMixinAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = AlienRace.objects.all()
    serializer_class = AlienSerializer
    lookup_field = 'name'

    def get(self, request, *args,**kwargs):
        name = kwargs.get("name")
        if name is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

AlienView = AlienMixinAPIView.as_view()


class VillainMixinAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Villain.objects.all()
    serializer_class = VillainSerializer
    lookup_field = 'name'

    def get(self, request, *args,**kwargs):
        name = kwargs.get("name")
        if name is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

VillainView = VillainMixinAPIView.as_view()


class DoctorMixinAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'number'

    def get(self, request, *args,**kwargs):
        number = kwargs.get("number")
        if number is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

DoctorView = DoctorMixinAPIView.as_view()


# @api_view(['GET'])
# def companion(request, pk=None):
#     # print('here')
#     data_here = {}
#     if pk is not None:
#         # print('here')
#         companion = get_object_or_404(Companion, pk=pk)
#         serialized_companion = CompanionSerializer(companion)
#         return Response(serialized_companion.data)
#     else:
#         print('companion empty')
#     return Response(data_here)

    #TODO: add web scraper to views so that it keeps updating the database