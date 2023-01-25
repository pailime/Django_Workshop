from django.shortcuts import render, redirect
from Reservation_app.models import ConferenceRoom

# Create your views here.


def Base(request):
    rooms = ConferenceRoom.objects.all()
    return render(
        request,
        'base.html',
        context={'rooms': rooms}
    )


def AddRoom(request):
    rooms = ConferenceRoom.objects.all()
    if request.method == "GET":
        return render(
            request,
            'add_room.html',
            context={'rooms': rooms}
        )

    elif request.method == "POST":
        room_name = request.POST.get("room_name")
        room_capacity = request.POST.get("room_capacity")
        projector = request.POST.get("projector")
        if not room_name:
            return render(
                'add_room.html',
                context={'error': 'Please enter a Room Name'}
            )
        if room_name == rooms.name:
            return render(
                'add_room.html',
                context={'error': 'This room already exists'}
            )
        if room_capacity <= 0:
            return render(
                'add_room.html',
                context={'error': 'The given value of Room Capacity must be positive'}
            )

        ConferenceRoom.objects.create(name=room_name, capacity=room_capacity, projector_availability=projector)
        return redirect("Base")

