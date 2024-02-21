from django.urls import path
from .views import lista_ativos, detalhes_ativo, novo_ativo, editar_ativo, excluir_ativo

urlpatterns = [
    path('ativos/', lista_ativos, name='lista_ativos'),
    path('ativos/<int:pk>/', detalhes_ativo, name='detalhes_ativo'),
    path('ativos/novo/', novo_ativo, name='novo_ativo'),
    path('ativos/editar/<int:pk>/', editar_ativo, name='editar_ativo'),
    path('ativos/excluir/<int:pk>/', excluir_ativo, name='excluir_ativo'),
]
