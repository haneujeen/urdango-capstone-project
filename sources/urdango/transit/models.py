from django.db import models


# Create your models here.
class Bus(models.Model):
    veh_id = models.CharField(max_length=50, primary_key=True)
    st_id = models.IntegerField()
    st_ord = models.IntegerField()
    stop_flag = models.IntegerField()
    data_tm = models.IntegerField()
    tm_x = models.FloatField()
    tm_y = models.FloatField()
    plain_no = models.CharField(max_length=100)
    bus_type = models.IntegerField()
    last_stn_id = models.IntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    passenger_load = models.IntegerField()
    is_full_flag = models.BooleanField(default=False)


class PushSubscription(models.Model):
    endpoint = models.URLField(max_length=400)
    p256dh = models.CharField(max_length=255)
    auth = models.CharField(max_length=255)

