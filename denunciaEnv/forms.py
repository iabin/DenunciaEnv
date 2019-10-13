from denunciaEnv.models import Evento
from django.forms import ModelForm
class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
