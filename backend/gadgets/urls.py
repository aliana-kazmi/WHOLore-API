from django.urls import re_path,path,include
from .views import *

urlpatterns = [
    path('',AllGadgetsAPIView.as_view(), name='all-gadgets'),
    re_path(r'add-gadget',GadgetCreateAPIView.as_view() ,name = 'add-gadget'),
    path('<int:pk>/',GadgetDetailAPIView.as_view(), name='search-gadget' ),
]