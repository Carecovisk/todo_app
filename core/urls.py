from django.urls import path, include
from core import views
urlpatterns = [
    path('', views.ListarTarefas.as_view(), name='listar-tarefas'),
    path('images/<str:arquivo>/', views.getAppImages, name='carregar_imagem')
]