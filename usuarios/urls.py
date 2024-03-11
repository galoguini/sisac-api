from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegistroView, LogoutView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(), name='logout'),
]