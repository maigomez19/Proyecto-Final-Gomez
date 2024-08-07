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

def login(request):
    plantilla = loader.get_template('App_Usuario/login.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def registro(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = Usuario(
                nombre=informacion["nombre"], 
                apellido=informacion["apellido"], 
                email=informacion["email"],
                clave=hash(informacion["clave"]), 
                rol=2,
            )
            usuario.save()

            formulario = UsuarioFormulario()

            respuesta = "¡Registro realizado con éxito!"

            tipo = "success"

            return render(request, "App_Usuario/registro.html", {"formulario": formulario, "respuesta": respuesta, "tipo": tipo})
    else:
        formulario = UsuarioFormulario()

    return render(request, "App_Usuario/registro.html", {"formulario": formulario})

class PerfilDetailView(DetailView):
    model = Usuario

    template_name = "App_Usuario/perfil.html"
