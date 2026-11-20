from django.urls import path
from .import views

urlpatterns = [
    path("", views.entrar, name="login"),
    path("sair/", views.sair, name="sair"),
    path("principal/", views.principal, name="principal"),
    path("clientes/", views.clientes, name="clientes"),
    path("clientes/novo/", views.cliente_novo, name="cliente_novo"),
    path("clientes/<int:id>/editar/", views.cliente_editar, name="cliente_editar"),
    path("aparelhos/", views.aparelhos, name="aparelhos"),
    path("aparelhos/novo/", views.aparelho_novo, name="aparelho_novo"),
    path("agendamentos/", views.agendamentos, name="agendamentos"),
    path("agendamentos/novo/", views.agendamento_novo, name="agendamento_novo"),
    path("agendamentos/<int:id>/data/", views.agendamento_data, name="agendamento_data"),

]

Ask AI
