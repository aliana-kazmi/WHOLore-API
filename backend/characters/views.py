from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Fix this func so that it can show all companions in json
@api_view(['GET'])
def all_companions(request, *args, **kwargs):
    query = Companion.objects.all().first()
    if query:
        companion = CompanionSerializer(query)
    
    else:
        print('data empty')
    return Response(companion.data)

@api_view(['GET'])
def companion(request, url_parameters):
    companion = Companion.objects.all().order_by("?").first()
    data_here = {}
    if companion:
        data_here = CompanionSerializer(companion).data
        data_here['image'] = data_here['image'][1:].replace('src%3D%22','').replace('%3A/','://www.')

        print(data_here['image'])
        
    else:
        print('companion empty')
    return Response(data_here)