from django.urls import path
from .views import register_view, home , login, test  

urlpatterns = [
    path('register/', register_view, name='register'),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('test/', test, name='test')
]

