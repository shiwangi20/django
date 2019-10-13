from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Album, Song


def index(request):
    all_album = Album.objects.all()
    context = {
        'all_album': all_album,
    }
    return render(request, 'music/index.html', context)


def details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html',
                      {'album': album,
                       'error_message': "You did not select anything",
                       })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})
