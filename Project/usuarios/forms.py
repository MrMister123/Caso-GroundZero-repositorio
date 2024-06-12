from django import forms
from .models import Genero

from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        Model = Genero
        fields = "__all__"