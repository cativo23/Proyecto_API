from django.urls import path, include
from .views import proveedor_list, proveedor_edit, proveedor_delete, proveedor_watch, cliente_list, cliente_watch, \
    cliente_edit, cliente_delete, index

app_name = 'apiApp'

urlpatterns = [
    path('', index, name='index'),

    path('pro_list/', proveedor_list, name='pro_list'),
    path('pro_watch/<int:id>/', proveedor_watch, name='pro_watch'),
    path('pro_edit/<int:id>/', proveedor_edit, name='pro_edit'),
    path('pro_delete/<int:id>/', proveedor_delete, name='pro_delete'),


    path('cli_list/', cliente_list, name='cli_list'),
    path('cli_watch/<int:id>/', cliente_watch, name='cli_watch'),
    path('cli_edit/<int:id>/', cliente_edit, name='cli_edit'),
    path('cli_delete/<int:id>/', cliente_delete, name='cli_delete'),


]