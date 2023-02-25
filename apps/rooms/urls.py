from django.urls import path
#My imports
from .views import RoomAPI,RoomDetailAPI,ReservationAPIViewSet

urlpatterns = [
    path('api/room/',RoomAPI.as_view(), name="api_room"),
    path('api/room/<int:pk>',RoomDetailAPI.as_view(), name="api_room_detail"),
    path('api/reservation/',ReservationAPIViewSet.as_view(), name="api_reservation"),
    
    
]

