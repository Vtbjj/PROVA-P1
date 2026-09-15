from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome