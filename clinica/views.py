from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Consulta
from rest_framework.response import Response
from .forms import ConsultaForm

def listar_medicos(request):
    medicos = Medico.objects.all()

    # query = request.GET.get('q')
    # livros = Livro.objects.none()

    return render(request, "clinica/listar_medicos.html", {'medicos': medicos})


def criar_consulta(request):
    if request.method == 'POST':
        form  = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return render('listar_medicos')
    else:
        form = ConsultaForm()

    return render(request, 'clinica/form_consultar.html', {'form': form})

def detalhes_consulta(request, id):
    consulta = Consulta.objects.filter(id=id)
    return render(request, "clinica/listar_consultas.html", {'consulta': consulta})