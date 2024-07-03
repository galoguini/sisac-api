from rest_framework.response import Response

class EmpresaSeleccionadaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verificar si la solicitud está dirigida al admin de Django
        if request.path.startswith('/admin'):
            # Si es así, simplemente pasa la solicitud al siguiente middleware o vista sin hacer nada
            return self.get_response(request)

        # Tu lógica existente para usuarios autenticados fuera del admin
        if request.user.is_authenticated and not request.user.empresa_seleccionada:
            return Response({'error': 'Debe seleccionar o crear una empresa.'}, status=400)
        
        response = self.get_response(request)
        return response