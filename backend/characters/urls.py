from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('companions/', AllCompanionsAPIView.as_view() ,name='all-companions'),
    path('alien-Races/', AllAlienRacesAPIView.as_view() ,name='all-alien-races'),
    path('villains/', AllVillainsAPIView.as_view() ,name='all-villains'),
    path('doctors/',DoctorAPIView.as_view(),name='all-doctors'),
    # path('<>',companion,name='all-companions'),
    re_path(r'(?P<pk>[0-9]{1,4})/$',companion,name='view-companion'),
]