from django.db import models


# Create your models here.
class BusStop(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)


class SubwayStation(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)


class BusLine(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=200)


class SubwayLine(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    route_stations = models.ManyToManyField(SubwayStation, through='SubwayRouteStation')


class BusRouteStop(models.Model):
    bus_line = models.ForeignKey(BusLine, on_delete=models.CASCADE)
    bus_stop = models.ForeignKey(BusStop, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    sequence = models.IntegerField()


"""
might be represented like:
    BusRouteStop.objects.create(bus_line=my_bus_line, bus_stop=A, sequence=1)
    BusRouteStop.objects.create(bus_line=my_bus_line, bus_stop=B, sequence=2)
    BusRouteStop.objects.create(bus_line=my_bus_line, bus_stop=C, sequence=3)
"""


class SubwayRouteStation(models.Model):
    subway_line = models.ForeignKey(SubwayLine, on_delete=models.CASCADE)
    subway_station = models.ForeignKey(SubwayStation, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    sequence = models.IntegerField()


class Bus(models.Model):
    bus_identifier = models.CharField(max_length=200)
    bus_line = models.ForeignKey(BusLine, on_delete=models.CASCADE)
    current_stop = models.ForeignKey(BusStop, on_delete=models.CASCADE)
    next_stop = models.ForeignKey(BusStop, related_name='+', on_delete=models.CASCADE)
    estimated_arrival_time_next_stop = models.TimeField(null=True)


class Subway(models.Model):
    train_identifier = models.CharField(max_length=200)
    subway_line = models.ForeignKey(SubwayLine, on_delete=models.CASCADE)
    current_station = models.ForeignKey(SubwayStation, on_delete=models.CASCADE)
    next_station = models.ForeignKey(SubwayStation, related_name='+', on_delete=models.CASCADE)
    estimated_arrival_time_next_stop = models.TimeField(null=True)
