from django.contrib import admin
from astronomical_observatory.models import Observation,Asteroid

# Register your models here.
admin.site.register(Observation)
admin.site.register(Asteroid)