# Generated by Django 4.2.9 on 2024-01-20 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['-id'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]