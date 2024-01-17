from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('download_csv/', download_csv, name='download_csv'),

]
