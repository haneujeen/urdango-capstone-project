from django.db import models


# Create your models here.
class PushSubscription(models.Model):
    subscription = models.JSONField()

    def __str__(self):
        return f'PushSubscription {self.pk}: {self.subscription}'

