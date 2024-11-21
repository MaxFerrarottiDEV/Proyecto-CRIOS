from django.shortcuts import redirect

class SessionExpiryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Lista de rutas permitidas sin autenticación
        self.allowed_paths = [
            '/login/',
            '/reset_password/',
            '/reset_password_send/',
            '/reset/',
            '/reset_password_complete/',
        ]

    def __call__(self, request):
        # Permitir acceso si el usuario está autenticado
        if request.user.is_authenticated and not request.session.get('has_logged_out', False):
            return self.get_response(request)
        
        # Permitir acceso a rutas en la lista de excepciones
        if any(request.path.startswith(path) for path in self.allowed_paths):
            return self.get_response(request)

        # Redirigir al login si la sesión ha expirado
        if not request.user.is_authenticated:
            return redirect('login')
        
        return self.get_response(request)