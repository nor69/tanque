# Generated by Django 4.0.6 on 2022-08-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_principal', '0002_delete_estadistica'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual', models.IntegerField()),
                ('mejor', models.IntegerField()),
                ('peor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Win8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual', models.IntegerField()),
                ('mejor', models.IntegerField()),
                ('peor', models.IntegerField()),
            ],
        ),
    ]