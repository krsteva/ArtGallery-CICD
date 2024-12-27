from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, Painting
from .forms import ArtistForm, PaintingForm

def artist_list(request):
   artists = Artist.objects.all()
   return render(request, 'artist_list.html', {'artists': artists})

def artist_detail(request, pk):
   artist = get_object_or_404(Artist, pk=pk)
   return render(request, 'artist_detail.html', {'artist': artist})

def artist_create(request):
   if request.method == 'POST':
       form = ArtistForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('artist_list')
   else:
       form = ArtistForm()
   return render(request, 'artist_form.html', {'form': form})

def artist_update(request, pk):
   artist = get_object_or_404(Artist, pk=pk)
   if request.method == 'POST':
       form = ArtistForm(request.POST, instance=artist)
       if form.is_valid():
           form.save()
           return redirect('artist_list')
   else:
       form = ArtistForm(instance=artist)
   return render(request, 'artist_form.html', {'form': form})

def artist_delete(request, pk):
   artist = get_object_or_404(Artist, pk=pk)
   if request.method == 'POST':
       artist.delete()
       return redirect('artist_list')
   return render(request, 'artist_confirm_delete.html', {'artist': artist})

def painting_list(request):
   paintings = Painting.objects.all()
   return render(request, 'painting_list.html', {'paintings': paintings})

def painting_detail(request, pk):
   painting = get_object_or_404(Painting, pk=pk)
   return render(request, 'painting_detail.html', {'painting': painting})

def painting_create(request):
   if request.method == 'POST':
       form = PaintingForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('painting_list')
   else:
       form = PaintingForm()
   return render(request, 'painting_form.html', {'form': form})

def painting_update(request, pk):
   painting = get_object_or_404(Painting, pk=pk)
   if request.method == 'POST':
       form = PaintingForm(request.POST, instance=painting)
       if form.is_valid():
           form.save()
           return redirect('painting_list')
   else:
       form = PaintingForm(instance=painting)
   return render(request, 'painting_form.html', {'form': form})

def painting_delete(request, pk):
   painting = get_object_or_404(Painting, pk=pk)
   if request.method == 'POST':
       painting.delete()
       return redirect('painting_list')
   return render(request, 'painting_confirm_delete.html', {'painting': painting})