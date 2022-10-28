from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('companion/', AllCompanionsAPIView.as_view() ,name='all-companions'),
    # path('<>',companion,name='all-companions'),
    re_path(r'(?P<pk>[0-9]{1,4})/$',companion,name='view-companion'),
]