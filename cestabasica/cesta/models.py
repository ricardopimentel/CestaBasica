from django.db import models
from enum import Enum
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
# import datetime

# class categoria(models.Model):
#     nome = models.CharField(max_length=100)
#     datahora = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.nome
#
# class trasacao(models.Model):
#     data = models.DateTimeField()
#     descricao = models.CharField(max_length=100)
#     valor = models.DecimalField(max_digits=4, decimal_places=2)
#     categorias = models.ForeignKey(categoria, on_delete=models.CASCADE)
#     obs = models.TextField(null=True, blank=True)
#     def __str__(self):
#         return self.descricao

class estado(models.Model):
    nome = models.CharField(max_length=20)
    sigla = models.CharField(max_length=2)
    def __str__(self):
        return self.nome

class cidade(models.Model):
    nome = models.CharField(max_length=20)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class estabelecimento(models.Model):
    nome = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    cidade = models.ForeignKey(cidade, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class categoria(models.Model):
    nome = models.CharField(max_length=20)
    def __str__(self):
        return self.nome

class tipo(models.Model):
    nome = models.CharField(max_length=20)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class marca(models.Model):
    nome = models.CharField(max_length=20)
    def __str__(self):
        return self.nome

class unidadeMedida(models.Model):
    tipo = models.CharField(max_length=2)
    def __str__(self):
        return self.tipo

class produto(models.Model):
    nome = models.CharField(max_length=20)
    codbarras = models.CharField(max_length=20)
    quantidade = models.DecimalField(max_digits=8, decimal_places=6)
    marca = models.ForeignKey(marca, on_delete=models.CASCADE)
    tipo = models.ForeignKey(tipo, on_delete=models.CASCADE)
    unidadeMedida = models.ForeignKey(unidadeMedida, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome


class eventos(models.Model):
    mes = models.IntegerField(default=2)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.now().year)],
        help_text="Use the following format: <YYYY>")
    # YEAR_CHOICES = []
    # for r in range(1980, (datetime.datetime.now().year + 1)):
    #     YEAR_CHOICES.append((r, r))
    # year = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    # year = models.IntegerField(_('year'), choices=year_choices, default=current_year)
    # year = models.PositiveIntegerField(
    #         validators=[
    #             MinValueValidator(1900),
    #             MaxValueValidator(datetime.now().year)],
    #         help_text="Use the following format: <YYYY>")
    def __str__(self):
        return str(self.mes)+"/"+str(self.year)


class pesquisa_preco(models.Model):
    preco = models.DecimalField(max_digits=8, decimal_places=6)
    produto = models.ForeignKey(produto, on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(estabelecimento, on_delete=models.CASCADE)
    evento = models.ForeignKey(eventos, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.preco)