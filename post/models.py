from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=100)                 # esto es un titulo. El max_length es requerido.
    content = models.TextField()                             # esto es el contenido del post
    created_at = models.DateTimeField(auto_now_add=True)     # esto es la fecha de creacion del post
    updated_at = models.DateTimeField(auto_now=True)         # esto es la fecha de actualizacion del post
    # Como insertar las imagenes:
    #image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title                        # esto es para que en el admin se muestre el titulo del post