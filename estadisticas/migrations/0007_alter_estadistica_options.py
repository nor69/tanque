# Generated by Django 4.0.6 on 2022-08-13 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0006_alter_estadistica_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estadistica',
            options={'ordering': ['nivel']},
        ),
    ]
