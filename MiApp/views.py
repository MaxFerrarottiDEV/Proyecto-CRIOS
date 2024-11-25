from datetime import date

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from django.db.models import Q, Count
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter  # type: ignore
from reportlab.lib.units import inch  # type: ignore
from reportlab.pdfgen import canvas  # type: ignore
from reportlab.platypus import Table, TableStyle  # type: ignore

from .forms import PreinscripcionForm
from .models import CamposEstudios,Carreras, DatInsc, EstadosCurriculares, Estudiantes, InscCarreras, Materias, MateriasxplanesEstudios, PlanesEstudios, TiposUnidades

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Cambia 'home' al nombre de tu URL para la página principal.
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Cambia 'home' si es necesario.
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    request.session['has_logged_out'] = True
    logout(request)
    return redirect('login')


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
def change_password(request):
    if request.method == 'POST':
        # Obtener las contraseñas ingresadas
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        
        # Verificar si las contraseñas coinciden
        if new_password1 == new_password2:
            # Establecer la nueva contraseña
            request.user.set_password(new_password1)
            request.user.save()
            
            # Cerrar la sesión del usuario
            logout(request)
            
            # Mensaje de éxito
            messages.success(request, "Contraseña cambiada exitosamente. Por favor, vuelve a iniciar sesión.")
            
            # Redirigir al login
            return redirect('login')  # Redirigir al login tras cambio de contraseña
        else:
            # Mensaje de error si las contraseñas no coinciden
            messages.error(request, "Las contraseñas no coinciden.")
    
    return render(request, 'change_password.html')

@login_required
def tipo_inscripcion(request):
    return render(request, 'inscripciones/tipo_inscripcion.html')


@login_required
def lista_solicitudes(request):
    # Filtrar las solicitudes con inscripto=False
    solicitudes = DatInsc.objects.filter(inscripto=False)

    # Inicializamos el formulario de preinscripción
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

    # Devolver el formulario y las solicitudes filtradas
    return render(request, 'inscripciones/solicitudes/lista_solicitudes.html', {
        'solicitudes': solicitudes,
        'form': form  # Pasamos el formulario al contexto
    })


@login_required
def confirmar_solicitud(request, id_datinsc):
    # Obtener la solicitud específica
    solicitud = get_object_or_404(DatInsc, id_datinsc=id_datinsc)

    if request.method == 'POST':
        # Obtener valores del formulario
        matricula = request.POST.get('matricula') == 'True'
        legajo_fisico = request.POST.get('legajo_fisico') == 'True'
        carrera_id = request.POST.get('carrera')
        anio_insc = request.POST.get('anio_insc')
        nro_legajo = request.POST.get('nro_legajo') or None  # Si está vacío, será None

        # Fecha actual
        fecha_insc = date.today()

        # Crear un nuevo estudiante basado en la solicitud
        nuevo_estudiante = Estudiantes.objects.create(
            id_datinsc=solicitud,
            anio_insc=anio_insc,
            nro_legajo=nro_legajo,
            legajo_digital=None,  # Puedes ajustar según tus necesidades
        )

        # Crear un nuevo registro en la tabla InscCarreras
        insc_carrera = InscCarreras.objects.create(
            id_carrera_ic_id=carrera_id,
            fecha_insc=fecha_insc,
            id_estudiante_ic=nuevo_estudiante  # Relación con el nuevo estudiante
        )

        # Actualizar el atributo "inscripto" en la solicitud
        solicitud.inscripto = True
        solicitud.save()

        # Mensaje de éxito y redirección
        messages.success(request, 'Solicitud confirmada exitosamente.')
        return redirect('lista_solicitudes')

    # Obtener las carreras disponibles para el formulario
    carreras = Carreras.objects.all()
    return render(request, 'inscripciones/solicitudes/confirmar_solicitud.html', {
        'solicitud': solicitud,
        'carreras': carreras
    })


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
    # Obtener parámetros de búsqueda y filtro
    dni = request.GET.get('dni')
    curso = request.GET.get('curso')  # Filtro por curso

    if dni:
        # Buscar el estudiante por su DNI en DatInsc
        estudiante_datinsc = DatInsc.objects.filter(dni=dni).first()
        if estudiante_datinsc:
            # Buscar al estudiante relacionado en Estudiantes
            estudiante = Estudiantes.objects.filter(id_datinsc=estudiante_datinsc).first()
            if estudiante:
                context = {'estudiante': estudiante}
            else:
                context = {'error': 'No se encontró un estudiante con este DNI en la tabla de Estudiantes.'}
        else:
            context = {'error': 'No se encontró un estudiante con este DNI en DatInsc.'}
    else:
        # Obtener todos los estudiantes, filtrados y ordenados
        estudiantes = (
            Estudiantes.objects
            .select_related('id_datinsc')  # Cargar datos relacionados con DatInsc
            .order_by('id_datinsc__apellido', 'id_datinsc__nombre')  # Ordenar por apellido y nombre
        )
        
        if curso:
            # Filtrar por curso si se seleccionó uno
            estudiantes = estudiantes.filter(anio_insc=curso)
        
        context = {
            'estudiantes': estudiantes,
            'curso_seleccionado': curso  # Pasar el curso seleccionado al template
        }

    return render(request, 'inscripciones/consultas/consultas.html', context)


@login_required
def graficos_estudiantes(request):
    # Consulta para contar estudiantes por año de inscripción
    inscriptos_por_anio = (
        Estudiantes.objects.values('anio_insc')
        .annotate(total=Count('id_estudiante'))
        .order_by('anio_insc')
    )

    # Formatear datos para el gráfico
    etiquetas = ['1er Año', '2do Año', '3er Año', '4to Año', '5to Año']
    datos = [0] * 5  # Inicializar con ceros para los 5 años

    for inscripto in inscriptos_por_anio:
        anio = inscripto['anio_insc']
        if 1 <= anio <= 5:  # Asegurarnos de que esté en el rango esperado
            datos[anio - 1] = inscripto['total']

    return render(request, 'inscripciones/graficos_estudiantes.html', {'etiquetas': etiquetas, 'datos': datos})


@login_required
def ver_datos(request, id_estudiante_ic):
    # Obtener la inscripción en carrera por id_estudiante_ic
    insc_carrera = get_object_or_404(InscCarreras, id_estudiante_ic=id_estudiante_ic)

    # Obtener el estudiante relacionado
    estudiante = insc_carrera.id_estudiante_ic

    # Obtener los datos relacionados
    dat_insc = estudiante.id_datinsc  # Relación con DatInsc
    carrera = insc_carrera.id_carrera_ic  # Relación con la tabla Carreras

    # Contexto para el template
    context = {
        'estudiante': estudiante,
        'dat_insc': dat_insc,
        'insc_carrera': insc_carrera,
        'carrera': carrera,
    }

    return render(request, 'inscripciones/consultas/ver_datos.html', context)


@login_required
def guardar_legajo_digital(request, id_estudiante):
    if request.method == 'POST':
        enlace = request.POST.get('legajo_digital')
        estudiante = get_object_or_404(Estudiantes, id_estudiante=id_estudiante)
        estudiante.legajo_digital = enlace
        estudiante.save()
        messages.success(request, "Se ha guardado el enlace correctamente.")
    return redirect('ver_datos', id_estudiante_ic=estudiante.id_estudiante)


@login_required
def modificar_datos(request, id_estudiante):
    # Obtener el registro del estudiante por su ID
    estudiante = get_object_or_404(Estudiantes, id_estudiante=id_estudiante)

    # Acceder a los datos de la tabla DatInsc a través de la relación
    dat_insc = estudiante.id_datinsc

    # Si la solicitud es POST, procesar el formulario
    if request.method == 'POST':
        form = PreinscripcionForm(request.POST, instance=dat_insc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ver_datos', args=[id_estudiante]))
    else:
        # Crear el formulario con los datos actuales
        form = PreinscripcionForm(instance=dat_insc)

    # Renderizar la plantilla con el formulario y los datos del estudiante
    return render(request, 'inscripciones/consultas/modificar_datos.html', {
        'form': form,
        'estudiante': 
        estudiante
    })


@login_required
@transaction.atomic
def eliminar_estudiante(request, id_estudiante):
    estudiante = get_object_or_404(Estudiantes, id_estudiante=id_estudiante)
    try:
        # Eliminar inscripciones vinculadas
        InscCarreras.objects.filter(id_estudiante_ic=estudiante.id_estudiante).delete()
        
        # Eliminar datos personales
        datinsc = estudiante.id_datinsc
        estudiante.delete()
        datinsc.delete()
        
        # Mensaje de éxito
        request.session['message'] = "El estudiante ha sido eliminado con éxito."
    except Exception as e:
        request.session['error'] = f"Error al eliminar al estudiante: {str(e)}"
    return redirect('consultas')  # Redirige a la página de consultas


@login_required
def build(request):
    return render(request, 'build.html')


@login_required
def plan_estudio_view(request):
    anios_cursado = [1, 2, 3, 4, 5]  # Lista de años
    materias = Materias.objects.all()
    planes = PlanesEstudios.objects.all()
    carreras = Carreras.objects.all()

    # Obtén el ID del plan seleccionado desde los parámetros GET o POST
    id_plan = request.GET.get('id_planestudio')  # Supongamos que se pasa en la URL
    plan = PlanesEstudios.objects.get(pk=id_plan) if id_plan else None

    return render(request, 'estadosCurriculares/planesEstudios/planestudio.html', 
                  {'anios_cursado': anios_cursado,
                   'materias': materias,
                   'planes': planes,
                   'carreras': carreras,
                   'plan': plan,  # Incluye el plan seleccionado
                   })


@login_required
def agregar_plan(request):
    if request.method == 'POST':
        anio_plan = request.POST.get('anio_plan')
        id_carrera = request.POST.get('id_carrera')
        descripcion = request.POST.get('descripcion')

        # Asignar valor por defecto si descripción está vacía
        if not descripcion:
            descripcion = "No agregada"

        try:
            carrera = Carreras.objects.get(id_carrera=id_carrera)
            nuevo_plan = PlanesEstudios.objects.create(
                anio_plan=anio_plan,
                id_carrera=carrera,
                descripcion=descripcion
            )
            nuevo_plan.save()
            messages.success(request, "Plan de estudio agregado con éxito. No se olvide de agregar la materias en el boton 'Administrar Plan'")
        except Carreras.DoesNotExist:
            messages.error(request, "La carrera seleccionada no existe.")
        return redirect('plan_estudio')

    return render(request, 'plan_estudio')


@login_required
def guardar_materias_plan(request):
    if request.method == 'POST':
        id_planestudio = request.POST.get('id_planestudio')
        plan = get_object_or_404(PlanesEstudios, id_planestudio=id_planestudio)

        for anio in range(1, 6):  # Iterar sobre los años del 1 al 5
            materias_ids = request.POST.getlist(f'materias_{anio}[]')

            for materia_id in materias_ids:
                materia = get_object_or_404(Materias, id_materia=materia_id)
                
                # Crear la relación con el año correspondiente
                MateriasxplanesEstudios.objects.create(
                    id_planestudio=plan,
                    id_materia=materia,
                    anio_materia=anio,  # Asignar el año correspondiente
                )

        messages.success(request, "Materias agregadas correctamente al plan de estudio.")
        return redirect('plan_estudio')
    

@login_required
@login_required
def obtener_materias_plan(request, plan_id):
    # Obtener las materias asociadas al plan, ordenadas por año
    materias = MateriasxplanesEstudios.objects.filter(id_planestudio_id=plan_id).order_by('anio_materia')
    
    # Organizar las materias por año
    materias_data = {}
    for materia in materias:
        anio = materia.anio_materia  # Atributo del año
        if anio not in materias_data:
            materias_data[anio] = []
        materias_data[anio].append({
            'nombre': materia.id_materia.nombre,  # Suponiendo que `id_materia` tiene un campo `nombre`
        })
    
    return JsonResponse({'materias': materias_data})


@login_required
def eliminar_plan(request, id_planestudio):
    try:
        plan = PlanesEstudios.objects.get(id_planestudio=id_planestudio)
        plan.delete()
        messages.success(request, "Plan de estudio eliminado con éxito.")
    except PlanesEstudios.DoesNotExist:
        messages.error(request, "El plan de estudio no existe.")
    return redirect('plan_estudio')


@login_required
def materias_view(request):
    materias = Materias.objects.all()
    tipos_unidades = TiposUnidades.objects.all()  # Obtener todos los tipos de unidades
    campos_estudio = CamposEstudios.objects.all()   # Obtener todos los campos de estudio
    return render(request, 'estadosCurriculares/planesEstudios/materias.html', {
        'materias': materias,
        'tipos_unidades': tipos_unidades,
        'campos_estudio': campos_estudio,
    })


@login_required
def agregar_materia(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        id_unidad = request.POST['id_unidad']
        cuatrimestral_anual = request.POST['cuatrimestral_anual']
        id_campoestudio = request.POST['id_campoestudio']
            # Manejar el valor del checkbox
        correlatividad = request.POST.get('correlatividad', request.POST.get('correlatividad_hidden'))

        Materias.objects.create(
            nombre=nombre,
            id_unidad_id=id_unidad,
            cuatrimestral_anual=cuatrimestral_anual,
            id_campoestudio_id=id_campoestudio,
            correlatividad=correlatividad,
        )

        messages.success(request, 'Materia agregada exitosamente.')
        return redirect('materia')  # Redirigir a la lista de materias
    return redirect('materia')


@login_required
def editar_materia(request):
    if request.method == 'POST':
        id_materia = request.POST.get('id_materia')
        nombre = request.POST.get('nombre')
        id_unidad = request.POST.get('id_unidad')
        cuatrimestral_anual = request.POST.get('cuatrimestral_anual')
        id_campoestudio = request.POST.get('id_campoestudio')
        correlatividad = request.POST.get('correlatividad', request.POST.get('correlatividad_hidden'))

        # Obtener la materia que se va a editar
        materia = get_object_or_404(Materias, id_materia=id_materia)
        
        # Asignar los valores a la materia
        materia.nombre = nombre

        # Obtener la instancia de TiposUnidades correspondiente al id_unidad
        if id_unidad:
            materia.id_unidad = get_object_or_404(TiposUnidades, id_unidad=id_unidad)
        
        # Asignar cuatrimestral_anual y correlatividad
        materia.cuatrimestral_anual = cuatrimestral_anual

        if id_campoestudio:
            materia.id_campoestudio = get_object_or_404(CamposEstudios, id_campoestudio=id_campoestudio)
        materia.correlatividad = correlatividad

        # Guardar los cambios
        materia.save()

        messages.success(request, "Materia actualizada con éxito.")
        return redirect('materia')
    
    
@login_required
def eliminar_materia(request, id_materia):
    materia = get_object_or_404(Materias, id_materia=id_materia)
    materia.delete()
    messages.success(request, "La materia se ha eliminado correctamente.")
    return redirect('materia')  # Asegúrate de usar el nombre correcto de la vista


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