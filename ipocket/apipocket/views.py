from django.shortcuts import render, get_object_or_404, redirect
from .models import Ativo
from .forms import AtivoForm


def lista_ativos(request):
    ativos = Ativo.objects.all()
    return render(request, 'lista_ativos.html', {'ativos': ativos})


def detalhes_ativo(request, pk):
    ativo = get_object_or_404(Ativo, pk=pk)
    return render(request, 'detalhes_ativo.html', {'ativo': ativo})


def novo_ativo(request):
    if request.method == 'POST':
        form = AtivoForm(request.POST)
        if form.is_valid():
            ativo = form.save(commit=False)
            ativo.save()
            return redirect('lista_ativos')
    else:
        form = AtivoForm()
    return render(request, 'novo_ativo.html', {'form': form})


def editar_ativo(request, pk):

    ativo = get_object_or_404(Ativo, pk=pk)
    if request.method == 'POST':
        form = AtivoForm(request.POST, instance=ativo)
        if form.is_valid():
            form.save()
            return redirect('lista_ativos')
    else:
        form = AtivoForm(instance=ativo)
    return render(request, 'editar_ativo.html', {'form': form, 'ativo': ativo})


def excluir_ativo(request, pk):
    ativo = get_object_or_404(Ativo, pk=pk)
    ativo.delete()
    return redirect('lista_ativos')
