from django.urls import re_path,path,include
from .views import *

urlpatterns = [
    path("", api_home, name="api-home"),
    path("show-details/",include('show_details.urls')),
    path("characters/",include('characters.urls')),
    path("gadgets/",include('gadgets.urls')),
    # path("serials/<int:season_no>/<int:serial_no>/",SerialDetailAPIView.as_view(),name="one-serial"),
    # path("episodes/<int:season_no>/<int:season_no>/<int:serial_no>/<int:episode_no>",AllEpisodesAPIView.as_view(),name="episodeI"),
    # path("episodes/<int:season_no>/<int:episode_no>",AllEpisodesAPIView.as_view(),name="episodeII"),

]