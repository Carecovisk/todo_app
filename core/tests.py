from django.test import TestCase
from django.urls import reverse
from core.models import Tarefa
from django.contrib.auth.models import User
from core.forms import FormularioTarefa

# Create your tests here.

class TestesModelTarefas(TestCase):

    def setUp(self) -> None:
        self.tarefa_test = Tarefa(
            titulo="Titulo qualquer",
            descricao="Essa é uma descricão bem descritiva.",
        )
    
    def test_estado_padrao(self):
        self.assertFalse(self.tarefa_test.feito)


class TestesViewListarTarefas(TestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='teste',
            password='12345@teste'
        )
        self.client.force_login(self.user)
        self.url = reverse('listar-tarefas')
        self.tarefa_test = Tarefa(
            titulo="Titulo qualquer",
            descricao="Essa é uma descricão bem descritiva.",
        ).save()
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get('tarefas')), 1)

class TesteViewCriarTarefa(TestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create(username='testando', password='12345teste')
        self.client.force_login(self.user)
        self.url = reverse('criar-tarefas')
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioTarefa)
    
    def test_post(self):
        data = {'titulo': 'Criando novos caminhos', 'descricao': 'A vida é bela, as vezes.'}
        response = self.client.post(self.url, data)


        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-tarefas'))


        self.assertEqual(Tarefa.objects.count(), 1)
        self.assertEqual(Tarefa.objects.first().titulo,'Criando novos caminhos' )

class TesteViewEditarVeiculo(TestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create(username='test', password='12345@teste')
        self.client.force_login(self.user)
        self.instancia = Tarefa.objects.create(titulo='Um bom titulo', descricao='Uma boa descricao')
        self.url = reverse('editar-tarefas', kwargs={'pk' : self.instancia.pk})
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Tarefa)
        self.assertIsInstance(response.context.get('form'), FormularioTarefa)
        self.assertEqual(response.context.get('object').titulo, 'Um bom titulo')
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)

    
    def test_post(self):
        data = {'titulo':'Um titulo melhor', 'descricao':'Uma descrição melhor ainda'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-tarefas'))
        self.assertEqual(Tarefa.objects.count(), 1)
        self.assertEqual(Tarefa.objects.first().pk , self.instancia.pk)
        self.assertEqual(Tarefa.objects.first().titulo, data['titulo'])

class TesteViewDeletarVeiculo(TestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create(username='test', password='12345@teste')
        self.client.force_login(self.user)
        self.instancia = Tarefa.objects.create(titulo='Um bom titulo', descricao='Uma boa descricao')
        self.url = reverse('deletar-tarefas', kwargs={'pk' : self.instancia.pk})
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Tarefa)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)
    
    def test_post(self):
        count = Tarefa.objects.count()
        pk = self.instancia.pk
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tarefa.objects.count(), count - 1)
        self.assertRaises(Tarefa.DoesNotExist, Tarefa.objects.get, pk=pk)

        