from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from core.models import Tarefa
from django.http import FileResponse, Http404
import requests

# Create your views here.

# def index(request):

    # url = 'https://api.unsplash.com/'

    # headers = {
    #     "Authorization": "Client-ID nE-MSKc9z0VxQLNv6bnlSnpjhwbSEgQb_vbTEpAA81U",
    #     "Content-Type": "application/json",
    #     "Accept": "application/json"
    # }
    # response = requests.get(url + '/photos/random', headers=headers)

    # if response.status_code == 200:
    #     json = response.json()
    #     context = {'image_url': json['urls']['regular'], 'descricao': 'Imagem motivacional'}
    # else:
    #     print(response.json())
    #     context = {'descricao': 'imagem não pôde ser carregada'}
    # context = {'nums': list(range(5))}

    # return render(request, 'todo/listar_tarefas.html', context)

class ListarTarefas(ListView):
    model = Tarefa
    context_object_name = 'tarefas'
    template_name = 'todo/listar_tarefas.html'

def getAppImages(request, arquivo):
    try:
        tarefa = Tarefa.objects.get(foto=f"core/fotos/{arquivo}")
        return FileResponse(tarefa.foto)
    except ObjectDoesNotExist:
        raise Http404("Imagem não encontrada")
