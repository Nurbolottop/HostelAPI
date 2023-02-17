from django.urls import path

#My imports
from apps.settings.views import SettingAPI

urlpatterns = [
    path('api/settings/',SettingAPI.as_view(), name="api_settings")
]

