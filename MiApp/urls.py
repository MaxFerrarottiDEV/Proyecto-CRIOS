from django.contrib.auth import views as auth_views # type: ignore
from django.urls import path, include # type: ignore
from django.contrib import admin # type: ignore
from . import views
from .forms import CustomPasswordResetForm
from .views import guardar_datos_google_forms, sincronizar_datos


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('build/',views.build, name='build'),

    # Password Reset
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(
    template_name='registration/password_reset/password_reset_form.html', 
    form_class=CustomPasswordResetForm,
    email_template_name='registration/password_reset/password_reset_email.html'),
    name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset/password_reset_complete.html'), name='password_reset_complete'),
    
    # Modulo de solicitudes inscripciones
    path('inscripciones/tipoInscripcion/',views.tipo_inscripcion, name='tipo_inscripcion'),
    path('inscripciones/solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
    path('inscripciones/solicitudes/confirmar/<int:id_datinsc>/', views.confirmar_solicitud, name='confirmar_solicitud'),
    path('inscripciones/solicitudes/editar/<id_datinsc>', views.editar_solicitud, name='editar_solicitud'),
    path('inscripciones/solicitudes/eliminar/<id_datinsc>', views.eliminar_solicitud, name='eliminar_solicitud'),
    path('inscripciones/solicitudes/guardarDatos', views.guardar_datos_google_forms, name='guardar_datos_google_forms'),
    path('sincronizar/', sincronizar_datos, name='sincronizar_datos'),

    # Modulo de consultas
    path('inscripciones/consultas/', views.consultas, name='consultas'),
    path('inscripciones/consultas/modificar/<str:dni>/', views.modificar, name='modificar'),
    path('eliminar/<int:dni>/', views.eliminar_estudiante, name='eliminar_estudiante'),


    # Modulo de estados Curriculares
    #Gestión de Planes de Estudio:
    path('plan-estudio/', views.plan_estudio_view, name='plan_estudio'),
    #Gestión de Estados Curriculares:
    path('estadosCurriculares/estados', views.estados, name='estados'),
    path('estadosCurriculares/estados', views.agregarNota, name='agregarNota'),
    path('estadosCurriculares/agregar_nota/<str:dni>/', views.agregar_nota, name='agregar_nota'),
    path('estadosCurriculares/verEstado/<str:dni>/', views.verEstado, name='verEstado'),
    path('pdf_estadoCurricular', views.pdf_estadoCurricular, name='descargar_pdf'),
    ]