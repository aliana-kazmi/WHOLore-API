from django.urls import path
from .views import *

urlpatterns = [
    path("serials/<str:title>", SerialView,name='serial'),
    path("episodes/<str:title>", EpisodeView, name="episode"),      
    path("episodes/", EpisodeView, name="episodes"),   
    path("serials/", SerialView, name="serials"),      
]