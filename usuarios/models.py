from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        related_name='perfil',
        on_delete=models.CASCADE
    )
    foto = models.ImageField(upload_to='usuarios/perfil/foto')
    bio = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.usuario.username
