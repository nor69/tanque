# Generated by Django 4.0.6 on 2022-08-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0017_alter_estadistica_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadistica',
            name='subtotal',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Subtotal'),
        ),
        migrations.AddField(
            model_name='estadistica',
            name='total',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Total'),
        ),
    ]
