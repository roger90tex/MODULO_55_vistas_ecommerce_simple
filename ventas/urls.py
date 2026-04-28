from django.urls import path
from .views import lista_productos, carrito, procesar_pedido

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('carrito/', carrito, name='carrito'),
    path('pedido/', procesar_pedido, name='pedido'),
]