from rest_framework import serializers
from .models import Cliente, Preventa, DetalleIngenieria, Item, User

class ClienteSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'rut']

class ClienteSerializerSelect(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'rut']

class PreventaSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Preventa
        fields = ['nombre_proyecto', 'nombre_solicitante', 'nombre_vertical', 'fecha', 'correlativo', 'usuario_teknica', 'id_cliente']

class PreventaSerializerSelect(serializers.ModelSerializer):
    class Meta:
        model = Preventa
        fields = ['id', 'nombre_proyecto', 'nombre_solicitante', 'nombre_vertical', 'fecha', 'correlativo', 'id_cliente']

class DetallesPreventasSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = DetalleIngenieria
        fields = ['id_preventa', 'usuario_teknica', 'especialidad', 'nombre_solicitante', 'revision', 'alcance', 'entregables', 'info_requerida_mandante', 'limitaciones', 'exclusiones', 'plazo_entrega', 'costo', 'firma']

class ItemSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['nombre','marca','modelo','descripcion','formato','costo']

class ItemSerializerSelect(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','nombre','marca','modelo','descripcion','formato','costo']

