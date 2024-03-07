from django.db import models
from datetime import date, datetime
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
    
class FacturaCompra(models.Model):
        fecha = models.DateField("Fecha", default=date.today)
        cantidad = models.IntegerField("Cantidad")
        sub_total = models.FloatField("Sub Total")
        id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
        id_compra = models.IntegerField("ID Compra")
        


class Cliente(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    apellidos = models.CharField("Apellidos", max_length=100)
    direccion = models.CharField("Dirección", max_length=100)
    celular = models.IntegerField("Celular")
    nit = models.CharField("NIT", max_length=25)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def _str_(self):
        return f"{self.nombre} {self.apellidos}"


class Compra(models.Model):
    fecha_hora = models.DateTimeField("Fecha y Hora", default=datetime.now)  # Corregido
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.FloatField("Descuento")
    sub_total = models.FloatField("Sub Total")
    total_compra = models.FloatField("Total de Compra")

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'




class Proveedor(models.Model):
    razon_social = models.CharField(max_length=100)
    celular = models.IntegerField()
    nit = models.CharField(max_length=25)
    pagina_web = models.CharField(max_length=150)

    def __str__(self):
        return self.razon_social



class Orden(models.Model):
    fecha = models.DateField("Fecha", default=date.today)
    cod_orden = models.CharField("Código de Orden", max_length=25)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    descuento = models.FloatField("Descuento")
    sub_total = models.FloatField("Sub Total")
    total = models.FloatField("Total")

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'


class DetalleCompra(models.Model):
    fecha = models.DateField("Fecha", default=date.today)
    cantidad = models.IntegerField("Cantidad")
    sub_total = models.FloatField("Sub Total")
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compra'

