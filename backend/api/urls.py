from django.urls import re_path,path,include
from .views import *

urlpatterns = [
    path("", api_home, name="api-home"),
    path("characters/",include('characters.urls')),
    path("gadgets/",include('gadgets.urls')),
    path("serials/<int:pk>",SerialDetailAPIView.as_view(),name='serialI'),
    path("serials/<int:season_no>/<int:serial_no>/",SerialDetailAPIView.as_view(),name="one-serial"),
    path("serials/",AllSerialsAPIView.as_view(),name="all-serials"),
    # path("episodes/<int:season_no>/<int:season_no>/<int:serial_no>/<int:episode_no>",AllEpisodesAPIView.as_view(),name="episodeI"),
    # path("episodes/<int:season_no>/<int:episode_no>",AllEpisodesAPIView.as_view(),name="episodeII"),
    path("episodes/",AllEpisodesAPIView.as_view(),name="all-episodes"),
]