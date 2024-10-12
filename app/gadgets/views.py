from django.shortcuts import render
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

class GadgetMixinAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer
    lookup_field = 'name'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args,**kwargs):
        name = kwargs.get("name")
        if name is not None:
            return self.retrieve(request, *args, **kwargs)        
        return self.list(request, *args, **kwargs)


GadgetView = GadgetMixinAPIView.as_view()

# @api_view(['POST'])
# def add_gadget(request, *args, **kwargs): 
#     serialized_data = GadgetSerializer(data=request.data)
    
#     if serialized_data.is_valid():
#         instance = serialized_data.save()
#         print(instance)
#         return Response(serialized_data.data)
#     else:
#         return Response({'error':'Invalid data submitted'},status=400)


# class GadgetCreateAPIView(generics.CreateAPIView):
#     queryset = Gadget.objects.all()
#     serializer_class = GadgetSerializer
