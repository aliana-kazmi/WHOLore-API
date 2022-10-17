from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('',all_companions,name='all-companions'),
    re_path(r'<int:id>/',companion,name='view-companion'),
]