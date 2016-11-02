from django.contrib import admin

from .models import Event, Category, Place, Schedule, PlaceSchedule, Galery

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Schedule)
admin.site.register(PlaceSchedule)
admin.site.register(Galery)
