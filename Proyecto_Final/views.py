from django.http import HttpResponse
from django.template import loader

def inicio(request):
    productos = {"cosmeticos": ["Base", "Corrector", "Rubor", "Labial"]}

    plantilla = loader.get_template('index.html')

    documento = plantilla.render(productos)

    return HttpResponse(documento)

def login(request):
    plantilla = loader.get_template('login.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def registro(request):
    plantilla = loader.get_template('registro.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def detalle(request, id_producto):
    plantilla = loader.get_template('detalle.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def perfil(request, id_usuario):
    plantilla = loader.get_template('perfil.html')

    documento = plantilla.render()

    return HttpResponse(documento)