from django.shortcuts import render, redirect ,get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import PreinscripcionForm 
from django.http import JsonResponse
from .models import DatInsc, EstadosCurriculares ,Estudiantes,Materias,MateriasxplanesEstudios,PlanesEstudios

from datetime import date
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from MiApp.management.commands.sync_firebase_to_mysql import Command
from io import BytesIO
from reportlab.lib.pagesizes import letter # type: ignore
from reportlab.pdfgen import canvas # type: ignore
from reportlab.lib import colors # type: ignore
from reportlab.lib.units import inch # type: ignore
from reportlab.platypus import Table, TableStyle # type: ignore
import json


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

@csrf_exempt  # Desactiva la verificación CSRF solo para este endpoint
def sincronizar_datos(request):
    if request.method == 'POST':
        try:
            # Ejecutar el comando de sincronización de Firebase a MySQL
            command = Command()
            command.handle()

            return JsonResponse({'success': True, 'message': 'Datos sincronizados correctamente'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)

@csrf_exempt
def guardar_datos_google_forms(request):
    if request.method == 'POST':
        datos = json.loads(request.body)
        for dato in datos:
            # Suponiendo que tienes un modelo Solicitud
            DatInsc.objects.create(
                    nombre=dato.get('nombre', ''),
                    apellido=dato.get('apellido', ''),
                    fecha_nac=dato.get('fecha_nac', ''),
                    provincia=dato.get('provincia', ''),
                    dni=dato.get('dni', ''),
                    edad=dato.get('edad', ''),
                    domicilio=dato.get('domicilio', ''),
                    telefono_fijo=dato.get('telefono_fijo', ''),
                    celular_nro=dato.get('celular_nro', ''),
                    email=dato.get('email', ''),
                    estado_civil=dato.get('estado_civil', ''),
                    hijos=dato.get('hijos', None),
                    lugar_trabajo=dato.get('lugar_trabajo', ''),
                    tel_emergencia=dato.get('tel_emergencia', ''),
                    col_egreso=dato.get('col_egreso', ''),
                    titulo=dato.get('titulo', ''),
                    otro_titulo=dato.get('otro_titulo', ''),
                    anio_egreso=dato.get('anio_egreso', ''),
                    preg_1=dato.get('preg_1', None),
                    resp_1=dato.get('resp_1', ''),
                    resp_2=dato.get('resp_2', None),
                    preg_2=dato.get('preg_2', ''),
                    matricula=dato.get('matricula', False),
                    legajo_fisico=dato.get('legajo_fisico', False)
            )
        return JsonResponse({'mensaje': 'Datos guardados correctamente'}, status=200)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

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

@login_required
def build(request):
    return render(request, 'build.html')

@login_required
def plan_estudio_view(request):
    planes = PlanesEstudios.objects.all()
    return render(request, 'estadosCurriculares/planesEstudios/planestudio.html', {'planes': planes})

@login_required
def verEstado(request, dni): 
    estudiante = get_object_or_404(Estudiantes, id_datinsc__dni=dni)
    estado_curricular = EstadosCurriculares.objects.filter(id_estudiante_estcur=estudiante) 
    return render(request, 'estadosCurriculares/verEstado.html', {
        'estudiante': estudiante,
        'estado_curricular': estado_curricular})

@login_required
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

@login_required
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

@login_required    
def agregar_nota(request, dni):
    estudiante = get_object_or_404(Estudiantes, id_datinsc__dni=dni)
    
    if request.method == 'POST':
        materia_id = request.POST.get('materia')
        condicion = request.POST.get('condicion')
        nota = request.POST.get('nota')
        fecha = request.POST.get('fecha')

        # Crear la nueva nota
        materia = get_object_or_404(Materias, id=materia_id)
        nuevo_estado = EstadosCurriculares(
            id_estudiante=estudiante,
            id_matxplan=materia,
            condicion_nota=condicion,
            nota=nota,
            fecha_finalizacion=fecha
        )
        nuevo_estado.save()
        return redirect('estado_curricular', dni=dni)
    materias = Materias.objects.all()
    return render(request, 'estadosCurriculares/agregar_nota.html', {'estudiante': estudiante, 'materias': materias})

@login_required
def pdf_estadoCurricular(request):
    dni = request.GET.get('dni')
    if not dni:
        return HttpResponse("DNI no proporcionado.", status=400)
    estudiante = get_object_or_404(Estudiantes, id_datinsc__dni=dni)
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 710, f"Apellidos: {estudiante.id_datinsc.apellido}"),p.drawString(100, 690, f"Nombres: {estudiante.id_datinsc.nombre}")
    p.drawString(100, 750, f"Legajo N: {estudiante.nro_legajo}"), p.drawString(100, 730, f"DNI: {estudiante.id_datinsc.dni}")
    p.drawString(100, 650, "Notas del Estudiante")
    estado_curricular = estudiante.estadoscurriculares_set.all()
   
    data = [["Materia", "Estado", "Nota", "Fecha"]]  
    for materia in estado_curricular:
        data.append([
            materia.id_matxplan_estcur.id_materia.nombre,
            materia.condicion_nota,
            str(materia.nota),
            materia.fecha_finalizacion.strftime("%d/%m/%Y")
        ])
    
    table = Table(data, colWidths=[2*inch, 1.5*inch, 1*inch, 1.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    table.wrapOn(p, 100, 500)
    table.drawOn(p, 100, 500)

    p.showPage()
    p.save()
    
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{estudiante.id_datinsc.apellido} {estudiante.id_datinsc.nombre}-Estado Curricular.pdf"'
    return response