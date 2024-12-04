from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from core.models import Tarefa

class SerializadorTarefas(serializers.ModelSerializer):
    
    foto = Base64ImageField(required=False, represent_in_base64=True)

    class Meta:
        model = Tarefa
        exclude = []