from django.db import models

class Cliente(models.Model):
    cpf = models.BigIntegerField('CPF', primary_key=True, unique=True)
    nome = models.CharField('Nome do Cliente', max_length=100)
    data_nascimeto = models.DateField('Data nascimento',blank=False)
    email = models.EmailField('E-mail',max_length=100,blank=False, unique = True)
    telefonte = models.BigIntegerField('telefone',blank=False,help_text='inserir numero com DDD')

    def __str__(self):
        return self.cpf
