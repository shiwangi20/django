from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('This is a Music app homepage')


def details(request, album_id):
    return HttpResponse('Details of album %s.' % album_id)
