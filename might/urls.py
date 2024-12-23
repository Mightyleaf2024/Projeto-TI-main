"""
URL configuration for might project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MightyLeaf import views
from MightyLeaf.views import home,login,plantas,redefsenha,cadastro,teste,conta,Vconta


urlpatterns = [
    path('', home, name='home'),
    path('plantas/', plantas, name='plantas'),
    path('redefsenha/', redefsenha, name='redefsenha'),
    path('cad/', cadastro, name='cadastro'),
    path('teste/', teste, name='teste'),
    path('log/', login, name='login'),
    path('conta/', conta,name='conta'),
    path('Vconta/', Vconta,name='Vconta'),
]