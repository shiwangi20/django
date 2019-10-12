from django.http import HttpResponse
from .models import Album
from django.template import loader


def index(request):
    all_album = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_album': all_album
    }
    return HttpResponse(template.render(context, request))


def details(request, album_id):
    return HttpResponse('Details of album %s.' % album_id)
