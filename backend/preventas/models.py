from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    rut = models.CharField(max_length=13, null=False, unique=True)
    def __str__(self):
        return self.nombre
    
class Preventa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=100, null=False)
    nombre_solicitante = models.CharField(max_length=100, null=False)
    OPCIONES_ENUM = [
        ('estandar', 'Estandar'),
        ('zona_norte_antofagasta', 'Zona Norte Antofagasta'),
        ('data_center', 'Data Center'),
        ('mineria_y_utilities', 'Mineria y Utilities'),
        ('industrias', 'Industrias'),
        ('telecomunicaciones', 'Telecomunicaciones'),
        ('transporte_y_gobierno', 'Transporte y Gobierno'),
    ]
    nombre_vertical = models.CharField(max_length=50, choices=OPCIONES_ENUM)
    fecha = models.DateField(null=False)
    correlativo = models.IntegerField(null=False)
    usuario_teknica = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.nombre_proyecto
    



class DetalleIngenieria(models.Model):
    id = models.AutoField(primary_key=True)
    id_preventa = models.ForeignKey(Preventa, on_delete=models.CASCADE, null=False)
    usuario_teknica = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    OPCIONES_ENUM = [
        ('CLM', 'clima'),
        ('ENR', 'energia'),
        ('PCI', 'incendio'),
        ('SSMM', 'Soluciones Modulares'),
        ('MON', 'Monitoreo'),
    ]
    nombre_solicitante = models.CharField(max_length=100, null=False)
    especialidad = models.CharField(max_length=100, choices=OPCIONES_ENUM)
    revision = models.CharField(max_length=100, null=False)
    alcance = models.TextField()
    entregables = models.TextField()
    info_requerida_mandante = models.TextField()
    limitaciones = models.TextField()
    exclusiones = models.TextField()
    plazo_entrega = models.TextField()
    costo = models.IntegerField(null=False)
    firma = models.CharField(max_length=100, null=False)
    def __str__(self) -> str:
        return self.alcance
    
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    marca = models.CharField(max_length=100, null=True,)
    modelo = models.CharField(max_length=100, null=True,)
    descripcion = models.CharField(max_length=100, null=True)
    OPCIONES_ENUM = [
        ('unidad', 'unidad'),
        ('metros', 'metros'),
        ('kilos', 'kilos'),
        ('horas', 'horas')
    ]
    formato = models.CharField(max_length=100, choices=OPCIONES_ENUM)
    costo = models.IntegerField(null=False)

class DetalleItem(models.Model):
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    id_detalle_ingenieria = models.ForeignKey(DetalleIngenieria, on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField(null=False)
    revisionItem = models.CharField(max_length=100, null=True)
