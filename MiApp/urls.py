from django.urls import path
from .views import register, home , login, test  

urlpatterns = [
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('test/', test, name='test')
]

