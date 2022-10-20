from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from characters.models import *
from characters.serializers import *

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    data_here = {
        'Doctors':'',
        'Comapnions':'',
        'Writers':'',
        'Gadgets':'',
        'Serials':'',
        'Ally':'',

    }
    return Response(data_here)