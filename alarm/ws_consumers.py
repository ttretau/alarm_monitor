from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.auth import login


class NotificationWebsocketConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None

    async def connect(self):
        """
        Accept every connection, verify user later
        """
        self.user = self.scope["user"]

        await self.accept()

    async def notify(self, event):
        """
        This sends client notifications
        """
        await self.send_json(event["content"])

    async def receive_json(self, content, **kwargs):
        """
        This handles client registrations.

        TODO validate user
        """
        self.groups.append("alarm")
        await self.channel_layer.group_add(
            "alarm",
            self.channel_name,
        )
