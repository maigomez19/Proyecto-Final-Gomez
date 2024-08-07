from django.urls import path
from App_Usuario import views

urlpatterns = [
    # Usuario
    path('login/', views.login, name='Login'),
    path('registro/', views.registro, name='Registro'),
    path('perfil/<pk>', views.PerfilDetailView.as_view(), name='Perfil'),
]
