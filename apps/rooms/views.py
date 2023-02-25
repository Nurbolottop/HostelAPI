from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

from .serializers import RoomSerializer,Rooms,ReservationSerializer,Reservation
from rest_framework import generics
# Create your views here.

class RoomAPI(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    
class RoomDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    
class ReservationAPIViewSet(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer