# Generated by Django 4.1 on 2022-11-28 14:43

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
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripción')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('ip_usuario', models.GenericIPAddressField(verbose_name='IP Usuario')),
                ('fecha_log', models.DateTimeField(auto_now=True, verbose_name='Fecha')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]