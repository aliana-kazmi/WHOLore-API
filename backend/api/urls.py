from django.urls import re_path,path,include
from . import views

urlpatterns = [
    path("", views.api_home),
    path("companion/",include('characters.urls')),
    path("gadget/",include('gadgets.urls')),
]