from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # Configuración para la URL raíz
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('build/',views.build, name='build'),
    path('inscripciones/solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
    path('inscripciones/solicitudes/eliminar/<int:id>/', views.eliminar_solicitud, name='eliminar_solicitud'),
    path('inscripciones/consultas/', views.consultas, name='consultas'),
    path('inscripciones/consultas/modificar/<int:id>/', views.modificar, name='modificar'),
    path('upload/', views.adjuntar_archivo, name='adjuntar_archivo'),
    path('eliminar_estudiante_ajax/', views.eliminar_estudiante_ajax, name='eliminar_estudiante_ajax'),
    ]