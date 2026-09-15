from django.db import models


class Cliente(models.Model):
	nome = models.CharField(max_length=150)
	email = models.EmailField(unique=True)
	telefone = models.CharField(max_length=20)
	data_cadastro = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.nome
