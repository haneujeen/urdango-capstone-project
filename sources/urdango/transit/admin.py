from django.contrib import admin
from .models import BusStop, SubwayStation, BusLine, SubwayLine, BusRouteStop, SubwayRouteStation, Bus, Subway

# Register your models here.

admin.site.register(BusStop)
admin.site.register(SubwayStation)
admin.site.register(BusLine)
admin.site.register(SubwayLine)
admin.site.register(BusRouteStop)
admin.site.register(SubwayRouteStation)
admin.site.register(Bus)
admin.site.register(Subway)