from App_Final.models import Producto, Usuario, Articulo
from django.http import HttpResponse
from django.template import loader
from App_Final.forms import ProductoFormulario, UsuarioFormulario, ArticuloFormulario
from django.shortcuts import render
from datetime import date

# import clases basadas en vistas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class InicioListView(ListView):
    model = Articulo

    context_object_name = "Inicio"

    def get_queryset(self, *args, **kwargs): 
        query = super(InicioListView, self).get_queryset(*args, **kwargs) 
        query = query.all()[:3] 
        return query

    template_name = "App_Final/index.html"

class ProductosListView(ListView):
    model = Producto

    context_object_name = "Productos"

    template_name = "App_Final/productos.html"

class ProductosCreateView(CreateView):
    model = Producto

    template_name = "App_Final/productos-crear.html"

    success_url = reverse_lazy("Productos")

    fields = ["nombre", "detalle", "precio", "seccion_rostro"]

class ProductoDetailView(DetailView):
    model = Producto

    template_name = "App_Final/detalle.html"

class ArticulosListView(ListView):
    model = Articulo

    context_object_name = "Articulos"

    template_name = "App_Final/articulos.html"

class ArticulosCreateView(CreateView):
    model = Articulo

    template_name = "App_Final/articulos-crear.html"

    success_url = reverse_lazy("Articulos")

    fields = ["titulo", "detalle", "autor", "clasificacion"]

class ArticuloDetailView(DetailView):
    model = Articulo

    template_name = "App_Final/ver_mas.html"

# BUSCADORES
def buscar_productos(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = Producto.objects.filter(nombre__icontains=nombre)

        return render(request, "App_Final/productos.html", {"productos": productos})
    
    else:
        respuesta = "Error. El campo de búsqueda no fue completado."

        productos = Producto.objects.all()

        return render(request, "App_Final/productos.html", {"productos": productos, "respuesta": respuesta})
    
def buscar_articulos(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        articulos = Articulo.objects.filter(titulo__icontains=titulo)

        return render(request, "App_Final/articulos.html", {"articulos": articulos})
    
    else:
        respuesta = "Error. El campo de búsqueda no fue completado."

        articulos = Articulo.objects.all()

        return render(request, "App_Final/articulos.html", {"articulos": articulos, "respuesta": respuesta})