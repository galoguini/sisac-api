from django.contrib.auth.models import AbstractUser
from django.db import models
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY').encode()
fernet = Fernet(ENCRYPTION_KEY)

class Usuario(AbstractUser):
    celular = models.CharField(max_length=40)
    empresa_seleccionada = models.ForeignKey('empresas.Empresa', on_delete=models.SET_NULL, blank=True, null=True, related_name='usuarios_seleccionados')
    email_smtp = models.EmailField(max_length=254, blank=True, null=True)
    _smtp_app_password = models.BinaryField(blank=True, null=True, db_column='smtp_app_password')

    @property
    def smtp_app_password(self):
        if self._smtp_app_password:
            return fernet.decrypt(self._smtp_app_password).decode()
        return None

    @smtp_app_password.setter
    def smtp_app_password(self, value):
        if value:
            self._smtp_app_password = fernet.encrypt(value.encode())
        else:
            self._smtp_app_password = None
