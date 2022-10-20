from django.shortcuts import render
from rest_framework import status
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
def companion(request, pk):
    print('here')
# def companion(request):
    try:
        print('here')
        companion = Companion.objects.get(pk=pk)
        serialized_companion = CompanionSerializer(companion)
        serialized_companion['image'] = serialized_companion['image'][1:].replace('src%3D%22','').replace('%3A/','://www.')
        return Response(serialized_companion.data)
    
    except Companion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # data_here = {}
    # if companion:
    #     data_here = CompanionSerializer(companion).data
        

        
        
    else:
        print('companion empty')
    return Response(data_here)