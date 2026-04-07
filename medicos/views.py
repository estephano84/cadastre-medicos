from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Medico
from .forms import MedicoForm



def home(request): 
    return render(request, 'medicos/home.html')

def cadastrar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = MedicoForm()

    return render(request,'medicos/cadastrar.html',{'form': form})

def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request,'medicos/listar.html',{'medicos': medicos})

def editar(request, id):
    medico = get_object_or_404(Medico ,id=id)
    
    if request.method == 'POST':
        medico.nome = request.POST.get('nome')
        medico.especialidade = request.POST.get('especialidade')
        medico.crm = request.POST.get('crm')
        medico.telefone = request.POST.get('telefone')
        medico.email = request.POST.get('email')
        medico.save()
        return redirect('listar')
    
    return render(request,'medicos/editar.html',{'medico': medico})

def excluir(request, id):
    medico = get_object_or_404(Medico, id=id)
    medico.delete()
    return redirect ('listar')

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect ('/') 
    else:
        form = AuthenticationForm()
    
    return render(request, 'medicos/login.html',{'form': form})

def logout_usuario(request):
    logout(request)
    return redirect ('/')








    
