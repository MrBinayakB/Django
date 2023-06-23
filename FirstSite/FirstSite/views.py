#File Created by MrBinayakB
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello there, its me Binayak")
