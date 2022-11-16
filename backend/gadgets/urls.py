from django.urls import re_path,path,include
from .views import *

urlpatterns = [
    path('',AllGadgetsAPIView.as_view(), name='all-gadgets'),
    path('<int:pk>/',GadgetDetailAPIView.as_view(), name='search-gadget' ),
]