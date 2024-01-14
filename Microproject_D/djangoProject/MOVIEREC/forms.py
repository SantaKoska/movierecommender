from django import forms
from .models import Genrecinema

class GenreForm(forms.Form):
    genre = forms.ChoiceField(choices=Genrecinema.GENRE_CHOICES)
