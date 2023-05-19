# Generated by Django 4.1 on 2022-08-12 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insumos', '0008_alter_insumo_categoria_alter_insumo_unidad_medida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categorias', related_query_name='categoria', to='insumos.categoria', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='unidad_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='umedidas', related_query_name='unidmed', to='insumos.unidadmedida', verbose_name='Unidad Medida'),
        ),
    ]
