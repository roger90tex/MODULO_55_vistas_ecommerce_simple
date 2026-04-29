from django.urls import path
from .views import (
    lista_productos,
    carrito,
    procesar_pedido,
    ventas_view,
    datos_ventas,
    agregar_carrito,
)

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('carrito/', carrito, name='carrito'),
    path('pedido/', procesar_pedido, name='pedido'),
    path('agregar/<int:producto_id>/', agregar_carrito, name='agregar_carrito'),

    path('grafica/', ventas_view, name='ventas_grafica'),
    path('grafica/datos/', datos_ventas, name='datos_ventas'),
]