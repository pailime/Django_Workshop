# Generated by Django 4.1.5 on 2023-01-27 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('comment', models.TextField(null=True)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservation_app.conferenceroom')),
            ],
            options={
                'unique_together': {('date', 'room_id')},
            },
        ),
    ]
