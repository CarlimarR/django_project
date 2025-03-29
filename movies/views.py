from django.shortcuts import render
from django.views.generic import ListView, DetailView
from movies.models import Movies


# Create your views here.

class MovieListView(ListView):                      #Aqui se registra la view
    model = Movies                                   #aqui el modelo es el de la clase que se registre en models.py
    template_name = 'movies/movie_list.html'         #NO olvides registrar los templates tambien

class MovieDetailView(DetailView):                    #Aqui se registra la view

    model = Movies                                   #aqui el modelo es el de la clsse que se registre en models.py
    template_name = 'movies/movie_detail.html'        #NO olvides registrar los templates tambien

