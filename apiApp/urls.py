from django.urls import path, include
from .views import prueba, proveedor_list

app_name = 'apiApp'

urlpatterns = [
    path('prueba/', prueba, name='prueba'),
    path('pro_list/', proveedor_list, name='pro_list'),
]