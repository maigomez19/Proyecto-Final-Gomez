"""
URL configuration for Proyecto_Final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from App_Final import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    # Usuario
    path('login/', views.login, name='Login'),
    path('registro/', views.registro, name='Registro'),
    path('perfil/<id_usuario>', views.perfil, name='Perfil'),

    # Producto
    path('productos/', views.productos, name='Productos'),
    path('productos/buscar/', views.buscar_productos, name='Buscar Productos'),
    path('productos/crear/', views.crear_producto, name='Crear Producto'),
    path('productos/<id_producto>', views.detalle, name='Detalle Producto'),

    # Articulo
    path('articulos/', views.articulos, name='Articulos'),
    path('articulos/buscar/', views.buscar_articulos, name='Buscar Articulos'),
    path('articulos/crear/', views.crear_articulo, name='Crear Articulo'),
    path('articulos/<id_articulos>', views.ver_mas, name='Detalle Articulo'),
]
