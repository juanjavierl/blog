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


class Producto(models.Model):
    nombre = models.CharField("Nombre producto", max_length=50)
    precio = models.FloatField("Precio", blank=True, null=True, help_text="Campo Opcional")
    stock = models.IntegerField("Stock")
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    imagen = models.ImageField("Imagen", upload_to='img_productos')

    estado = models.BooleanField(default = True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

        ordering = ["-id"]
    
    def __str__(self):
        return self.nombre

