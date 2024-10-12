from django.urls import path
from .views import *

urlpatterns = [
    path("serials/<int:serial_no>", SerialView,name='serial'),
    path("episodes/<int:pk>", EpisodeView, name="episode"),      
    path("episodes/", EpisodeView, name="episodes"),   
    path("serials/", SerialView, name="serials"),      
]