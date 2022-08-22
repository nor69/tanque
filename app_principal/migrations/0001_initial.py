# Generated by Django 4.0.6 on 2022-07-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('tipo', models.CharField(max_length=15, verbose_name='Tipo')),
                ('pais', models.CharField(max_length=20, verbose_name='Pais')),
                ('nivel', models.IntegerField(verbose_name='Nivel')),
                ('batallas', models.IntegerField(verbose_name='Batallas')),
                ('victorias', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Victorias')),
                ('experiencia', models.IntegerField(verbose_name='Experiencia')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Sub-Total')),
                ('win8', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Win8')),
                ('total', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Total')),
            ],
        ),
    ]