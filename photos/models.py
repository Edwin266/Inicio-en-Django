from django.db import models

# Create your models here.
from django.db.models import CharField

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)


class Photo(models.Model):
    name = models.CharField(max_length=150)  # Nombre con un maximo de 150 caracteres
    url = models.URLField()  # Fuente de la foto
    description = models.TextField(blank=True, null=True, default="")  # Opcion de dejan en blanco el campo
    created_at = models.DateTimeField(auto_now_add=True)  # Guarda el valor del instante de tiempo en que se guarda el objeto
    modified_at = models.DateTimeField(auto_now=True)  # Cada vez que se guarde la foto se actualiza
    license = models.CharField(max_length=3, choices=LICENSES)
    # Muestra el nombre en lugar de PHOTO OBJECT (1)
    def __str__(self):
        return self.name
