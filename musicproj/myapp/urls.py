from django.urls import path
from .views import *

urlpatterns = [
    path('', genre_list, name='genre_list'),
    path('genres/<int:genre_id>/', musician_list, name='musician_list'),
    path('musicians/<int:musician_id>/', musician_detail, name='musician_detail'),
]