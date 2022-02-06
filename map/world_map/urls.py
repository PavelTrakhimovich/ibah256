from django.urls import path
from .views import *

urlpatterns = [
    path('', map_view),
    path('list/', list_cliks),
    path('save_coordinates/', save_coordinates, name='save_coordinates'),
]