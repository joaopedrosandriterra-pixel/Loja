from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=5000)
#   imagem = models.ImageField(upload_to='produtos/')
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome
