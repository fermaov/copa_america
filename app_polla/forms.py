from django import forms
from .models import Marcador, ViewMarcador
from django.contrib.auth import get_user_model

User = get_user_model()

class MarcadorForm(forms.ModelForm):
    class Meta:
        model = Marcador
        fields = ['nro_partido', 'marcador1', 'marcador2']
        
        labels = {
            'nro_partido': 'Partido',
            'marcador1': 'Equipo1',
            'marcador2': 'Equipo2'
        }
        
class CambiarContrasenaForm(forms.ModelForm):
    """Formulario para cambiar la contraseña del usuario."""
    contrasena_actual = forms.CharField(
        label="Contraseña actual",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
    )
    nueva_contrasena1 = forms.CharField(
        label="Nueva contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
    )
    nueva_contrasena2 = forms.CharField(
        label="Confirmar nueva contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
    )

    def clean_contrasena_actual(self):
        """Validar la contraseña actual."""
        contrasena_actual = self.cleaned_data.get('contrasena_actual')
        usuario = self.request.user
        if not usuario.check_password(contrasena_actual):
            raise forms.ValidationError("Contraseña actual incorrecta.")
        return contrasena_actual

    def clean_nueva_contrasena2(self):
        """Validar la confirmación de la nueva contraseña."""
        nueva_contrasena1 = self.cleaned_data.get('nueva_contrasena1')
        nueva_contrasena2 = self.cleaned_data.get('nueva_contrasena2')
        if nueva_contrasena1 != nueva_contrasena2:
            raise forms.ValidationError("Las contraseñas nuevas no coinciden.")
        return nueva_contrasena2

    def save(self, commit=True):
        """Actualizar la contraseña del usuario."""
        usuario = self.request.user
        usuario.set_password(self.cleaned_data['nueva_contrasena1'])
        if commit:
            usuario.save()
        return usuario        
        
    
    