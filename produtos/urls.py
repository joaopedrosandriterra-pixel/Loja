from django.urls import path
from produtos import views

urlpatterns = [
    path("cadastro_produto/", views.cadastro_produto, name="cadastro_produto") #path(caminho da url; a view que ele chama;  nome da url)
]
