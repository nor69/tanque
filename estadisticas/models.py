from django.db import models


class Estadistica(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo = models.CharField(max_length=15, verbose_name="Tipo")
    pais = models.CharField(max_length=20, verbose_name="Pais")
    nivel = models.IntegerField(verbose_name="Nivel")
    batallas = models.IntegerField(verbose_name="Batallas")
    victorias = models.FloatField(verbose_name="Victorias")
    experiencia = models.IntegerField(verbose_name="Experiencia")
    win8 = models.FloatField(verbose_name="Win8")
    subtotal = models.FloatField(
        verbose_name="Subtotal", blank=True, null=True, default=0)
    total = models.FloatField(verbose_name="Total",
                              blank=True, null=True, default=0)
    garaje = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)

    class Meta:
        ordering = ['nivel']
