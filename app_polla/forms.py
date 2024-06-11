from django import forms
from .models import Marcador

class MarcadorForm(forms.ModelForm):
    class Meta:
        model = Marcador
        fields = ['nro_partido', 'marcador1', 'marcador2']
        
        labels = {
            'nro_partido': 'Partido',
            'marcador1': 'Equipo1',
            'marcador2': 'Equipo2'
        }
        
        
        
    
    