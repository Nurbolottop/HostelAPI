from rest_framework import serializers

from .models import Rooms,Reservation

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = "__all__"



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"