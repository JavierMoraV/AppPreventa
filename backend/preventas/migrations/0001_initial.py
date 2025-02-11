# Generated by Django 4.2 on 2024-05-08 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=13, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleIngenieria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_solicitante', models.CharField(max_length=100)),
                ('especialidad', models.CharField(choices=[('CLM', 'clima'), ('ENR', 'energia'), ('PCI', 'incendio'), ('SSMM', 'Soluciones Modulares'), ('MON', 'Monitoreo')], max_length=100)),
                ('revision', models.CharField(max_length=100)),
                ('alcance', models.TextField()),
                ('entregables', models.TextField()),
                ('info_requerida_mandante', models.TextField()),
                ('limitaciones', models.TextField()),
                ('exclusiones', models.TextField()),
                ('plazo_entrega', models.TextField()),
                ('costo', models.IntegerField()),
                ('firma', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100, null=True)),
                ('modelo', models.CharField(max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('formato', models.CharField(choices=[('unidad', 'unidad'), ('metros', 'metros'), ('kilos', 'kilos'), ('horas', 'horas')], max_length=100)),
                ('costo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Preventa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proyecto', models.CharField(max_length=100)),
                ('nombre_solicitante', models.CharField(max_length=100)),
                ('nombre_vertical', models.CharField(choices=[('estandar', 'Estandar'), ('zona_norte_antofagasta', 'Zona Norte Antofagasta'), ('data_center', 'Data Center'), ('mineria_y_utilities', 'Mineria y Utilities'), ('industrias', 'Industrias'), ('telecomunicaciones', 'Telecomunicaciones'), ('transporte_y_gobierno', 'Transporte y Gobierno')], max_length=50)),
                ('fecha', models.DateField()),
                ('correlativo', models.IntegerField()),
                ('id_cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='preventas.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('revisionItem', models.CharField(max_length=100, null=True)),
                ('id_detalle_ingenieria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preventas.detalleingenieria')),
                ('id_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preventas.item')),
            ],
        ),
        migrations.AddField(
            model_name='detalleingenieria',
            name='id_preventa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preventas.preventa'),
        ),
        migrations.AddField(
            model_name='detalleingenieria',
            name='usuario_teknica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
