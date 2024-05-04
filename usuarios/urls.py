from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegistroView, LogoutView, PerfilView, EditarPerfilView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('editar_perfil/', EditarPerfilView.as_view(), name='editar_perfil'),
]