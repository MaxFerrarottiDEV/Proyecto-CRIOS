from django.contrib.auth import views as auth_views  # type: ignore
from django.contrib.auth.views import LogoutView
from django.urls import path, include  # type: ignore
from django.contrib import admin  # type: ignore
from . import views
from .views import login_view, logout_view
from .forms import CustomPasswordResetForm

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('cambiar_contraseña/', views.change_password, name='change_password'),

    path('register/', views.register, name='register'),

    path('login/', login_view, name='login'),

    path('logout/', logout_view, name='logout'),

    path('build/', views.build, name='build'),

    # Password Reset
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset/password_reset_form.html',
             form_class=CustomPasswordResetForm,
             email_template_name='registration/password_reset/password_reset_email.html'),
         name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset/password_reset_complete.html'), name='password_reset_complete'),

    # Modulo de inscripciones - solicitudes
    path('inscripciones/tipoInscripcion/',
         views.tipo_inscripcion, name='tipo_inscripcion'),
    path('inscripciones/solicitudes/',
         views.lista_solicitudes, name='lista_solicitudes'),
    path('inscripciones/solicitudes/confirmar/<int:id_datinsc>/',
         views.confirmar_solicitud, name='confirmar_solicitud'),
    path('inscripciones/solicitudes/editar/<int:id_datinsc>',
         views.editar_solicitud, name='editar_solicitud'),
    path('inscripciones/solicitudes/eliminar/<int:id_datinsc>',
         views.eliminar_solicitud, name='eliminar_solicitud'),

    # Modulo de inscripciones - consultas
    path('inscripciones/consultas/', views.consultas, name='consultas'),
    path('inscripciones/graficos/estudiantes/',
         views.graficos_estudiantes, name='graficos_estudiantes'),
    path('inscripciones/consultas/ver_datos/<int:id_estudiante_ic>/',
         views.ver_datos, name='ver_datos'),
    path('inscripciones/consultas/modificar_datos/<int:id_estudiante>/',
         views.modificar_datos, name='modificar_datos'),
    path('inscripciones/consultas/guardar_legajo/<int:id_estudiante>/',
         views.guardar_legajo_digital, name='guardar_legajo_digital'),
    path('inscripciones/consultas/eliminar/<int:id_estudiante>/',
         views.eliminar_estudiante, name='eliminar_estudiante'),

    # Modulo de estados Curriculares - Gestión de Planes de Estudio:
    path('plan_estudio/', views.plan_estudio_view, name='plan_estudio'),
    path('plan_estudio/agregar_plan/', views.agregar_plan, name='agregar_plan'),
    path('plan_estudio/eliminar_plan/<int:id_planestudio>/',
         views.eliminar_plan, name='eliminar_plan'),
    path('plan_estudio/<int:plan_id>/materias/',
         views.obtener_materias_plan, name='obtener_materias_plan'),
    path('plan_estudio/agregar_materias/',
         views.guardar_materias_plan, name='guardar_materias_plan'),
    path('plan_estudio/materias', views.materias_view, name='materia'),
    path('plan_estudio/materias/agregar_materia/',
         views.agregar_materia, name='agregar_materia'),
    path('plan_estudio/materias/editar_materia/',
         views.editar_materia, name='editar_materia'),
    path('plan_estudio/materias/eliminar_materia/<int:id_materia>/',
         views.eliminar_materia, name='eliminar_materia'),

    # Modulo de estados Curriculares - Gestión de Estados Curriculares:
    path('estadosCurriculares/estados', views.estados, name='estados'),
    path('estadosCurriculares/estados', views.agregarNota, name='agregarNota'),
    path('estadosCurriculares/agregar_nota/<str:dni>/',
         views.agregar_nota, name='agregar_nota'),
    path('estadosCurriculares/verEstado/<str:dni>/',
         views.verEstado, name='verEstado'),
    path('pdf_estadoCurricular', views.pdf_estadoCurricular, name='descargar_pdf'),

    # examenes gestion
    path('examenes/gestionExamenes/',
         views.gestion_Examenes, name='gestion_Examenes'),
    path('examenes/obtener_examenes/',
         views.obtener_examenes, name='Obtener_examenes'),
    path('examenes/obtener_materias/',
         views.obtener_materias, name='obtener_materias'),
    path('examenes/agregar_examen/', views.agregar_examen, name='agregar_examen'),
    path('examenes/eliminar_mesaExamen/<int:Id_MesaExamen>/',
         views.eliminar_mesaExamen, name='eliminar_mesaExamen'),
    path('examenes/editar_mesaExamen/<int:Id_MesaExamen>/',
         views.editar_mesaExamen, name='editar_mesaExamen'),
    # INSCRIPCIÓN MESA EXAMENS

    path('Examenes/solicitud_examenes/',
         views.solicitud_examenes, name='solicitud_examenes'),

    path('Examenes/solicitud_examenes/inscribir_Examen/<int:id_estudiante_ie>/',
         views.inscribir_examen, name='inscribir_examen'),

]
