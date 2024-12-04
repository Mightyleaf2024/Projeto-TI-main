
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request): 
    return render(request,'home.html')
def plantas(request): 
    return render(request,'plantas.html')
def redefsenha(request): 
    return render(request,'redefsenha.html')
def teste(request): 
    return render(request,'teste.html')
def conta(request): 
    return render(request,'conta.html')
def Vconta(request): 
    return render(request,'Vconta.html')

def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existente')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Cadastrado')
                return redirect('login')
        else:
            messages.error(request, 'As senhas não são iguais')

    return render(request, 'cad.html')

def loguin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            messages.error(request, 'Usuário ou senha incorretos!')

    return render(request, 'log.html')