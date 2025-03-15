from django.shortcuts import render
from django.views.generic import ListView
from post.models import post                #Aqui tambien se importa el modelo post

# Create your views here.

class post(ListView):
    model = post
    template_name = 'post.html'

