from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):

    dest1= Destination()
    dest1.name='Mumbai'
    dest1.desc='City Never Sleeps'
    dest1.img='destination_1.jpg'
    dest1.price=700

    dest2= Destination()
    dest2.name='Kathmandu'
    dest2.desc='City of Temple'
    dest2.img='destination_2.jpg'
    dest2.price=900
    
    dest3= Destination()
    dest3.name='Pokhara'
    dest3.desc='Heavenly City'
    dest3.img='destination_3.jpg'
    dest3.price=750
    
    dests=[dest1,dest2,dest3]

    return render(request,'index.html',{'dests':dests})