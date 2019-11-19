from django.db import models

# Create your models here.


class user(models.Model):
    nombre = models.CharField(max_length=30)


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    tipo = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    organizacion = models.CharField(max_length=50)
    dui = models.CharField(max_length=30)
    nit = models.CharField(max_length=30)


class proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=300)


class Material(models.Model):
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)


class producto(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    materiales = models.ManyToManyField(Material)


class Orden(models.Model):
    cantidad = models.IntegerField()
    express = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_realizacion = models.DateTimeField() 
    fecha_entrega = models.DateTimeField() 
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ManyToManyField(producto)


class OrdenDeTrabajo(models.Model):
    Orden = models.ManyToManyField(Orden)


