# Generated by Django 4.0.6 on 2022-08-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0004_alter_estadistica_victorias_alter_estadistica_win8'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadistica',
            name='subtotal',
            field=models.FloatField(blank=True, default=0, verbose_name='Subtotal'),
        ),
        migrations.AddField(
            model_name='estadistica',
            name='total',
            field=models.FloatField(blank=True, default=0, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='estadistica',
            name='victorias',
            field=models.FloatField(verbose_name='Victorias'),
        ),
        migrations.AlterField(
            model_name='estadistica',
            name='win8',
            field=models.FloatField(verbose_name='Win8'),
        ),
    ]
