from django.urls import path
from .views import MovieListView

urlpatterns = [

    path('', MovieListView.as_view(), name='movie_list')           #Aqui se registra la url

]
