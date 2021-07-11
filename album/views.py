from django.shortcuts import render
from .models import Album

# Create your views here.

def list (request):
    albums = Album.objects.all()

    context = {
        'albums':albums
    }

    return render (request, 'album/index.html',context)
