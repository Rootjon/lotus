from django.contrib import admin
from django.db import models
from .models import Album

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'thumbnail',
        'description',
        'short_descripton',
        'creation',


    ]
admin.site.register(Album, AlbumAdmin)
