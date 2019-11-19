from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import proveedor, Cliente
from django.contrib.auth.decorators import login_required

# Create your views here.

# CRUD Proveedor

# Create your views here
@login_required()
def index(request):
    return render(request, template_name='index.html')


def proveedor_list(request):
    proveedores = proveedor.objects.all()

    if request.method == 'POST':
        p = proveedor()
        p.nombre = request.POST.get('Nombre')
        p.direccion = request.POST.get('Direccion')
        p.telefono = request.POST.get('Telefono')
        p.descripcion = request.POST.get('Descripcion')
        p.save()
        return redirect('apiApp:pro_list')

    return render(request, template_name='proveedor/proveedor_list.html', context={'proveedores': proveedores})


def proveedor_watch(request, id):
    pro = proveedor.objects.get(id=id)
    return render(request, template_name='proveedor/proveedor_watch.html', context={'pro': pro})


def proveedor_edit(request, id):
    pro = proveedor.objects.get(id=id)

    if request.method == 'POST':
        pro.nombre = request.POST.get('Nombre')
        pro.direccion = request.POST.get('Direccion')
        pro.telefono = request.POST.get('Telefono')
        pro.descripcion = request.POST.get('Descripcion')
        pro.save()
        return redirect('apiApp:pro_list')
    return render(request, template_name='proveedor/proveedor_edit.html', context={'pro': pro})


def proveedor_delete(request, id):
    pro = proveedor.objects.get(id=id)

    if request.method == 'POST':
        pro.delete()
        return redirect('apiApp:pro_list')
    return render(request, template_name='proveedor/proveedor_delete.html', context={'pro': pro})


#CRUD Clientes

def cliente_list(request):
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        c = Cliente()
        c.nombre = request.POST.get('Nombre')
        c.apellido = request.POST.get('Apellido')
        c.tipo = request.POST.get('Tipo')
        c.direccion = request.POST.get('Direccion')
        c.telefono = request.POST.get('Telefono')
        c.email = request.POST.get('Email')
        c.organizacion = request.POST.get('Organizacion')
        c.dui = request.POST.get('Dui')
        c.nit = request.POST.get('Nit')
        c.save()
        return redirect('apiApp:cli_list')
    return render(request, template_name='cliente/cliente_list.html', context={'clientes': clientes})


def cliente_watch(request, id):
    cli = Cliente.objects.get(id=id)
    return render(request, template_name='cliente/cliente_watch.html', context={'cli': cli})


def cliente_edit(request, id):
    cli = Cliente.objects.get(id=id)

    if request.method == 'POST':
        cli.nombre = request.POST.get('Nombre')
        cli.apellido = request.POST.get('Apellido')
        cli.tipo = request.POST.get('Tipo')
        cli.direccion = request.POST.get('Direccion')
        cli.telefono = request.POST.get('Telefono')
        cli.email = request.POST.get('Email')
        cli.organizacion = request.POST.get('Organizacion')
        cli.dui = request.POST.get('Dui')
        cli.nit = request.POST.get('Nit')
        cli.save()
        return redirect('apiApp:cli_list')
    return render(request, template_name='cliente/cliente_edit.html', context={'cli': cli})


def cliente_delete(request, id):
    cli = Cliente.objects.get(id=id)

    if request.method == 'POST':
        cli.delete()
        return redirect('apiApp:cli_list')
    return render(request, template_name='cliente/cliente_delete.html', context={'cli': cli})