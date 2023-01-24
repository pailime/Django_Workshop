from django.shortcuts import render
from Reservation_app.models import ConferenceRoom

# Create your views here.


def base(request):
    rooms = ConferenceRoom.objects.all()
    return render(
        request,
        'base.html',
        context={'rooms': rooms}
    )


def AddRoom(request):
    rooms = ConferenceRoom.objects.all()
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass
