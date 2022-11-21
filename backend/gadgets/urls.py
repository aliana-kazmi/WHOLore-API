from django.urls import re_path,path,include
from .views import *

urlpatterns = [
    path('',GadgetView, name='all-gadgets'),
    path('<int:pk>/',GadgetView, name='search-gadget' ),
]