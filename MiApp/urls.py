from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # Configuración para la URL raíz
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    ]