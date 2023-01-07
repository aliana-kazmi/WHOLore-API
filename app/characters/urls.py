from django.urls import path
from .views import *

urlpatterns = [
    path('companions/<int:pk>/', CompanionView ,name='companion'),
    path('alien-races/<int:pk>/', AlienView ,name='alien-race'),
    path('villains/<int:pk>/', VillainView ,name='villain'),
    path('doctors/<int:pk>/', DoctorView, name='doctor'),
    path('companions/', CompanionView ,name='all-companions'),
    path('alien-races/', AlienView ,name='all-alien-races'),
    path('villains/', VillainView ,name='all-villains'),
    path('doctors/', DoctorView, name='all-doctors'),

    # re_path(r'companions/(?P<pk>[0-9]{1,4})/$',companion,name='view-companion'),
]