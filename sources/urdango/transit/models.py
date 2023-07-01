from django.db import models


# Create your models here.
class PushSubscription(models.Model):
    endpoint = models.URLField(max_length=255, unique=True)
    expiration_time = models.CharField(max_length=255, null=True)
    p256dh = models.CharField(max_length=255)
    auth = models.CharField(max_length=255)

    def __str__(self):
        return f'PushSubscription {self.pk} for endpoint {self.endpoint}'

