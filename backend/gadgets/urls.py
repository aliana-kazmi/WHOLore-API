from django.urls import re_path,path,include
from .views import *

urlpatterns = [
    re_path(r'add-gadget',add_gadget,name = 'add-gadget'),
]