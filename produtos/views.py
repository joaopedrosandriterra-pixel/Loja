from django.shortcuts import render, redirect
from .forms import ProdutoForm
from django.contrib import messages


def cadastro_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('cadastro_produto')  # Redireciona para a página inicial após o cadastro

    else:
        form = ProdutoForm()

    return render(request, 'produtos/cadastro_produto.html', {'form': form})