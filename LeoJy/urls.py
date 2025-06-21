from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('productos/', views.productos, name='productos'),
    path('formulario/', views.formulario, name='formulario'),
    path('clientes/', views.listado, name='listado'),
]
