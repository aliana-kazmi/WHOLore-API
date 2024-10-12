from django.urls import path
from .views import *

urlpatterns = [
    path('',GadgetView, name='all-gadgets'),
    path('<str:name>/',GadgetView, name='search-gadget' ),
]