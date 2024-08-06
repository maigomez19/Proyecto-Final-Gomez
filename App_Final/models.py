from django.db import models
from django.utils import timezone

class Producto(models.Model):
    listado_secciones_rostro = [
        ("rostro completo", "Rostro completo"),
        ("frente", "Frente"),
        ("cejas", "Cejas"),
        ("pestañas", "Pestañas"),
        ("párpados", "Párpados"),
        ("contorno de ojos", "Contorno de ojos"),
        ("pómulos", "Pómulos"),
        ("mejillas", "Mejillas"),
        ("nariz", "Nariz"),
        ("labios", "Labios"),
        ("mentón", "Mentón"),
        ("cuello", "Cuello"),
    ]

    nombre = models.CharField(max_length=40)
    detalle = models.TextField(max_length=280)
    precio = models.DecimalField(max_digits=8,decimal_places=2)
    seccion_rostro = models.CharField(max_length=40, choices=listado_secciones_rostro)

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    clave = models.CharField(max_length=20)
    rol = models.IntegerField()

class Articulo(models.Model):
    listado_clasificaciones = [
        ("tendencias", "Tendencias"),
        ("productos virales", "Productos Virales"),
        ("tutoriales y consejos", "Tutoriales y consejos"),
        ("nuevos lanzamientos", "Nuevos lanzamientos"),
        ("reseñas y opiniones", "Reseñas y opiniones"),
        ("comparativas", "Comparativas"),
        ("DIY", "DIY (Hazlo tú mismo)"),
        ("caro vs barato", "Producto caro VS Producto barato"),
    ]

    titulo = models.CharField(max_length=40)
    detalle = models.TextField()
    fecha = models.DateField(default=timezone.now)
    autor = models.CharField(max_length=40)
    clasificacion = models.CharField(max_length=40, choices=listado_clasificaciones)