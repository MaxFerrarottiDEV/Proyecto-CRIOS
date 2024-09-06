from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            messages.success(request, '¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirige a la página de inicio de sesión
        else:
            messages.error(request, 'Hubo un error en la creación de la cuenta. Inténtalo de nuevo.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    return render(request, 'login.html')

def test(request):
    return render(request, 'test.html')

def homebeta(request):
    return render(request, 'homebeta.html')

@login_required
def home(request):
    return render(request, 'home.html')
