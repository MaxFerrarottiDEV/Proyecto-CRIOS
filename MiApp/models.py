from django.db import models

# Create your models here.

class Candidato(models.Model):
    apellido = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    fecha_nacimiento = models.CharField(max_length=100)
    provincia = models.CharField(max_length=255)
    numero_documento = models.CharField(max_length=20)
    edad = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    telefono_celular = models.CharField(max_length=100)
    telefono_emergencia = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=100)
    hijos = models.CharField(max_length=100)
    lugar_trabajo = models.CharField(max_length=100)
    colegio_egreso = models.CharField(max_length=255)
    colegio_titulo = models.CharField(max_length=255)
    año_egreso = models.CharField(max_length=100)
    otros_titulos = models.CharField(max_length=100)