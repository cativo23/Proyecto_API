from django.shortcuts import render, redirect
from .models import proveedor, Cliente, producto, Material, Orden, Lineas
from django.core import serializers
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    return render(request, template_name='index.html')


# CRUD Proveedor
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


def proveedor_create(request):
    if request.method == 'POST':
        p = proveedor()
        p.nombre = request.POST.get('Nombre')
        p.direccion = request.POST.get('Direccion')
        p.telefono = request.POST.get('Telefono')
        p.descripcion = request.POST.get('Descripcion')
        p.save()
        return redirect('apiApp:pro_list')
    return render(request, template_name='proveedor/proveedor_create.html')


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


# CRUD Clientes
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, template_name='cliente/cliente_list.html', context={'clientes': clientes})


def cliente_create(request):
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
    return render(request, template_name='cliente/cliente_create.html')

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


# CRUD Productos


# CRUD Material
def material_list(request):
    materiales = Material.objects.all()
    pro = proveedor.objects.all()
    return render(request, template_name='material/material_list.html', context={'materiales': materiales, 'pro': pro})


def material_create(request):
    pro = proveedor.objects.all()
    if request.method == 'POST':
        m = Material()
        m.codigo = request.POST.get('Codigo')
        m.nombre = request.POST.get('Nombre')
        m.cantidad = request.POST.get('Cantidad')
        m.precio = request.POST.get('Precio')

        idproveedor = request.POST.get('Proveedor')
        m.proveedor = proveedor.objects.get(id=idproveedor)

        m.save()
        return redirect('apiApp:mat_list')
    return render(request, template_name='material/material_create.html', context={'pro': pro})


def material_watch(request, id):
    mat = Material.objects.get(id=id)
    return render(request, template_name='material/material_watch.html', context={'mat': mat})


def material_edit(request, id):
    mat = Material.objects.get(id=id)
    proveedores = proveedor.objects.all()

    if request.method == 'POST':
        mat.codigo = request.POST.get('Codigo')
        mat.nombre = request.POST.get('Nombre')
        mat.cantidad = request.POST.get('Cantidad')
        mat.precio = request.POST.get('Precio')

        idproveedor = request.POST.get('Proveedor')
        mat.proveedor = proveedor.objects.get(id=idproveedor)
        mat.save()
        return redirect('apiApp:mat_list')
    return render(request, template_name='material/material_edit.html', context={'mat': mat, 'proveedores':
        proveedores})


def material_delete(request, id):
    mat = Material.objects.get(id=id)

    if request.method == 'POST':
        mat.delete()
        return redirect('apiApp:mat_list')
    return render(request, template_name='material/material_delete.html', context={'mat': mat})


# Orden (Cotizacion)

def orden(request):
    clientes = Cliente.objects.all()
    clientes_js = serializers.serialize('json', clientes, fields=['nombre','apellido', 'organizacion',
                                                                  'telefono', 'email'])

    return HttpResponse(clientes_js, content_type='application/json')


def orden_create(request):
    hoy = datetime.date.today()
    numero = Orden.objects.count()
    orden = Orden.objects.last()
    lineas = Lineas.objects.filter(orden_id=orden.id)
    return render(request, template_name='orden/orden_create.html', context={'hoy': hoy, 'numero': numero, 'lineas': lineas})


# CRUD Lineas de orden
def linea_create(request):
    productos = producto.objects.filter(estado=True)

    if request.method == 'POST':
        linea = Lineas()

        idproducto = request.POST.get('Producto')
        linea.producto = producto.objects.get(id=idproducto)
        linea.cantidad = request.POST.get('Cantidad')

        cant = float(linea.cantidad)
        prec = float(linea.producto.precio)
        linea.subtotal = prec * cant
        # Al dar clic en agregar orden se debe crear la orden, y aqui buscamos la última orden
        o = Orden.objects.last()
        linea.orden = o
        linea.save()
        return redirect('apiApp:ord_create')
    return render(request, template_name='linea/linea_create.html', context={'productos': productos})


def linea_watch(request, id):
    lin= Lineas.objects.get(id=id)
    return render(request, template_name='linea/linea_watch.html', context={'lin': lin})


def linea_edit(request, id):
    lin = Lineas.objects.get(id=id)
    productos = producto.objects.filter(estado=True)

    if request.method == 'POST':
        idproducto = request.POST.get('Producto')
        lin.producto = producto.objects.get(id=idproducto)
        lin.cantidad = request.POST.get('Cantidad')

        cant = float(lin.cantidad)
        prec = float(lin.producto.precio)
        lin.subtotal = prec * cant

        lin.save()
        return redirect('apiApp:ord_create')
    return render(request, template_name='linea/linea_edit.html', context={'lin': lin, 'productos': productos})


def linea_delete(request, id):
    lin = Lineas.objects.get(id=id)

    if request.method == 'POST':
        lin.delete()
        return redirect('apiApp:ord_create')
    return render(request, template_name='linea/linea_delete.html', context={'lin': lin})
