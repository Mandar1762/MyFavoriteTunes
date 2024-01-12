# TuneTracker/urls.py
from django.urls import path
from .views import song_list, add_song, delete_song

urlpatterns = [
    path('', song_list, name='song_list'),
    path('add_song/', add_song, name='add_song'),
    path('delete_song/<int:song_id>/', delete_song, name='delete_song'),

]
