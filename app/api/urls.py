from django.urls import re_path,path,include
from .views import *

urlpatterns = [
    path("", api_home, name="api-home"),
    path("serials/<int:pk>", SerialView,name='serial'),
    path("episodes/<int:pk>", EpisodeView, name="episode"),      
    path("episodes/", EpisodeView, name="episodes"),   
    path("serials/", SerialView, name="serials"),      
    path("characters/",include('characters.urls')),
    path("gadgets/",include('gadgets.urls')),
    # path("serials/<int:season_no>/<int:serial_no>/",SerialDetailAPIView.as_view(),name="one-serial"),
    # path("episodes/<int:season_no>/<int:season_no>/<int:serial_no>/<int:episode_no>",AllEpisodesAPIView.as_view(),name="episodeI"),
    # path("episodes/<int:season_no>/<int:episode_no>",AllEpisodesAPIView.as_view(),name="episodeII"),

]