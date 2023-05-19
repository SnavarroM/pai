# Generated by Django 4.1 on 2022-09-22 21:19

from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_usercargo_id_cargo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id_perfil',
            field=models.ForeignKey(default=user.models.Perfil.get_default_Perfil, on_delete=django.db.models.deletion.PROTECT, to='user.perfil', verbose_name='Perfil'),
        ),
    ]
