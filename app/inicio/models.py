from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre_categoria = models.CharField("Nombre Categoria", max_length=60)
    estado = models.BooleanField(default = True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nombre_categoria

