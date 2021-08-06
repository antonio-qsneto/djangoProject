from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField
import math

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    """def __str__(self):
        return "{}".format(self.nome)"""

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    proprietario = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    placa = models.CharField(max_length=7)
    cor   = models.CharField(max_length=15)
    observacoes = models.TextField()

    def __str__(self):
        return "{} {}".format(self.marca, self.placa)

class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return "Parametros Gerais"

class movRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        return math.ceil((self.checkout - self.checkin).total_seconds()/3600)

    def total(self):
        return self.valor_hora * self.horas_total()

    def __str__(self):
        return self.veiculo.placa

class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    inicio = models.DateField()
    valor_mensa = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return "{} - {} {}".format(self.veiculo.proprietario, self.veiculo, self.inicio)

class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.PROTECT)
    data_pag = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "{}: {} - {}".format(self.mensalista, self.data_pag, self.total)

    "VagaReserta created to build list to mensal users"
class VagaReservada(models.Model):
    pessoa = models.ForeignKey(Mensalista, on_delete=models.PROTECT)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.pessoa, self.veiculo)
