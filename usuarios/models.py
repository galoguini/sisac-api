from django.contrib.auth.models import AbstractUser
from django.db import models
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
import base64

load_dotenv()

ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY').encode()
fernet = Fernet(ENCRYPTION_KEY)

class Usuario(AbstractUser):
    celular = models.CharField(max_length=40)
    empresa_seleccionada = models.ForeignKey('empresas.Empresa', on_delete=models.SET_NULL, blank=True, null=True, related_name='usuarios_seleccionados')
    email_smtp = models.EmailField(max_length=254, blank=True, null=True)
    _smtp_app_password = models.TextField(blank=True, null=True, db_column='smtp_app_password')

    @property
    def smtp_app_password(self):
        if self._smtp_app_password:
            encrypted_password = base64.b64decode(self._smtp_app_password)
            return fernet.decrypt(encrypted_password).decode()
        return None

    @smtp_app_password.setter
    def smtp_app_password(self, value):
        if value:
            encrypted_password = fernet.encrypt(value.encode())
            self._smtp_app_password = base64.b64encode(encrypted_password).decode()
        else:
            self._smtp_app_password = None