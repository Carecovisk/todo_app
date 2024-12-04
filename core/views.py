from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.core.exceptions import ObjectDoesNotExist
from core.models import Tarefa
from core.forms import FormularioTarefa
from django.http import FileResponse, Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from core.serializers import SerializadorTarefas
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class ListarTarefas(LoginRequiredMixin, ListView):
    model = Tarefa
    context_object_name = 'tarefas'
    template_name = 'todo/listar_tarefas.html'

class CriarTarefa(LoginRequiredMixin, CreateView):
    model =Tarefa
    form_class = FormularioTarefa
    template_name = 'todo/criar_tarefas.html'
    success_url = reverse_lazy('listar-tarefas')


class EditarTarefa( LoginRequiredMixin, UpdateView):
    model =Tarefa
    form_class = FormularioTarefa
    template_name = 'todo/editar_tarefas.html'
    success_url = reverse_lazy('listar-tarefas')

class DeletarTarefa(LoginRequiredMixin, DeleteView):
    model = Tarefa
    template_name = 'todo/deletar_tarefas.html'
    success_url = reverse_lazy('listar-tarefas')


class VerTarefa(LoginRequiredMixin, View):

    def get(self, request, pk):
        tarefa = Tarefa.objects.get(pk=pk)
        return render(request, 'todo/ver_tarefas.html', {'tarefa': tarefa})
    
    def post(self, request, pk):
        tarefa = Tarefa.objects.get(pk=pk)
        tarefa.feito = not tarefa.feito
        tarefa.save()
        isFeita = tarefa.feito
        return render(request, 'todo/ver_tarefas.html', {'tarefa': tarefa, 'isFeita': isFeita})


class APIListarTarefas(ListAPIView):
    serializer_class = SerializadorTarefas
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.all()

class APIDeleteTarefas(DestroyAPIView):
    serializer_class = SerializadorTarefas
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.all()

class APICriarTarefas(CreateAPIView):
    serializer_class = SerializadorTarefas
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.all()

class APIEditarTarefas(UpdateAPIView):
    serializer_class = SerializadorTarefas
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.all()


def getAppImages(request, arquivo):
    try:
        tarefa = Tarefa.objects.get(foto=f"images/{arquivo}")
        return FileResponse(tarefa.foto)
    except ObjectDoesNotExist:
        raise Http404("Imagem não encontrada")
