# Generated by Django 4.0.6 on 2022-08-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0004_alter_win8_actual_alter_win8_mejor_alter_win8_peor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tanques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
            ],
        ),
    ]
