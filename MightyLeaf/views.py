from django.shortcuts import render

from django.contrib import messages

def home(request): 
    return render(request,'home.html')
def log(request): 
    return render(request,'log.html')
def plantas(request): 
    return render(request,'plantas.html')
def redefsenha(request): 
    return render(request,'redefsenha.html')
def cad(request): 
    return render(request,'cad.html')
def teste(request): 
    return render(request,'teste.html')