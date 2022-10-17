from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from characters.serializers import SerialSerializer
from .serializers import *

@api_view(['POST'])
def add_gadget(request, *args, **kwargs): 
    serialized_data = GadgetSerializer(data=request.data)
    
    if serialized_data.is_valid():
        instance = serialized_data.save()
        print(instance)
        return Response(serialized_data.data)
    else:
        return Response({'error':'Invalid data submitted'},status=400)
