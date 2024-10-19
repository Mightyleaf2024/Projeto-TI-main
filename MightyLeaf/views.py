from django.shortcuts import render

from django.contrib import messages

def home(request): #vai fazer uma requisição ao servidor
    return render(request,'home.html')#trazendo a pagina ao html
def log(request): #vai fazer uma requisição ao servidor
    return render(request,'log.html')#trazendo a pagina ao html
def plantas(request): #vai fazer uma requisição ao servidor
    return render(request,'plantas.html')#trazendo a pagina ao html
def redefsenha(request): #vai fazer uma requisição ao servidor
    return render(request,'redefsenha.html')#trazendo a pagina ao html
def cad(request): #vai fazer uma requisição ao servidor
    return render(request,'cad.html')#trazendo a pagina ao html
