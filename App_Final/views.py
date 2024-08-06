from App_Final.models import Producto, Usuario, Articulo
from django.http import HttpResponse
from django.template import loader
from App_Final.forms import ProductoFormulario, UsuarioFormulario, ArticuloFormulario
from django.shortcuts import render
from datetime import date

def inicio(request):
    articulos = Articulo.objects.all()[:3]

    return render(request, "App_Final/index.html", {"articulos": articulos})

def login(request):
    plantilla = loader.get_template('App_Final/login.html')

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

            return render(request, "App_Final/registro.html", {"formulario": formulario, "respuesta": respuesta, "tipo": tipo})
    else:
        formulario = UsuarioFormulario()

    return render(request, "App_Final/registro.html", {"formulario": formulario})

def perfil(request, id_usuario):
    plantilla = loader.get_template('App_Final/perfil.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def buscar_productos(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = Producto.objects.filter(nombre__icontains=nombre)

        return render(request, "App_Final/productos.html", {"productos": productos})
    
    else:
        respuesta = "Error. El campo de búsqueda no fue completado."

        productos = Producto.objects.all()

        return render(request, "App_Final/productos.html", {"productos": productos, "respuesta": respuesta})

def productos(request):
    productos = Producto.objects.all()

    return render(request, "App_Final/productos.html", {"productos": productos})

def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            producto = Producto(
                nombre=informacion["nombre"], 
                detalle=informacion["detalle"], 
                precio=informacion["precio"], 
                seccion_rostro=informacion["seccion_rostro"]
            )
            producto.save()

            formulario = ProductoFormulario()

            respuesta = "¡Producto creado con éxito!"

            tipo = "success"

            return render(request, "App_Final/productos-crear.html", {"formulario": formulario, "respuesta": respuesta, "tipo": tipo})
    else:
        formulario = ProductoFormulario()

    return render(request, "App_Final/productos-crear.html", {"formulario": formulario})

def detalle(request, id_producto):
    plantilla = loader.get_template('App_Final/detalle.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def buscar_articulos(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        articulos = Articulo.objects.filter(titulo__icontains=titulo)

        return render(request, "App_Final/articulos.html", {"articulos": articulos})
    
    else:
        respuesta = "Error. El campo de búsqueda no fue completado."

        articulos = Articulo.objects.all()

        return render(request, "App_Final/articulos.html", {"articulos": articulos, "respuesta": respuesta})

def articulos(request):
    articulos = Articulo.objects.all()

    return render(request, "App_Final/articulos.html", {"articulos": articulos})

def crear_articulo(request):
    if request.method == 'POST':
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            articulo = Articulo(
                titulo=informacion["titulo"], 
                detalle=informacion["detalle"],
                fecha=date.today, 
                autor=informacion["autor"], 
                clasificacion=informacion["clasificacion"]
            )
            articulo.save()

            formulario = ArticuloFormulario()

            respuesta = "¡Artículo creado con éxito!"

            tipo = "success"

            return render(request, "App_Final/articulos-crear.html", {"formulario": formulario, "respuesta": respuesta, "tipo": tipo})
    else:
        formulario = ArticuloFormulario()

    return render(request, "App_Final/articulos-crear.html", {"formulario": formulario})

def ver_mas(request, id_producto):
    plantilla = loader.get_template('App_Final/ver_mas.html')

    documento = plantilla.render()

    return HttpResponse(documento)