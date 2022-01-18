from rest_framework import serializers
from .models import Alarm


class AlarmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alarm
        fields = ['id', 'title', 'text', 'created', 'test', 'closed']

    def to_representation(self, obj):
        return {
            "id": str(obj.id),
            "title": obj.title,
            "text": obj.text,
            "created": obj.created.isoformat(),
            "test": obj.test,
            "closed": obj.closed
        }
