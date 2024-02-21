from django.db import models


class Ativo(models.Model):
    name = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
