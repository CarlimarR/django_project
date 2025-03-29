from django.urls import path
from .views import MovieListView
from.views import MovieDetailView

urlpatterns = [

    path('', MovieListView.as_view(), name='movie_list'),      #Aqui se registra la url, si se colocan mas url se coloca una coma","
    path('movie/detail/<int:pk>', MovieDetailView.as_view(), name='movie_details')

]
