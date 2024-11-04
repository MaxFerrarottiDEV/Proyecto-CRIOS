from django.shortcuts import render, redirect ,get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import PreinscripcionForm 
from django.http import JsonResponse
from .models import DatInsc, EstadosCurriculares ,Estudiantes,Materias,MateriasxplanesEstudios
from datetime import date


def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, '¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('login')  
        else:
            messages.error(request, 'Hubo un error en la creación de la solicitud. Inténtalo de nuevo.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form}) 


@login_required
def home(request):
    return render(request,'home.html')

@login_required
def tipo_inscripcion(request):
    return render(request, 'inscripciones/tipo_inscripcion.html')

@login_required
def lista_solicitudes(request):
    
    solicitudes = DatInsc.objects.filter

    # Inicializamos el formulario de la solicitud
    form = PreinscripcionForm()

    if request.method == 'POST':
        form = PreinscripcionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Se ha agregado exitosamente la solicitud.')
                return redirect('lista_solicitudes')
            except Exception as e:
                messages.error(request, f'Ocurrió un error al agregar la solicitud: {str(e)}')
        else:
            messages.error(request, 'Formulario inválido. Por favor revisa los campos e inténtalo de nuevo.')

    # Siempre devolver el formulario y las solicitudes, incluso para GET
    return render(request, 'inscripciones/solicitudes/lista_solicitudes.html', {
        'solicitudes': solicitudes,
        'form': form  # Pasamos el formulario al contexto
    })

@login_required
def confirmar_solicitud(request, id_datinsc):
    solicitud = get_object_or_404(DatInsc, id_datinsc=id_datinsc)

    if request.method == 'POST':
        matricula = request.POST.get('matricula') == 'True'  # Si no se marca, será False
        legajo_fisico = request.POST.get('legajo_fisico') == 'True'  # Si no se marca, será False

        # Actualizamos los campos en la solicitud
        solicitud.matricula = matricula
        solicitud.legajo_fisico = legajo_fisico
        solicitud.save()

        # Creamos un nuevo estudiante basado en la solicitud
        nuevo_estudiante = Estudiantes.objects.create(
            id_datinsc=solicitud,
            fecha_insc_est=date.today(),  # Corregido a date.today()
            nro_legajo=None,  # Esto puede depender de tus necesidades
            legajo_digital=None  # Esto puede depender de tus necesidades
        )

        # Mensaje de éxito y redirigir a la lista de solicitudes
        messages.success(request, 'Solicitud confirmada exitosamente.')
        return redirect('lista_solicitudes')

    return render(request, 'inscripciones/solicitudes/confirmar_solicitud.html', {'solicitud': solicitud})


@login_required
def editar_solicitud(request, id_datinsc):
    solicitud = get_object_or_404(DatInsc, id_datinsc=id_datinsc)
    if request.method == 'POST':
        form = PreinscripcionForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitud actualizada con éxito.')
            return redirect('lista_solicitudes')
        else:
            messages.error(request, 'Hubo un error en el formulario. Por favor, corrige los errores.')
    else:
        form = PreinscripcionForm(instance=solicitud)

    return render(request, 'inscripciones/solicitudes/editar_solicitud.html', {'form': form})

@login_required
def eliminar_solicitud(request, id_datinsc):
    solicitud = get_object_or_404(DatInsc, id_datinsc=id_datinsc)
    
    if request.method == "POST":
        try:
            solicitud.delete()
            messages.success(request, "La solicitud ha sido eliminada correctamente.")
        except Exception as e:
            messages.error(request, f"Ocurrió un error al eliminar la solicitud: {str(e)}")
        return redirect('lista_solicitudes')
    return render(request, 'inscripciones/solicitudes/eliminar_solicitud.html', {'solicitud': solicitud})


@login_required
def consultas(request):
    dni = request.GET.get('dni')  
    if dni:
        estudiante_datinsc = DatInsc.objects.filter(dni=dni).first()
        if estudiante_datinsc:
            estudiante = Estudiantes.objects.filter(id_datinsc=estudiante_datinsc).first()
            context = {'estudiante': estudiante}
        else:
            context = {'error': 'Estudiante no encontrado'}
    else:
        lista_estudiantes = Estudiantes.objects.select_related('id_datinsc').all()
        context = {'estudiantes': lista_estudiantes}
    
    return render(request, 'inscripciones/consultas/consultas.html', context)


@login_required
def modificar(request, dni):
    estudiante = get_object_or_404(DatInsc, dni=dni)
    
    if request.method == 'POST':
        estudiante.nombre = request.POST.get('nombre')
        estudiante.apellido = request.POST.get('apellido')
        estudiante.dni = request.POST.get('dni')
        estudiante.celular_nro = request.POST.get('telefono')
        estudiante.email = request.POST.get('email')
        estudiante.domicilio = request.POST.get('domicilio')
        estudiante.matricula = request.POST.get('matricula') == 'on'
        estudiante.legajo_fisico = request.POST.get('legajo_fisico') == 'on'
        estudiante.save()
        messages.success(request, '¡Estudiante modificado exitosamente!')
        return redirect('consultas')
    return render(request, 'inscripciones/consultas/modificar.html', {'estudiante': estudiante})


@login_required
def eliminar_estudiante(request, dni):
    estudiante = get_object_or_404(Estudiantes, id_datinsc__dni=dni)
    estudiante.delete()
    messages.success(request, 'El estudiante ha sido eliminado exitosamente.')
    return redirect('consultas')


def build(request):
    return render(request, 'build.html')


def estados(request):
    dni = request.GET.get('dni')
    if dni:
        estudiante_datinsc = DatInsc.objects.filter(dni=dni).first()
        if estudiante_datinsc:
            estudiante = Estudiantes.objects.filter(id_datinsc=estudiante_datinsc).first()
            if estudiante:
                estado_curricular = EstadosCurriculares.objects.filter(id_estudiante_estcur=estudiante)
                materias = Materias.objects.all()
                context = {
                    'estudiante': estudiante,
                    'estudiante_datinsc': estudiante_datinsc,
                    'estado_curricular': estado_curricular,
                    'materias': materias  }
            else:
                context = {'error': 'No se encontró el estado curricular para este estudiante.'}
        else:
            context = {'error': 'Estudiante no encontrado.'}
    else:
        lista_estudiantes = Estudiantes.objects.all()
        materias = Materias.objects.all()  #
        context = {
            'estudiantes': lista_estudiantes,
            'materias': materias }

    return render(request, 'estadosCurriculares/estados.html', context)


def agregarNota(request):
    if request.method == 'POST':
        materia_id = request.POST.get('materia')
        condicion_nota = request.POST.get('condicion')
        nota = request.POST.get('nota')
        fecha_finalizacion = request.POST.get('fecha')
        estudiante_id = request.POST.get('estudiante_id')

        nueva_nota = EstadosCurriculares(
            id_matxplan_estcur_id=materia_id, 
            id_estudiante_estcur_id=estudiante_id,
            condicion_nota=condicion_nota,
            nota=nota,
            fecha_finalizacion=fecha_finalizacion
        )
        nueva_nota.save()
        return redirect('estados')
    else:
        materias = Materias.objects.all()
        return render(request, 'estados.html', {'materias': materias})

def examenes(request):
    return render(request, 'examenes/examenes.html')





