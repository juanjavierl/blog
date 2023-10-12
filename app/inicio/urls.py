from . import views
from django.urls import path
urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('login/', views.login, name='login'),
]