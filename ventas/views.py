from django.shortcuts import render
from django.http import HttpResponse

def lista_productos(request):
    productos = [
        {"nombre": "Laptop Gamer", "precio": 18500, "descripcion": "16GB RAM, SSD 512GB"},
        {"nombre": "Mouse Inalámbrico", "precio": 450, "descripcion": "Ergonómico y rápido"},
        {"nombre": "Teclado Mecánico", "precio": 1200, "descripcion": "RGB profesional"},
        {"nombre": "Monitor 24 pulgadas", "precio": 3200, "descripcion": "Full HD"},
    ]
    return render(request, "ventas/ventas.html", {"productos": productos})


def carrito(request):
    return HttpResponse("🛒 Carrito de compras vacío por ahora")


def procesar_pedido(request):
    return HttpResponse("✅ Pedido procesado correctamente")