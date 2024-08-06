from django import forms
from datetime import date

class ProductoFormulario(forms.Form):
    listado_secciones_rostro = [
        ("rostro completo", "Rostro completo"),
        ("frente", "Frente"),
        ("cejas", "Cejas"),
        ("pestañas", "Pestañas"),
        ("parpados", "Párpados"),
        ("contorno de ojos", "Contorno de ojos"),
        ("pomulos", "Pómulos"),
        ("mejillas", "Mejillas"),
        ("nariz", "Nariz"),
        ("labios", "Labios"),
        ("menton", "Mentón"),
        ("cuello", "Cuello"),
    ]

    nombre = forms.CharField(
        max_length=40,
        error_messages={
            "required": "El campo nombre es obligatorio.",
            "max_length": "Recuerda que el campo tiene un máximo de 40 caracteres.",
        }
    )
    detalle = forms.CharField(
        widget=forms.Textarea,
        max_length=280,
        error_messages={
            "required": "El campo detalle es obligatorio.",
            "max_length": "Recuerda que el campo tiene un máximo de 200 caracteres.",
        }
    )
    precio = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        error_messages={
            "required": "El campo precio es obligatorio.",
            "max_digits": "Recuerda que el campo tiene un máximo de 8 dígitos.",
        }
    )
    seccion_rostro = forms.ChoiceField(choices=listado_secciones_rostro)

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(
        max_length=40,
        error_messages={
            "required": "El campo nombre es obligatorio.",
            "max_length": "Recuerda que el campo tiene un máximo de 40 caracteres.",
        }
    )
    apellido = forms.CharField(
        max_length=40,
        error_messages={
            "required": "El campo apellido es obligatorio.",
            "max_length": "Recuerda que el campo tiene un máximo de 40 caracteres.",
        }
    )
    email = forms.EmailField(error_messages={"required": "El campo email es obligatorio."})
    clave = forms.CharField(
        max_length=20,
        # widget=forms.PasswordInput,
    )
    rol = forms.IntegerField(
        initial=2,
        widget=forms.HiddenInput(),
    )

class ArticuloFormulario(forms.Form):
    listado_clasificaciones = [
        ("tendencias", "Tendencias"),
        ("productos virales", "Productos Virales"),
        ("tutoriales y consejos", "Tutoriales y consejos"),
        ("nuevos lanzamientos", "Nuevos lanzamientos"),
        ("reseñas y opiniones", "Reseñas y opiniones"),
        ("comparativas", "Comparativas"),
        ("diy", "DIY (Hazlo tú mismo)"),
        ("caro vs barato", "Producto caro VS Producto barato"),
    ]

    titulo = forms.CharField(
        max_length=40,
        error_messages={
            "required": "El campo título es obligatorio.",
            "max_length": "Recuerda que el campo tiene un máximo de 40 caracteres.",
        }
    )
    detalle = forms.CharField(
        widget=forms.Textarea,
        error_messages={"required": "El campo detalle es obligatorio.",}
    )
    fecha = forms.DateField(
        initial=date.today,
        widget=forms.HiddenInput(),
    )
    autor = forms.CharField(
        max_length=40,
        error_messages={
            "required": "El campo autor es obligatorio.",
            "max_length": "Recuerda que el campo tiene un máximo de 40 caracteres.",
        }
    )
    clasificacion = forms.ChoiceField(choices=listado_clasificaciones)