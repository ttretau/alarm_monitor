from django.db import models
import uuid


class Alarm(models.Model):
    # tracker = FieldTracker(fields=("title", "text", "created"))
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=450)
    created = models.DateTimeField(auto_now_add=True)
    test = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
