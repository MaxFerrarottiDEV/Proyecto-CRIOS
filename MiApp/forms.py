from typing import Any
from django import forms  # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth.models import User # type: ignore
from MiApp.models import DatInsc # type: ignore
from django import forms # type: ignore

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        
        # Validar si la contraseña contiene al menos un número
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        
        return password

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
    nombre = forms.CharField(label='Nombre/s:',required=True,)
    apellido = forms.CharField(label='Apellido/s:',required=True,)
    fecha_nac = forms.CharField(label='Fecha de Nacimiento:',widget=forms.DateInput(attrs={'type': 'date'}),required=True,)
    provincia = forms.ChoiceField(label='Provincia:',choices=PROVINCIA_CHOICES,required=True,)
    dni = forms.CharField(label='DNI (Solo numeros):',max_length=10,required=True,)
    edad = forms.CharField(label='Edad:', max_length=2,required=True)
    domicilio = forms.CharField(label='Domicilio:', max_length=200,required=True)
    telefono_fijo = forms.CharField(label='Teléfono Fijo:', max_length=12, required=False,)
    celular_nro = forms.CharField(label='Número de Celular:', max_length=12,required=True)
    email = forms.CharField(label='Correo Electronico:', max_length=200, required=False,)
    estado_civil = forms.ChoiceField(label='Estado Civil:', choices=ESTADO_CIVIL_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio', 'style': 'font-size: 16px; margin-right: 10px;'}),required=True,)
    hijos = forms.ChoiceField(label='¿Tiene hijos?:',choices=TIENE_HIJOS_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio', 'style': 'font-size: 16px; margin-right: 10px;'}), required=False,)
    lugar_trabajo = forms.CharField(label='Lugar de Trabajo:', max_length=200, required=False,)
    tel_emergencia = forms.CharField(label='Teléfono de Emergencia:', max_length=12, required=True,)
    col_egreso = forms.CharField(label='Colegio que Egresó:', max_length=200,required=True,)
    titulo = forms.CharField(label='Título:', max_length=200, required=False,)
    otro_titulo = forms.CharField(label='Otros Títulos (Separar con coma):', max_length=200, required=False,)
    anio_egreso = forms.CharField(label='Año de Egreso:',max_length=4,required=True)
    preg_1 = forms.ChoiceField(label='¿Tuvo otro ingreso a nivel Superior o universitario anterior a este?:',choices=PREG_1_CHOICES, widget=forms.RadioSelect,required=False,)
    resp_1 = forms.CharField(label='¿Cuál?', required=False,)
    resp_2 = forms.ChoiceField(label='¿Completo esos estudios?:', choices=RESP_2_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio', 'style': 'font-size: 16px; margin-right: 10px;'}),required=False,)
    preg_2 = forms.CharField(label='¿Es beneficiario de algún tipo de Beca/Ayuda Social? (Especifique):',required=False,)

    class Meta:
        model = DatInsc
        #fields = 'all'
        fields = ['id_datinsc', 'nombre','apellido','fecha_nac','provincia','dni','edad','domicilio',
                  'telefono_fijo','celular_nro','email','estado_civil','hijos','lugar_trabajo','tel_emergencia',
                  'col_egreso','titulo','otro_titulo','anio_egreso','preg_1','resp_1','resp_2','preg_2']
        exclude = ['matricula','legajo_fisico'] # Lista de campos del modelo a excluir del formulario

    def clean_hijos(self):
        hijos = self.cleaned_data.get('hijos')
        if hijos in ['', None]:  # Si está vacío o es None
            return None  # Devuelve None en lugar de una cadena vacía
        return hijos
    def clean_preg_1(self):
        preg_1 = self.cleaned_data.get('preg_1')
        if preg_1 in ['', None]:  # Si está vacío o es None
            return None  # Devuelve None en lugar de una cadena vacía
        return preg_1
    def clean_resp_1(self):
        resp_1 = self.cleaned_data.get('resp_1')
        if resp_1 in ['', None]:  # Si está vacío o es None
            return None  # Devuelve None en lugar de una cadena vacía
        return resp_1
    def clean_resp_2(self):
        resp_2 = self.cleaned_data.get('resp_2')
        if resp_2 in ['', None]:  # Si está vacío o es None
            return None  # Devuelve None en lugar de una cadena vacía
        return resp_2
    def clean_preg_2(self):
        preg_2 = self.cleaned_data.get('preg_2')
        if preg_2 in ['', None]:  # Si está vacío o es None
            return None  # Devuelve None en lugar de una cadena vacía
        return preg_2