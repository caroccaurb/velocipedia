from django.shortcuts import render, get_object_or_404
from .models import Bicicleta, Neumatico, Freno, Producto
from django.contrib import messages
# Create your views here.

def bicicleta(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, 'paginapp/bicicleta.html', {'bicicletas': bicicletas})

def neumatico(request):
    neumaticos = Neumatico.objects.all()
    return render(request, 'paginapp/neumatico.html', {'neumaticos' : neumaticos})

def frenos(request):
    frenos = Freno.objects.all()
    return render(request, 'paginapp/frenos.html', {'frenos': frenos})


def carrito(request):
    return render(request, 'pagina/carrito.html')

def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = Carrito(request)
    producto = Producto.object.get(id=producto_id)
    
    messages.success(request, f"Producto {producto.nombre} agregado al carrito.")
    carrito.agregar(producto)

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.object.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("index")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.object.get(id=producto_id)
    carrito.restar(producto)
    return redirect("index")

def limpiar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.object.get(id=producto_id)
    carrito.limpiar()
    return redirect("index")