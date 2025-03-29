from django.urls import path
from .views import MovieListView
from.views import MovieDetailView

urlpatterns = [

    path('', MovieListView.as_view(), name='movie_list'),      #Aqui se registra la url, si se colocan mas url se coloca una coma","
    path('movie/detail/<int:pk>', MovieDetailView.as_view(), name='movie_details')
    # int:pk es el id de la pelicula, se coloca pk porque es el nombre del campo en la base de datos
    # en la url se colocaria en id de la base de datos (movie/detail/1) y se mostraria la pelicula con id 1

]
