from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(user)
admin.site.register(proveedor)
admin.site.register(Cliente)
admin.site.register(OrdenDeTrabajo)
admin.site.register(Orden)
admin.site.register(producto)
admin.site.register(Material)
