from email.policy import default
from tabnanny import verbose
from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField("Criado", auto_now_add=True)
    update_at = models.DateTimeField("Atualizado", auto_now_add=True)
    disponivel = models.BooleanField("Status", default=True)
    class Meta:
        abstract = True

class Conta(Base):
    nome = models.CharField("Nome", max_length=225, null=False, blank=False)
    valor = models.FloatField("Valor")
    descricao = models.TextField("Descrição", null=True, blank=True)

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

    def __str__(self) -> str:
        return "{} - R${} - {}".format(self.nome, self.valor, self.descricao)    
