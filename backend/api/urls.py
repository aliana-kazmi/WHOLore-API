from django.urls import re_path,path,include
from .views import *

urlpatterns = [
    path("", api_home, name="api-home"),
    path("characters/",include('characters.urls')),
    path("gadgets/",include('gadgets.urls')),
    path("serials/",AllSerialsAPIView.as_view(),name="all-serials"),
    path("episodes/",AllEpisodesAPIView.as_view(),name="all-eipsodes"),
]