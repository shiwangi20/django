from django.http import HttpResponse
from .models import Album
from django.shortcuts import render


def index(request):
    all_album = Album.objects.all()
    context = {
        'all_album': all_album,
    }
    return render(request, 'music/index.html', context)


def details(request, album_id):
    return HttpResponse('Details of album %s.' % album_id)
