from django import forms
from django import forms
from .models import Asteroid
from django.forms import ModelForm


class AsteroidFindForm(ModelForm):
    class Meta:
        model = Asteroid
        fields = "__all__"
