#File Created by MrBinayakB
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello there, its me Binayak")

def about(request):
    return HttpResponse("About Binayak")