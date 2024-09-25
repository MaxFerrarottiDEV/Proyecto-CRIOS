from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from MiApp.models import DatInsc

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PreinscripcionForm(forms.ModelForm):
    class Meta:
        model = DatInsc
        #fields = 'all'
        fields = ['iidcliente', 'Nombres','Apellidos','Fecha de Nacimiento',
                  'Documento de Identidad (DNI)', 'Provincia','Domicilio','Estado Civil',
                  '¿Tiene Hijos?','Lugar de Trabajo','Numero de Celular','Telefono Fijo',
                  'Correo Electronico','Colegio de egreso','Año de Egreso','Titulo de Egreso',
                  'Otros Titulos','¿Tuvo otro ingreso a nivel Superior o Universitario anterior a este?',
                  '¿Cuales?','¿Completo los estudios?','¿Completo los estudios?']