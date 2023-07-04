from django.db import models
import uuid


# Create your models here.
class User(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


class PushSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subscription = models.JSONField()

    def __str__(self):
        return f'PushSubscription {self.pk}: {self.subscription}'
