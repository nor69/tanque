from django.db import models


class Ranking(models.Model):
    actual = models.IntegerField()
    mejor = models.IntegerField()
    peor = models.IntegerField()


class Win8(models.Model):
    actual = models.FloatField()
    mejor = models.FloatField()
    peor = models.FloatField()


class Tanque(models.Model):
    numero = models.IntegerField()
