# Generated by Django 4.0.6 on 2022-08-16 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0015_alter_estadistica_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estadistica',
            options={'ordering': ['experiencia']},
        ),
        migrations.AddField(
            model_name='estadistica',
            name='subtotal',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Subtotal'),
        ),
    ]