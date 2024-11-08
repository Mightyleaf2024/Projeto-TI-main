from django import forms        

from .models import Cliente

class ClienteModelForm(forms.ModelsForm):
    class Meta:
        model = Cliente
        fields = ['cpf','nome','date_nascimento','email', 'telefone']
