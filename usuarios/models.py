from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    celular = models.CharField(max_length=40)