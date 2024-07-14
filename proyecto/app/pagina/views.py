from cgitb import html
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from paginapp.models import Producto
from paginapp.carrito import Carrito
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'pagina/index.html') 


def tecnico(request):
    return render(request, 'pagina/tecnico.html')

def login(request):
    return render(request, 'registration/login.html')

def recuperar_contraseña(request):
    return render(request, 'registration/recupera_contra.html')

def registrar(request):
    return render(request, 'registration/registrar.html')


def mi_cuenta(request):
    if request.method == 'POST':
        email = request.POST.get('nombre')
        password = request.POST.get('contraseña')
        user = authenticate(request, username=email, password=password)
        if user is True:
            login(request, user)
            return redirect('index.html')
        else:
            messages.error(request, 'Email o contraseña incorrectos.')
    return render(request, 'registration/login.html')


def carrito(request):
    return render(request, 'pagina/carrito.html')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.agregar(producto)
    
    messages.success(request, f"Producto {producto.nombre} agregado al carrito.")
    return redirect('bicicleta')

def agregar_otro_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = Carrito(request)
    carrito.agregar(producto)
    return redirect('carrito')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("index")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")