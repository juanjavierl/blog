from . import views
from django.urls import path
urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('login/', views.login, name='login'),

    path('detalleUser/', views.detalleUser, name='detalleUser'),

    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
]