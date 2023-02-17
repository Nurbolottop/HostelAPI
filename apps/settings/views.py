from rest_framework.generics import ListAPIView

#My imports
from apps.settings.models import Setting
from apps.settings.seriliazers import SettingSerilaizer

# Create your views here.

class SettingAPI(ListAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerilaizer