from __future__ import unicode_literals
import datetime

from django.db import models

class Link(models.Model):
    nombre = models.TextField(max_length=50, null=True)
    objetivo = models.TextField(max_length=50, null=True)
    link_destino = models.URLField()
    monitorizar_usr = models.BooleanField(default=True)
    clicks = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre

class Capturado(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    datetime = models.DateTimeField('Fecha de Acceso', default=datetime.datetime.now)
    ip_extra = models.TextField(null=True)
    meta = models.TextField(null=True)