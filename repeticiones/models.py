from django.db import models


class Repeticione(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo = models.CharField(max_length=15, verbose_name="Tipo")
    pais = models.CharField(max_length=20, verbose_name="Pais")
    nivel = models.IntegerField(verbose_name="Nivel")
    destruidos = models.IntegerField(verbose_name="Destruidos")
    causado = models.IntegerField(verbose_name="Daño Causado")
    bloqueado = models.IntegerField(verbose_name="Daño Bloqueado")
    detectado = models.IntegerField(verbose_name="Daño Detectado")
    aturdimiento = models.IntegerField(verbose_name="Daño Aturdimiento")
    video = models.FileField(verbose_name="Video", upload_to='repeticiones')
    premium = models.BooleanField(default=False)

    class Meta:
        ordering = ['nivel']
