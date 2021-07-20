from django.http import HttpResponse
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    html = ''

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

