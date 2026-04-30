from django.shortcuts import render, redirect
from django.http import JsonResponse
from order_manager.models import Order
from cart.models import Cart
from .forms import RegistroUsuarioForm


PRODUCTOS = [
    {"id": 1, "nombre": "Laptop Gamer", "precio": 18500, "descripcion": "16GB RAM, SSD 512GB"},
    {"id": 2, "nombre": "Mouse Inalámbrico", "precio": 450, "descripcion": "Ergonómico y rápido"},
    {"id": 3, "nombre": "Teclado Mecánico", "precio": 1200, "descripcion": "RGB profesional"},
    {"id": 4, "nombre": "Monitor 24 pulgadas", "precio": 3200, "descripcion": "Full HD"},
]


def lista_productos(request):
    return render(request, "ventas/ventas.html", {"productos": PRODUCTOS})


def agregar_carrito(request, producto_id):
    carrito = request.session.get("carrito", [])

    producto = next((p for p in PRODUCTOS if p["id"] == producto_id), None)

    if producto:
        carrito.append(producto)
        request.session["carrito"] = carrito

    return redirect("/ventas/")


def carrito(request):
    carrito = request.session.get("carrito", [])
    total = sum(producto["precio"] for producto in carrito)

    return render(request, "ventas/carrito.html", {
        "carrito": carrito,
        "total": total
    })


def procesar_pedido(request):
    carrito = request.session.get("carrito", [])
    total = sum(producto["precio"] for producto in carrito)

    if total > 0:
        cart = Cart.objects.create(user=request.user)

        Order.objects.create(
            cart=cart,
            total=total,
            status="Pendiente"
        )

    request.session["ultimo_total"] = total
    request.session["carrito"] = []

    return render(request, "ventas/pedido.html", {"total": total})


def ventas_view(request):
    return render(request, "ventas/grafica_ventas.html")


def datos_ventas(request):
    ordenes = Order.objects.all().order_by("created_at")

    labels = []
    datos = []

    for orden in ordenes:
        labels.append(orden.created_at.strftime("%d/%m/%Y"))
        datos.append(float(orden.total))

    return JsonResponse({
        "labels": labels,
        "datos": datos
    })

def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/admin/")
    else:
        form = RegistroUsuarioForm()

    return render(request, "ventas/registro.html", {"form": form})