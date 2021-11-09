from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
import hashlib
import re

# Create your views here.
def cadastro(request):
    status = request.GET.get('status')
    return render(request,'cadastro.html', {'status':status})

def login(request):
    status = request.GET.get('status')
    return render(request,'login.html', {'status':status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
   
    usuario = Usuario.objects.filter(email = email)
    
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=1')
    if len(senha) < 8 or len(senha) > 16:
        return redirect('/auth/cadastro/?status=2')
    if nome.strip() == 0 or email.strip() == 0:
        return redirect('/auth/cadastro/?status=3')
    if not re.fullmatch(regex, email):
        return redirect('/auth/cadastro/?status=4')
    try:
        senha = hashlib.sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=5')

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = hashlib.sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email).filter(senha=senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) >0:
        request.session['usuario'] = usuario[0].id
        return redirect('/home/')

def sair(request):
    request.session.flush()
    return redirect('/auth/login')