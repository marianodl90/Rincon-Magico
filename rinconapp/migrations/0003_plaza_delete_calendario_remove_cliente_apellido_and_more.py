# Generated by Django 5.2.1 on 2025-05-21 05:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rinconapp', '0002_calendario_alter_cliente_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plaza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.DateField()),
                ('descripcion', models.TimeField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Calendario',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='seña',
        ),
        migrations.AddField(
            model_name='reserva',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rinconapp.cliente'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='ddireccion_evento',
            field=models.CharField(default='Por definir', max_length=255),
        ),
        migrations.AddField(
            model_name='reserva',
            name='fecha_evento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reserva',
            name='hora_evento',
            field=models.TimeField(default='12:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='plaza',
            field=models.ForeignKey(default='Sin dirección', on_delete=django.db.models.deletion.CASCADE, to='rinconapp.plaza'),
        ),
    ]
