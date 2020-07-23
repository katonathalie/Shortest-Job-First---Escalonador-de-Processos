from django.shortcuts import render, redirect
from .models import Processo
from .forms import CadastrarProcessoForm

def lista_pronto(request):
    template_name = 'lista_pronto.html'
    processos = Processo.objects.all()

    if request.method == 'POST':
        form = CadastrarProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pronto')
    else:
        form = CadastrarProcessoForm()

    return render(request, template_name, {'processos': processos, 'form': form})

def criar_processo(request):
    template_name = 'criar_processo.html'

    if request.method == 'POST':
        form = CadastrarProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            form = CadastrarProcessoForm()
    else:
        form = CadastrarProcessoForm()

    return render(request, template_name, {'form': form})