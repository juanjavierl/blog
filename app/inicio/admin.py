from django.contrib import admin
from .models import * #Categoria
# Register your models here.
admin.site.register(Categoria)

admin.site.register(Producto)

admin.site.register(Cliente)

admin.site.register(Compra)

admin.site.register(Proveedor)
admin.site.register(Orden)

admin.site.register(FacturaCompra)

