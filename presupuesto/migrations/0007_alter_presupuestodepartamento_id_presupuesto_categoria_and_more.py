# Generated by Django 4.1 on 2022-11-21 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0006_remove_presupuestodepartamento_id_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuestodepartamento',
            name='id_presupuesto_categoria',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='presupuesto_dpto_categoria', to='presupuesto.presupuestocategoria', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='presupuestosubdepartamento',
            name='id_presupuesto_categoria',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='presupuesto_subdpto_categoria', to='presupuesto.presupuestocategoria', verbose_name='Categoría'),
        ),
    ]
