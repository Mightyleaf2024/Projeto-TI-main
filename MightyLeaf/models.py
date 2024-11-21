from django.db import models

class Cliente(models.Model):
    id = models.IPAddressField
    nome = models.CharField('Nome do Cliente', max_length=100)
    data_nascimeto = models.DateField('Data nascimento',blank=False)
    email = models.EmailField('E-mail',max_length=100,blank=False, unique = True)

    def __str__(self):
        return self.cpf
