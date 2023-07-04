from django.db import models
import uuid


# Create your models here.
class PushSubscription(models.Model):
    subscription = models.JSONField()

    def __str__(self):
        return f'PushSubscription {self.pk}: {self.subscription}'


class User(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
