from django.contrib.auth import views as auth_views # type: ignore
from django.urls import path, include # type: ignore
from django.contrib import admin # type: ignore
from . import views
from .forms import CustomPasswordResetForm

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # Configuración para la URL raíz
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset/password_reset_form.html', 
             form_class=CustomPasswordResetForm,
             email_template_name='registration/password_reset/password_reset_email.html'),
         name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset/password_reset_complete.html'), name='password_reset_complete'),
    path('build/',views.build, name='build'),
    path('inscripciones/tipoInscripcion/',views.tipo_inscripcion, name='tipo_inscripcion'),
    path('inscripciones/solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
    path('inscripciones/solicitudes/eliminar/<id_datinsc>', views.eliminar_solicitud, name='eliminar_solicitud'),
    path('inscripciones/consultas/', views.consultas, name='consultas'),
    path('inscripciones/consultas/modificar/<int:id>/', views.modificar, name='modificar'),
    path('upload/', views.adjuntar_archivo, name='adjuntar_archivo'),
    path('eliminar_estudiante_ajax/', views.eliminar_estudiante_ajax, name='eliminar_estudiante_ajax'),
    ]