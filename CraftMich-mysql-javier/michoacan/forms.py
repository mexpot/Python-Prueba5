from django import forms
from .models import CrearEvento,Eventos

class CrearEventoForm(forms.ModelForm):
    class Meta:
        model = CrearEvento
        fields = ['nombre','fecha','hora','lugar','tipo','descripcion','image']
        
class EventosForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['imagen', 'evento', 'precio', 'descripcion']

