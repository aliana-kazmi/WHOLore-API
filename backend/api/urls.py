from django.urls import re_path,path,include
from .views import *

urlpatterns = [
    path("", api_home, name="api-home"),
    path("serials/<int:pk>", SerialView,name='serialI'),
    path("episodes/<int:pk>", EpisodeView, name="all-episodes"),    
    path("episodes/", EpisodeView, name="all-episodes"),   
    path("serials/", SerialView, name="all-serials"),      
    path("characters/",include('characters.urls')),
    path("gadgets/",include('gadgets.urls')),
    # path("serials/<int:season_no>/<int:serial_no>/",SerialDetailAPIView.as_view(),name="one-serial"),
    # path("episodes/<int:season_no>/<int:season_no>/<int:serial_no>/<int:episode_no>",AllEpisodesAPIView.as_view(),name="episodeI"),
    # path("episodes/<int:season_no>/<int:episode_no>",AllEpisodesAPIView.as_view(),name="episodeII"),

]