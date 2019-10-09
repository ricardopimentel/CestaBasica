from django.db import models
from enum import Enum
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

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
    quantidade = models.DecimalField(max_digits=8, decimal_places=3)
    cestabasica = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='static/img/', default='static/img/cart.png')
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
    quantidade = models.DecimalField(max_digits=8, decimal_places=3)
    marca = models.ForeignKey(marca, on_delete=models.CASCADE)
    tipo = models.ForeignKey(tipo, on_delete=models.CASCADE)
    unidadeMedida = models.ForeignKey(unidadeMedida, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.tipo) + " "+ str(self.marca)+ " "+ str(self.quantidade)+ " "+ str(self.unidadeMedida)

class evento(models.Model):
    mes = models.IntegerField(default=2)
    ano = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1990),
            MaxValueValidator(datetime.now().year)],
        help_text="Use the following format: <YYYY>")
    def __str__(self):
        return str(self.mes)+"/"+str(self.ano)

class pesquisa_preco(models.Model):
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    produto = models.ForeignKey(produto, on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(estabelecimento, on_delete=models.CASCADE)
    evento = models.ForeignKey(evento, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.produto) +"  "+str(self.estabelecimento)+"   "+str(self.preco)