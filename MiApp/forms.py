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
    nombre = forms.CharField(label='Nombre:')
    apellido = forms.CharField(label='Apellido:')
    hijos = forms.IntegerField(label='¿Tiene hijos?')
    preg_1 = forms.IntegerField(label='¿Tuvo otro ingreso a nivel Superior o universitario anterior a este?')
    resp_1 = forms.CharField(label='¿Cuál?')
    resp_2 = forms.IntegerField(label='¿Completo esos estudios?')
    preg_2 = forms.CharField(label='¿Es beneficiario de algún tipo de Beca/Ayuda Social? (Especifique)')

    class Meta:
        model = DatInsc
        #fields = 'all'
        fields = ['id_datinsc', 'nombre','apellido','fecha_nac','provincia','dni','edad','domicilio',
                  'telefono_fijo','celular_nro','email','estado_civil','hijos','lugar_trabajo','tel_emergencia',
                  'col_egreso','titulo','otro_titulo','anio_egreso','preg_1','resp_1','resp_2','preg_2']
        exclude = ['matricula','legajo_fisico'] # Lista de campos del modelo a excluir del formulario