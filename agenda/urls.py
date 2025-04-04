from django.urls import path
from . import views

urlpatterns = [
    path('api/servicos/', views.listar_servico),
    path('api/servicos/', views.criar_servico),
    path('api/servicos/<int:id>/', views.detalhe_servico),
    path('api/agendamentos/', views.listar_agendamento),
    path('api/agendamentos/', views.criar_agendamento),
    path('api/agendamentos/<int:id>/', views.detalhe_agendamento)
]