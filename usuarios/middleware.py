from rest_framework.response import Response

class EmpresaSeleccionadaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.empresa_seleccionada:
            return Response({'error': 'Debe seleccionar o crear una empresa.'}, status=400)
        response = self.get_response(request)
        return response