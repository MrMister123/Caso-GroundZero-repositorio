# Generated by Django 4.1.2 on 2024-07-06 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='apellido_materno',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apellido_paterno',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nacimiento',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id_genero',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
    ]
