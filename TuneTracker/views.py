
from django.shortcuts import render, redirect, get_object_or_404


from .models import Song, Artist


def song_list(request):
    songs = Song.objects.all()

    return render(request, 'song_list.html', {'songs': songs})


def add_song(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist_name = request.POST.get('artist')

        # Check if the artist exists or create a new one
        artist, created = Artist.objects.get_or_create(name=artist_name)

        # Create a new song with the current date
        Song.objects.create(title=title, artist=artist)

        return redirect('song_list')

    return render(request, 'song_list.html', {'songs': Song.objects.all()})


def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if request.method == 'POST':
        song.delete()

    return redirect('song_list')