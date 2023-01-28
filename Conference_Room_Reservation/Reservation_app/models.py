from django.db import models


class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector_availability = models.BooleanField()


class RoomReservation(models.Model):
    date = models.DateTimeField()
    room_id = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('date', 'room_id')
