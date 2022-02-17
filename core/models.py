from django.db import models

# Create your models here.

class Contato(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    nome = models.CharField('Nome', max_length=150)
    email = models.CharField('Email', max_length=150)
    mensagem = models.TextField('Mensagem', max_length=400)

    class Meta:
        verbose_name = ('Contato')
        verbose_name_plural = ('Contatos')