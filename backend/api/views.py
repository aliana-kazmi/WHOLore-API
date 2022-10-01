from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse

def api_home(request,*args,**kwargs):
    data = {}
    body = request.body #byte string of json data

    try: #body may not have json data
        data = json.loads(body) #str of json data has been converted into json 
    except:
        pass
    # code line below will not work
    # data['headers'] = request.headers #or request.META
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET) 
    data['content-type'] = request.content_type
    return JsonResponse({"message":"Testing, testing"})