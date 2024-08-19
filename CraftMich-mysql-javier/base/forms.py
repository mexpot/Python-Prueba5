from django import forms
from .models import Articulos,Contactos

class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ['imagen', 'ubicacion', 'categoria', 'producto', 'precio', 'descripcion']
        
from .models import Login

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = [
            'usuario',
            'nombre',
            'email',
            'password',
            'fecha',
            'roles',
        ]
class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = [
            'nombre',
            'correo',
            'mensaje',
            'avisos'

        ]
