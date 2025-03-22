from django.db import models

class Movies(models.Model):                      #Movies es el nombre de la clase que se registra en models.py
    # Opciones para el campo género
    GENRE_CHOICES = [
        ('AC', 'Acción'),
        ('CO', 'Comedia'),
        ('DR', 'Drama'),
        ('MS', 'Misterio'),
        ('CS', 'Ciencia Ficción'),
    ]

    # Campos del modelo
    title = models.CharField(max_length=200, verbose_name="Título")
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES, verbose_name="Género")
    release_date = models.DateField(verbose_name="Fecha de lanzamiento")
    description = models.TextField(verbose_name="Descripción", blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"