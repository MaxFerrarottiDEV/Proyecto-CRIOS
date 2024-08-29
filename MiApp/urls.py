from django.urls import path
from .views import register, home , login  

urlpatterns = [
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('', login, name='login'),
]

