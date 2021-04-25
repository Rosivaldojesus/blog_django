from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categoria"

    def __str__(self):
        return "`{}".format(self.nome_categoria)