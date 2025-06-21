
from django.shortcuts import render, redirect
from .models import Cliente

def landing(request):
    return render(request, 'LeoJy/landing.html')

def formulario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        Cliente.objects.create(nombre=nombre, email=email)
        return redirect('/')
    return render(request, 'LeoJy/formulario.html')

def listado(request):
    clientes = Cliente.objects.all()
    return render(request, 'LeoJy/listado.html', {'clientes': clientes})


def productos(request):
    clientes = Cliente.objects.all()
    nombre = request.POST.get('nombre')
    email = request.POST.get('email')
    Cliente.objects.create(nombre=nombre, email=email)
    return render(request, 'LeoJy/productos.html', {'clientes': clientes})