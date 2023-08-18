from django.db import models
from datetime import datetime
import json


class EtpOnline(models.Model):
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
    etp_vinculada = models.CharField(max_length=100, null=False, default='')
    oe_selec = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.etp_vinculada


class OtsDCI(models.Model):
    ots_id = models.CharField(max_length=100)
    num_ots = models.CharField(max_length=100)
    sigla = models.CharField(max_length=100)
    proprietario = models.CharField(max_length=100, null=True)
    etp_vinculada = models.CharField(max_length=100, null=False)
    ots_selec = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.etp_vinculada


class DciGerada(models.Model):

    OPCOES_TIPO_ENTREGA = [
        ("TOTAL", "Total"),
        ("PARCIAL", " Parcial"),
        ("FINAL", "Final"),
    ]

    etp_value = models.CharField(max_length=100)
    list_oes = models.TextField()
    list_ots = models.TextField()
    obv_atr = models.TextField(null=True)
    obv_oes = models.TextField(null=True)
    obv_rede_ext = models.TextField(null=True)
    topologia = models.CharField(max_length=150, default="", null=True)
    link = models.CharField(max_length=150, default="", null=True)
    obv_final = models.TextField(null=True)
    tipo_entrega = models.CharField(
        max_length=150, choices=OPCOES_TIPO_ENTREGA, default='')
    hora_geracao = models.DateTimeField(default=datetime.now)

    def gerar_lista_oes(self, lista):
        lista_seializada = json.dumps(lista)
        self.list_oes = lista_seializada

    def return_lista_oes(self):
        lista = json.loads(self.list_oes)
        return lista

    def gerar_lista_ots(self, lista):
        lista_seializada = json.dumps(lista)
        self.list_ots = lista_seializada

    def return_lista_ots(self):
        lista = json.loads(self.list_ots)
        return lista
