from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from Reservation_app.models import ConferenceRoom

# Create your views here.


def Base(request):
    rooms = ConferenceRoom.objects.all()
    return render(
        request,
        'base.html',
        context={'rooms': rooms}
    )


def HomePage(request):
    rooms = ConferenceRoom.objects.all()
    return render(
        request,
        'home_page.html',
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
        room_capacity = int(room_capacity) if room_capacity else 0
        projector = request.POST.get("projector") == 'on'
        if not room_name:
            return render(
                request,
                'add_room.html',
                context={'error': 'Please enter a Room Name'}
            )
        if ConferenceRoom.objects.filter(name=room_name):
            return render(
                request,
                'add_room.html',
                context={'error': 'This room already exists'}
            )
        if room_capacity <= 0:
            return render(
                request,
                'add_room.html',
                context={'error': 'The given value of Room Capacity must be positive'}
            )

        ConferenceRoom.objects.create(name=room_name, capacity=room_capacity, projector_availability=projector)
        return render(
            request,
            'home_page.html',
            context={'rooms': rooms}
        )


def Delete(request, id):
    if request.method == "GET":
        room = ConferenceRoom.objects.get(id=id)
        room.delete()
        return redirect('home_page')


def Modify(request, id):
    room = ConferenceRoom.objects.get(id=id)
    if request.method == "GET":
        return render(
            request,
            'modify.html',
            context={'room': room}
        )

    elif request.method == "POST":
        room_name = request.POST.get("room_name")
        room_capacity = request.POST.get("room_capacity")
        room_capacity = int(room_capacity) if room_capacity else 0
        projector = True if request.POST.get("projector") == 'on' else False
        if not room_name:
            return render(
                request,
                'modify.html',
                context={'error': 'Please enter a Room Name'}
            )
        if room_name != room.name and ConferenceRoom.objects.filter(name=room_name):
            return render(
                request,
                'modify.html',
                context={'error': 'This room already exists'}
            )
        if room_capacity <= 0:
            return render(
                request,
                'modify.html',
                context={'error': 'The given value of Room Capacity must be positive'}
            )

        room.name = room_name
        room.capacity = room_capacity
        room.projector_availability = projector
        room.save()

        return HttpResponseRedirect(reverse('home'))


