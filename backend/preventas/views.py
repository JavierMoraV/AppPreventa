from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClienteSerializerCreate, ClienteSerializerSelect, PreventaSerializerCreate, PreventaSerializerSelect, DetallesPreventasSerializerCreate, ItemSerializerCreate, ItemSerializerSelect
from django.http import JsonResponse
from .models import Cliente, Preventa, DetalleIngenieria, Item
from rest_framework import generics

@api_view(['POST'])
def add_cliente(request):
    if request.method == 'POST':
        serializer = ClienteSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def show_clientes(request):
    clientes = Cliente.objects.all()
    serializer = ClienteSerializerSelect(clientes, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def add_preventa(request):
    if request.method == 'POST':
        fecha = request.data.get('fecha')
        correlativo = int(request.data.get('correlativo'))
        usuario_teknica =  int(request.data.get('usuario_teknica'))
        id_cliente = int(request.data.get('id_cliente'))
        request.data['fecha'] = fecha
        request.data['correlativo'] = correlativo
        request.data['usuario_teknica'] = usuario_teknica
        request.data['id_cliente'] = id_cliente

        serializer = PreventaSerializerCreate(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_vertical_options(request):
    vertical_options = [{'key': option[0], 'value': option[1]} for option in Preventa.OPCIONES_ENUM]
    return JsonResponse(vertical_options, safe=False)



def capitalize_fields(data):
    for key, value in data.items():
        if isinstance(value, str):
            data[key] = value.capitalize()
    return data

def preventa_list(request):
    if request.method == 'GET':
        preventas = Preventa.objects.all()
        serializer = PreventaSerializerSelect(preventas, many=True)
        
        # Obtener los datos de clientes
        clientes = Cliente.objects.all()

        # Mapear las claves a los valores para nombre_vertical
        opciones = dict(Preventa.OPCIONES_ENUM)

        # Iterar sobre las preventas y agregar el nombre del cliente y el valor de nombre_vertical
        for preventa in serializer.data:
            cliente = clientes.filter(id=preventa['id_cliente']).first()
            preventa['nombre_cliente'] = cliente.nombre if cliente else 'Cliente no encontrado'

            # Obtener el valor correspondiente para nombre_vertical y capitalizarlo
            preventa['nombre_vertical'] = opciones.get(preventa['nombre_vertical'], 'Desconocido').capitalize()

            # Capitalizar todos los campos de texto
            preventa = capitalize_fields(preventa)

        return JsonResponse(serializer.data, safe=False)


def get_especialidad_options(request):
    especialidad_options = [{'key': option[0], 'value': option[1]} for option in DetalleIngenieria.OPCIONES_ENUM]
    return JsonResponse(especialidad_options, safe=False)

def get_formato_options(request):
    formato_options = [{'key': option[0], 'value': option[1]} for option in Item.OPCIONES_ENUM]
    return JsonResponse(formato_options, safe=False)


@api_view(['POST'])
def add_detalle_preventa(request):
    if request.method == 'POST':
        serializer = DetallesPreventasSerializerCreate(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            # Obtener el ID generado
            generated_id = instance.id
            # Crear un diccionario con los datos y el ID generado
            response_data = {
                'id': generated_id,
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def add_item(request):
    if request.method == 'POST':
        serializer = ItemSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def show_items(request):
    item = Item.objects.all()
    serializer = ItemSerializerSelect(item, many=True)
    return JsonResponse(serializer.data, safe=False)