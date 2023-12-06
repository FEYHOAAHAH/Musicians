
from django.shortcuts import render, get_object_or_404
from .models import Genre, Musician


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'myapp/genre_list.html', {'genres': genres})


def musician_list(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    musicians = Musician.objects.filter(genre=genre)
    return render(request, 'myapp/musician_list.html', {'genre': genre, 'musicians': musicians})


def musician_detail(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    return render(request, 'myapp/musician_detail.html', {'musician': musician})
