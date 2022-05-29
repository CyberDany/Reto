from django.urls import path
from . import views

app_name = 'astronomical_observatory'

urlpatterns = [
    path('', views.main_view, name="main_view"),
    path('asteroid_list/', views.asteroids_list, name="asteroids_list"),
    path('asteroid_sightings/', views.asteroid_sightings, name="asteroid_sightings"),
    path('asteroid_sightings/<int:id>', views.asteroid_sightings_show, name="asteroid_sightings_show"),
    path('asteroid_sightings_empty', views.asteroid_sightings_empty, name="asteroid_sightings_empty"),
    path('load_files/', views.load_files, name="load_files"),
    path('load_success/', views.load_success, name="load_success"),
]
