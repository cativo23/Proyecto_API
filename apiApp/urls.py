from django.urls import path, include
from .views import proveedor_create, proveedor_list, proveedor_edit, proveedor_delete, proveedor_watch, cliente_create, \
    cliente_list, cliente_watch, cliente_edit, cliente_delete, material_create, material_list, material_watch, \
    material_edit, material_delete, index, orden_create, orden, linea_create, linea_watch, linea_edit, linea_delete

app_name = 'apiApp'

urlpatterns = [
    path('index/', index, name='index'),

    # CRUD Proveedor
    path('pro_list/', proveedor_list, name='pro_list'),
    path('pro_create/', proveedor_create, name='pro_create'),
    path('pro_watch/<int:id>/', proveedor_watch, name='pro_watch'),
    path('pro_edit/<int:id>/', proveedor_edit, name='pro_edit'),
    path('pro_delete/<int:id>/', proveedor_delete, name='pro_delete'),

    # CRUD Cliente
    path('cli_list/', cliente_list, name='cli_list'),
    path('cli_create/', cliente_create, name='cli_create'),
    path('cli_watch/<int:id>/', cliente_watch, name='cli_watch'),
    path('cli_edit/<int:id>/', cliente_edit, name='cli_edit'),
    path('cli_delete/<int:id>/', cliente_delete, name='cli_delete'),

    # CRUD Producto


    # CRUD Material
    path('mat_list/', material_list, name='mat_list'),
    path('mat_create/', material_create, name='mat_create'),
    path('mat_watch/<int:id>/', material_watch, name='mat_watch'),
    path('mat_edit/<int:id>/', material_edit, name='mat_edit'),
    path('mat_delete/<int:id>/', material_delete, name='mat_delete'),

    # Orden
    path('ord/', orden, name='ord'),
    path('ord_create/', orden_create, name='ord_create'),

    # CRUD Linea
    path('lin_create/', linea_create, name='lin_create'),
    path('lin_watch/<int:id>/', linea_watch, name='lin_watch'),
    path('lin_edit/<int:id>/', linea_edit, name='lin_edit'),
    path('lin_delete/<int:id>/', linea_delete, name='lin_delete'),

]