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
        fields = ['id_datinsc', 'nombre','apellido','fecha_nac','provincia','dni','edad','domicilio',
                  'telefono_fijo','celular_nro','email','estado_civil','hijos','lugar_trabajo','tel_emergencia',
                  'col_egreso','titulo','otro_titulo','anio_egreso','preg_1','resp_1','resp_2','preg_2']