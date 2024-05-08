from django.urls import path
from .views import add_cliente, show_clientes, add_preventa, get_vertical_options, preventa_list, get_especialidad_options, add_detalle_preventa, add_item, get_formato_options, show_items

urlpatterns = [
    path('add_cliente/', add_cliente, name='add_cliente'),
    path('show_clientes/', show_clientes, name='show_clientes'),
    path('show_items/', show_items, name='show_items'),
    path('add_preventa/', add_preventa, name='add_preventa'),
    path('get_vertical_options/', get_vertical_options, name='get_vertical_options'),
    path('get_especialidad_options/', get_especialidad_options, name='get_especialidad_options'),
    path('get_formato_options/', get_formato_options, name='get_formato_options'),
    path('preventa_list/', preventa_list, name='preventa_list'),
    path('add_detalle_preventa/', add_detalle_preventa, name='add_detalle_preventa'),
    path('add_item/', add_item, name='add_item'),
]
