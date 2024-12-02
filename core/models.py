from django.db import models
import os
# Create your models here.

class Tarefa(models.Model):

    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=512)
    foto = models.ImageField(blank=True, null=True, upload_to='core/fotos')
    feito = models.BooleanField(default=False)

    def nome_foto(self):
        return os.path.basename(self.foto.url)