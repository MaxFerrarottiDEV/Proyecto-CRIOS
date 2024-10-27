from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('build/',views.build, name='build'),

    
    # Modulo de estados inscripciones
    path('inscripciones/tipoInscripcion/',views.tipo_inscripcion, name='tipo_inscripcion'),
    path('inscripciones/solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
    path('inscripciones/solicitudes/confirmar/<int:id_datinsc>/', views.confirmar_solicitud, name='confirmar_solicitud'),
    path('inscripciones/solicitudes/editar/<id_datinsc>', views.editar_solicitud, name='editar_solicitud'),
    path('inscripciones/solicitudes/eliminar/<id_datinsc>', views.eliminar_solicitud, name='eliminar_solicitud'),

    # Modulo de estados inscripciones
    path('inscripciones/consultas/', views.consultas, name='consultas'),
    path('inscripciones/consultas/modificar/<int:id>/', views.modificar, name='modificar'),
    path('upload/', views.adjuntar_archivo, name='adjuntar_archivo'),
    path('eliminar_estudiante_ajax/', views.eliminar_estudiante_ajax, name='eliminar_estudiante_ajax'),

    # Modulo de estados Curriculares
    path('estadosCurriculares/estados', views.estados, name='estados'),
    path('estadosCurriculares/estados', views.agregarNota, name='agregarNota'),

    ]