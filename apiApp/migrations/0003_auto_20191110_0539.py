# Generated by Django 2.2.7 on 2019-11-10 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0002_cliente_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('express', models.BooleanField(default=False)),
                ('fecha_realizacion', models.DateTimeField()),
                ('fecha_entrega', models.DateTimeField()),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiApp.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('codigo', models.CharField(max_length=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.BooleanField(default=True)),
                ('materiales', models.ManyToManyField(to='apiApp.Material')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDeTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Orden', models.ManyToManyField(to='apiApp.Orden')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='producto',
            field=models.ManyToManyField(to='apiApp.producto'),
        ),
    ]
