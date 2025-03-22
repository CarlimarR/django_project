from django.shortcuts import render
from django.views.generic import ListView, DetailView
from movies.models import Movies


# Create your views here.

class MovieListView(ListView):                      #Aqui se registra la view
    model = Movies                                   #aqui el modelo es el de la clsse que se registre en models.py
    template_name = 'movies/movie_list.html'         #NO olvides registrar los templas tambien
