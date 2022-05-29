from django.shortcuts import redirect, render
from django.urls import reverse
import os
from .models import Observation,Asteroid
from .forms import AsteroidFindForm
from .sources.loader import Loader

# Create your views here.

def main_view(request):
    
    return render(request, 'astronomical_observatory/main_view.html')


def asteroids_list(request):

    asteroids = Asteroid.objects.all()
    return render(request, 'astronomical_observatory/list.html', context={'asteroids':asteroids})


def load_files(request):
    
    if request.method == "POST":
        Loader.process_document()
        return redirect('astronomical_observatory:load_success')
    else:
        return render(request, 'astronomical_observatory/load_files.html')


def load_success(request):

    return render(request, 'astronomical_observatory/load_success.html')


def asteroid_sightings(request):
    
    if request.method == "POST":
        form = AsteroidFindForm(request.POST)
        if form.is_valid():

            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            matrix = form.cleaned_data['matrix']

            asteroid = Asteroid(width=int(width),
                                height=int(height), 
                                matrix=matrix)
            
            existent_asteroid = asteroid.check_exists()

            if existent_asteroid is None:
                return redirect(reverse('astronomical_observatory:asteroid_sightings_empty'))
            else:
                return redirect('astronomical_observatory:asteroid_sightings_show', id=existent_asteroid.id)
        else:
            return render(request, 'astronomical_observatory/asteroid_sightings.html')    
    else:
        form = AsteroidFindForm()
        return render(request, 'astronomical_observatory/asteroid_sightings.html',context={'form':form})
        

def asteroid_sightings_show(request, id):
    
    asteroid = Asteroid.objects.get(id=id)
    
    grid = asteroid.get_list_representation()

    observations = Observation.objects.filter(asteroid=id)

    return render(request, 'astronomical_observatory/asteroid_sightings_show.html',
                    context={'observations':observations, 'asteroid':asteroid, 'grid':grid})


def asteroid_sightings_empty(request):
    return render(request, 'astronomical_observatory/asteroid_sightings_empty.html')