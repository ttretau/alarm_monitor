from django.dispatch import receiver
from django.db.models.signals import post_save
from alarm.models import Alarm
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from alarm.serializers import AlarmSerializer


async def update_alarm(updated_alarm):
    serializer = AlarmSerializer(updated_alarm)
    channel_layer = get_channel_layer()
    content = {
        "type": "ALARM_UPDATE",
        "payload": serializer.data,
    }
    await channel_layer.group_send("alarm", {
        "type": "notify",
        "content": content,
    })


@receiver(post_save, sender=Alarm)
def publish_event(instance, **kwargs):
    async_to_sync(update_alarm)(instance)
