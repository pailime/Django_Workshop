from django.shortcuts import render, redirect
from Reservation_app.models import ConferenceRoom, RoomReservation
import datetime

# Create your views here.


def base(request):
    rooms = ConferenceRoom.objects.all()
    return render(
        request,
        'base.html',
        context={'rooms': rooms}
    )


def homepage(request):
    rooms = ConferenceRoom.objects.all()
    for room in rooms:
        reservation_dates = [reserve.date for reserve in room.roomreservation_set.all()]
        room.reserved = datetime.date.today() in reservation_dates
    return render(
        request,
        'home_page.html',
        context={'rooms': rooms,}
    )


def addroom(request):
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


def delete(request, id):
    if request.method == "GET":
        room = ConferenceRoom.objects.get(id=id)
        room.delete()
        return redirect('home_page')


def modify(request, id):
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

        return redirect('home')


def reserve(request, id):
    room_reserve = RoomReservation.objects.all()
    room_id = ConferenceRoom.objects.get(id=id)
    if request.method == 'GET':
        return render(
            request,
            'reserve.html',
            context={'room_reserve': room_reserve, 'room_id': room_id}
        )
    elif request.method == 'POST':
        reserve_date = request.POST.get('reserve_date')
        reserve_comment = request.POST.get('reserve_comment')
        reservation = room_id.roomreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')

        if RoomReservation.objects.filter(room_id=room_id, date=reserve_date):
            return render(
                request,
                'reserve.html',
                context={'room_id': room_id,
                         'reservation': reservation,
                         'error': "Room id already booked"}
            )
        elif reserve_date < str(datetime.date.today()):
            return render(
                request,
                'reserve.html',
                context={'room_id': room_id,
                         'reservation': reservation,
                         'error': "You entered a date in the past"}
            )

        RoomReservation.objects.create(date=reserve_date, room_id=room_id, comment=reserve_comment)
        return redirect('home')


def roomdetails(request, room_id):
    room = ConferenceRoom.objects.get(id=room_id)
    #room = ConferenceRoom.objects.all()
    reservation = room.roomreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
    if request.method == 'GET':
        return render(
            request,
            'room_details.html',
            context={'room': room, 'reservation': reservation}
        )


