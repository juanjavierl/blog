from . import views
from django.urls import path
urlpatterns = [
    path('', views.loguearse, name='loguearse'),
    path('inicio/', views.inicio, name='inicio'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),

    path('contacto/', views.contacto, name='contacto'),

    path('detalleUser/', views.detalleUser, name='detalleUser'),

    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('ver_categorias/',views.ver_categorias, name='ver_categorias'),

    path('crear_producto/',views.crear_producto, name='crear_producto'),

    path('listar_productos/',views.listarProductos, name='listar_productos'),

    path('register/', views.register, name='register'),

    path('buscar/', views.buscar_por_letra, name='buscar_por_letra'),
    
    path("por_fechas/", views.por_fechas, name="por_fechas"),

    path('consultas/', views.consultas, name='consultas'),
    path('editar_producto/<int:id_producto>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id_producto>/',views.eliminar_producto, name='eliminar_producto')
]