from django.contrib import admin
from .models import Album, Song

admin.site.register(Album)
admin.site.register(Song)

#line no 4&5 best alternative for multiple model register
admin.register(Album, Song)(admin.ModelAdmin)
