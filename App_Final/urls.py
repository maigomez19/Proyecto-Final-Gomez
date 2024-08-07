from django.urls import path
from App_Final import views

urlpatterns = [
    path('', views.InicioListView.as_view(), name='Inicio'),

    # Producto
    path('productos/', views.ProductosListView.as_view(), name='Productos'),
    path('productos/buscar/', views.buscar_productos, name='BuscarProductos'),
    path('productos/crear/', views.ProductosCreateView.as_view(), name='CrearProducto'),
    path('productos/<pk>', views.ProductoDetailView.as_view(), name='DetalleProducto'),

    # Articulo
    path('articulos/', views.ArticulosListView.as_view(), name='Articulos'),
    path('articulos/buscar/', views.buscar_articulos, name='BuscarArticulos'),
    path('articulos/crear/', views.ArticulosCreateView.as_view(), name='CrearArticulo'),
    path('articulos/<pk>', views.ArticuloDetailView.as_view(), name='DetalleArticulo'),
]
