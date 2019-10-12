from .models import Album
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404


def index(request):
    all_album = Album.objects.all()
    context = {
        'all_album': all_album,
    }
    return render(request, 'music/index.html', context)


def details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album': album})