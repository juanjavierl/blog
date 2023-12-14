from . import views
from django.urls import path
urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('login/', views.login, name='login'),

    path('detalleUser/', views.detalleUser, name='detalleUser'),

    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('ver_categorias/',views.ver_categorias, name='ver_categorias'),

    path('crear_producto/',views.crear_producto, name='crear_producto'),

    path('listar_productos/',views.listarProductos, name='listar_productos'),

    path('register/', views.register, name='register'),
]