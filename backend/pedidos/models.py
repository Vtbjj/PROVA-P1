from django.db import models

from clientes.models import Cliente
from produtos.models import Produto


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='pedidos')
    quantidade = models.IntegerField(default=1)
    data_pedido = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pendente')

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"