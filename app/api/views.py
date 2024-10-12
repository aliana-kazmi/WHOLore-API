from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from characters.models import *
from characters.serializers import *

import environ

env = environ.Env()
environ.Env.read_env()
WEBSITE_URL = env('WEBSITE_URL')

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    data_here = {
        'Doctors':'{}characters/doctors/'.format(WEBSITE_URL),
        'Companions':'{}characters/companions/'.format(WEBSITE_URL),
        'Villains':'{}characters/villains/'.format(WEBSITE_URL),
        'Alien Race':'{}characters/alien-races/'.format(WEBSITE_URL), 
        'Gadgets':'{}gadgets/'.format(WEBSITE_URL),  
        'Serials':'{}show-details/serials/'.format(WEBSITE_URL),
        'Episodes':'{}show-details/episodes/'.format(WEBSITE_URL)
    }
    return Response(data_here)