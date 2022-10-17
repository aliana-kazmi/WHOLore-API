from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from characters.models import *
from characters.serializers import *

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    companion = Companion.objects.all().order_by("?").first()
    data_here = {}
    if companion:
        data_here = CompanionSerializer(companion).data
        data_here['image'] = data_here['image'][1:].replace('src%3D%22','').replace('%3A/','://www.')

        print(data_here['image'])
        
    else:
        print('companion empty')
    return Response(data_here)