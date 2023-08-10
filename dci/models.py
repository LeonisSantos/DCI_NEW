from django.db import models


class DciOnline(models.Model):
    etp = models.CharField(max_length=100, null=False)
    titulo = models.CharField(max_length=200, null=False)
    elaborador = models.CharField(max_length=100, null=False)
    demanda = models.CharField(max_length=100, null=False)
    motivador = models.CharField(max_length=100, null=False)
    vendor = models.CharField(max_length=100, null=False)
    tipoEtp = models.CharField(
        max_length=150, blank=False, null=False, default="")
    descri_etp = models.CharField(
        max_length=100, blank=False, null=False, default="")
    objetivo = models.CharField(
        max_length=100, blank=False, null=False, default="")

    def __str__(self) -> str:
        return self.titulo


class OesDci(models.Model):
    oe_id = models.CharField(max_length=100, null=False)
    num_oe = models.CharField(max_length=100, null=False)
    tipo_oe = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=150, null=False)
