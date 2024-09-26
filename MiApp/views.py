from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import DatInsc
from .forms import PreinscripcionForm 

def login(request):
    return render(request, 'login.html')

def test(request):
    return render(request, 'test.html')

def homebeta(request):
    return render(request, 'homebeta.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def lista_solicitudes(request):
    solicitudes = DatInsc.objects.all()
    return render(request, 'inscripciones/solicitudes/lista_solicitudes.html', {'solicitudes': solicitudes})

def agregar_solicitud(request):
    if request.method == "POST":
        form = PreinscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_solicitudes')
    else:
        form = PreinscripcionForm()
    return render(request, 'inscripciones/solicitudes/agregar_solicitud.html', {'form': form})

def eliminar_solicitud(request, id):
    solicitud = get_object_or_404(DatInsc, id=id)
    if request.method == "POST":
        solicitud.delete()
        return redirect('lista_solicitudes')
    return render(request, 'inscripciones/solicitudes/eliminar_solicitud.html', {'solicitud': solicitud})

@login_required
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            messages.success(request, '¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirige a la página de inicio de sesión
        else:
            messages.error(request, 'Hubo un error en la creación de la cuenta. Inténtalo de nuevo.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})