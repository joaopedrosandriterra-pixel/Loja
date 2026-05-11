from django.shortcuts import render
from produtos.models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home/home.html', {'produtos': produtos})