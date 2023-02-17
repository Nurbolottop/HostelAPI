from rest_framework import serializers

#My imports
from apps.settings.models import Setting

class SettingSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'