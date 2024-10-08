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
    # Campo de seleccion para barra de opciones:
    PROVINCIA_CHOICES = {
    "-------": "-------",
    "Buenos Aires" : "Buenos Aires",
    "CABA" : "CABA",
    "Catamarca" : "Catamarca",
    "Chaco" : "Chaco",
    "Chubut" : "Chubut",
    "Córdoba" : "Córdoba",
    "Corrientes" : "Corrientes",
    "Entre Ríos" : "Entre Ríos",
    "Formosa" : "Formosa",
    "Jujuy" : "Jujuy",
    "La Pampa" : "La Pampa",
    "La Rioja" : "La Rioja",
    "Mendoza" : "Mendoza",
    "Misiones" : "Misiones",
    "Neuquén" : "Neuquén",
    "Río Negro" : "Río Negro",
    "Salta" : "Salta",
    "San Juan" : "San Juan",
    "San Luis" : "San Luis",
    "Santa Cruz" : "Santa Cruz",
    "Santa Fe" : "Santa Fe",
    "Santiago del Estero" : "Santiago del Estero",
    "Tierra del Fuego" : "Tierra del Fuego",
    "Tucuman" : "Tucuman",
}

    # Campo de seleccion con botones tipo radio:
    ESTADO_CIVIL_CHOICES = [
        ('Soltero/a', 'Soltero/a'),
        ('Casado/a', 'Casado/a'),
        ('Divorciado/a', 'Divorciado/a'),
        ('Viudo/a', 'Viudo/a'),
    ]
    TIENE_HIJOS_CHOICES = [
        (0, 'Si'),
        (1, 'No'),
    ]
    PREG_1_CHOICES = [
        (0, 'Si'),
        (1, 'No'),
    ]
    RESP_2_CHOICES = [
        (0, 'Si'),
        (1, 'No'),      
    ]
    nombre = forms.CharField(label='Nombre/s:',)
    apellido = forms.CharField(label='Apellido/s:',)
    fecha_nac = forms.CharField(label='Fecha de Nacimiento:',widget=forms.DateInput(attrs={'type': 'date'}),)
    provincia = forms.ChoiceField(label='Provincia:',choices=PROVINCIA_CHOICES,)
    dni = forms.CharField(label='DNI (Solo numeros):',max_length=10,)
    edad = forms.CharField(label='Edad:', max_length=2,)
    domicilio = forms.CharField(label='Domicilio:', max_length=200,)
    telefono_fijo = forms.CharField(label='Teléfono Fijo:', max_length=12, required=False,)
    celular_nro = forms.CharField(label='Número de Celular:', max_length=12,)
    email = forms.CharField(label='Correo Electronico:', max_length=200, required=False,)
    estado_civil = forms.ChoiceField(label='Estado Civil:', choices=ESTADO_CIVIL_CHOICES, widget=forms.RadioSelect,)
    hijos = forms.ChoiceField(label='¿Tiene hijos?:',choices=TIENE_HIJOS_CHOICES, widget=forms.RadioSelect, required=False,)
    lugar_trabajo = forms.CharField(label='Lugar de Trabajo:', max_length=200, required=False,)
    tel_emergencia = forms.CharField(label='Teléfono de Emergencia:', max_length=12, required=True,)
    col_egreso = forms.CharField(label='Colegio que Egresó:', max_length=200,required=True,)
    titulo = forms.CharField(label='Título:', max_length=200, required=False,)
    otro_titulo = forms.CharField(label='Otros Títulos (Separar con coma):', max_length=200, required=False,)
    anio_egreso = forms.CharField(label='Año de Egreso:',max_length=4,)
    preg_1 = forms.ChoiceField(label='¿Tuvo otro ingreso a nivel Superior o universitario anterior a este?:',choices=PREG_1_CHOICES, widget=forms.RadioSelect,required=False,)
    resp_1 = forms.CharField(label='¿Cuál?', required=False,)
    resp_2 = forms.ChoiceField(label='¿Completo esos estudios?:', choices=RESP_2_CHOICES, widget=forms.RadioSelect,required=False,)
    preg_2 = forms.CharField(label='¿Es beneficiario de algún tipo de Beca/Ayuda Social? (Especifique):',required=False,)

    class Meta:
        model = DatInsc
        #fields = 'all'
        fields = ['id_datinsc', 'nombre','apellido','fecha_nac','provincia','dni','edad','domicilio',
                  'telefono_fijo','celular_nro','email','estado_civil','hijos','lugar_trabajo','tel_emergencia',
                  'col_egreso','titulo','otro_titulo','anio_egreso','preg_1','resp_1','resp_2','preg_2']
        exclude = ['matricula','legajo_fisico'] # Lista de campos del modelo a excluir del formulario

