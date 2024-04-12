# Generated by Django 4.2.6 on 2024-04-12 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=60, verbose_name='Nombre Categoria')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('celular', models.IntegerField(verbose_name='Celular')),
                ('nit', models.CharField(max_length=25, verbose_name='NIT')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descuento', models.FloatField(verbose_name='Descuento')),
                ('sub_total', models.FloatField(verbose_name='Sub Total')),
                ('total_compra', models.FloatField(verbose_name='Total de Compra')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.cliente')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=100)),
                ('celular', models.IntegerField()),
                ('nit', models.CharField(max_length=25)),
                ('pagina_web', models.CharField(max_length=150)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre producto')),
                ('precio', models.FloatField(blank=True, help_text='Campo Opcional', null=True, verbose_name='Precio')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('imagen', models.ImageField(upload_to='img_productos', verbose_name='Imagen')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_orden', models.CharField(max_length=25, verbose_name='Código de Orden')),
                ('descuento', models.FloatField(verbose_name='Descuento')),
                ('sub_total', models.FloatField(verbose_name='Sub Total')),
                ('total', models.FloatField(verbose_name='Total')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.proveedor')),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
            },
        ),
        migrations.CreateModel(
            name='FacturaCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('sub_total', models.FloatField(verbose_name='Sub Total')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
                ('id_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.compra')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.producto')),
            ],
            options={
                'verbose_name': 'FacturaCompra',
                'verbose_name_plural': 'FacturaCompras',
            },
        ),
    ]
