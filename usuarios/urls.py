from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegistroView, LogoutView, PerfilView, EditarPerfilView, UpdateSMTPInfoView, SendEmailView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('editar_perfil/', EditarPerfilView.as_view(), name='editar_perfil'),
    path('update_smtp_info/', UpdateSMTPInfoView.as_view(), name='update_smtp_info'),
    path('send-email/', SendEmailView.as_view(), name='send_email'),
]
