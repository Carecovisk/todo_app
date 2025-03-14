from django.urls import path
from core import views

urlpatterns = [
    path('', views.ListarTarefas.as_view(), name='listar-tarefas'),
    path('images/<str:arquivo>/', views.getAppImages, name='carregar_imagem'),
    path('criar/', views.CriarTarefa.as_view(), name='criar-tarefas'),
    path('deletar/<int:pk>/', views.DeletarTarefa.as_view(), name='deletar-tarefas'),
    path('editar/<int:pk>/', views.EditarTarefa.as_view(), name='editar-tarefas'),
    path('ver/<int:pk>/', views.VerTarefa.as_view(), name='ver-tarefas'),

    path('api/listar/', views.APIListarTarefas.as_view()),
    path('api/criar/', views.APICriarTarefas.as_view()),
    path('api/deletar/<int:pk>/', views.APIDeleteTarefas.as_view()),
    path('api/editar/<int:pk>/', views.APIEditarTarefas.as_view()),
]



