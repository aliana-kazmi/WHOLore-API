from django.urls import path
from .views import *

urlpatterns = [
    path('companions/<str:name>/', CompanionView ,name='companion'),
    path('alien-races/<str:name>/', AlienView ,name='alien-race'),
    path('villains/<str:name>/', VillainView ,name='villain'),
    path('doctors/<int:number>/', DoctorView, name='doctor'),
    path('companions/', CompanionView ,name='all-companions'),
    path('alien-races/', AlienView ,name='all-alien-races'),
    path('villains/', VillainView ,name='all-villains'),
    path('doctors/', DoctorView, name='all-doctors'),

    # re_path(r'companions/(?P<pk>[0-9]{1,4})/$',companion,name='view-companion'),
]