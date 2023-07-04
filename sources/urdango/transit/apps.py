from django.apps import AppConfig
from .scheduler import scheduler


class TransitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transit'

    def ready(self):
        scheduler.start()
