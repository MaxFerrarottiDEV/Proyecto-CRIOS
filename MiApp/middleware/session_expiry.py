from django.shortcuts import redirect

class SessionExpiryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.session.get('has_logged_out', False):
            # Permitir acceso
            return self.get_response(request)
        
        # Redirigir al login si la sesión ha expirado
        if not request.user.is_authenticated and request.path != '/login/':
            return redirect('login')
        
        return self.get_response(request)