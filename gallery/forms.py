from django import forms
from .models import Artist, Painting

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'nationality', 'biography']

class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = ['title', 'year', 'medium', 'artist']