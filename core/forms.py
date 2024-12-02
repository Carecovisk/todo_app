from django.forms import ModelForm
from core.models import Tarefa

class FormularioTarefa(ModelForm):

    class Meta:
        model = Tarefa
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
