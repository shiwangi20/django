from django.contrib import admin
from .models import Album, Song

admin.register(Album, Song)(admin.ModelAdmin)
