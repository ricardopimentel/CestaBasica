from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login as login_auth, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import forms
from django.db.models import Q
from .models import *
from .form import *
# Create your views here.
def home(request):
    data = {}
    return render(request,'home.html', data)

def entrar(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        return redirect('/index')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('user')
        password = request.POST.get('pass')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login_auth(request, user)
            return redirect('/index')
        else:
            messages.error(request, "erro")
    return redirect('/login')

@login_required(login_url='/login')
def index(request):
    data = {}
    data['eventos'] = eventos.objects.all()
    return render(request, 'index.html', data)


@login_required(login_url='/login')
def dados(request, id):
    data = {}
    data['id'] = id;
    # data['eventos'] = pesquisa_preco.objects.filter(evento_id=id)
    data['eventos'] = tipo.objects.all()
    data['cat'] = categoria.objects.all()
    # return HttpResponse(data['eventos'])
    return render(request, 'data.html', data)

@login_required(login_url='/login')
def lista(request, id, pk):
    data = {}
    data['id'] = id;
    data['id2'] = pk;
    data['eventos'] = pesquisa_preco.objects.filter(Q(evento_id=pk) & Q(produto_id=id))
    # data['eventos'] = tipo.objects.all()
    # data['cat'] = categoria.objects.all()
    # return HttpResponse(data['eventos'])
    return render(request, 'lista.html', data)



@login_required(login_url='/login')
def updados(request, id, pk):
    data = {}
    data['id'] = pk;
    preco = pesquisa_preco.objects.get(id=id)
    form = PrecoForm(request.POST or None, instance=preco)
    if form.is_valid():
        form.save()
        # return redirect('/da')
        text = "/data/%s" %(pk)
        return redirect(text)
    data['form'] = form
    # return HttpResponse(form)
    return render(request, 'updata.html', data)

@login_required(login_url='/login')
def cadevento(request, id, pk):
    data = {}
    data['id'] = pk;
    # preco = pesquisa_preco.objects.get(id=id)
    form = PrecoFormCad(request.POST or None)
    if form.is_valid():
        form.save()
        # return redirect('/da')
        text = "/lista/%s/%s" %(id, pk)
        return redirect(text)
    data['form'] = form
    # form.initial['produto'] = id
    form.initial['evento'] = pk
    # form.fields['produto'].widget = forms.HiddenInput()
    form.fields['evento'].widget = forms.HiddenInput()
    # form.fields["produto"] = models.forms.ModelMultipleChoiceField(queryset=someData.objects.filter(tipo=id))
    form.fields['produto'] = forms.ModelChoiceField(produto.objects.filter(tipo_id=id))
    # return HttpResponse(form)
    return render(request, 'cadeventos.html', data)


def sair(request):
    logout(request)
    return redirect('/')