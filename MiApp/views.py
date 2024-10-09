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
            messages.success(request, f'La solicitud de inscripcion se ha creado correctamente!')
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
            messages.error(request, 'Hubo un error en la creación de la solicitud. Inténtalo de nuevo.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form}) 

def consultas(request):
    dni = request.GET.get('dni')  
    if dni:
        estudiante = DatInsc.objects.filter(dni=dni).first()
        if estudiante:
            print(estudiante.id_datinsc)  
            context = {'estudiante': estudiante}
        else:

            context = {'error': 'Estudiante no encontrado'}
    else:
        
        lista_estudiantes = DatInsc.objects.all()
        for est in lista_estudiantes:
            print(est.id_datinsc) 
        context = {'estudiantes': lista_estudiantes}
    
    return render(request, 'inscripciones/consultas/consultas.html',context)

@login_required
def modificar(request, id):
    estudiante = get_object_or_404(DatInsc, pk=id)
    if request.method == 'POST':
        # Procesar los datos del formulario de modificación (añade tu lógica de actualización aquí)
        estudiante.nombre = request.POST.get('nombre')
        estudiante.apellido = request.POST.get('apellido')
        estudiante.dni = request.POST.get('dni')
        estudiante.Celular_Nro = request.POST.get('telefono')
        estudiante.email = request.POST.get('email')
        estudiante.domicilio = request.POST.get('domicilio')
        estudiante.save()
        messages.success(request, '¡Estudiante modificado exitosamente!')
        return redirect('consultas')
    return render(request, 'inscripciones/consultas/modificar.html', {'estudiante': estudiante})


# Vista para eliminar estudiante
@login_required
def eliminar_estudiante_ajax(request):
    estudiante_id = request.POST.get('id')
    estudiante = get_object_or_404(DatInsc, id_datinsc=estudiante_id)
    estudiante.delete()
    return JsonResponse({'success': True, 'message': 'Estudiante eliminado'}) # type: ignore


# Vista para adjuntar un archivo
def adjuntar_archivo(request):
    if request.method == 'POST':
        try:
            archivo = request.FILES['fileUpload']
            return HttpResponse('Archivo subido exitosamente.') # type: ignore
        except KeyError:
            return HttpResponse('No se encontró el archivo.') # type: ignore
    return render(request, 'Insc/consultas.html')