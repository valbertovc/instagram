# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        verbose_name='Usuário',
        related_name='perfil',
        on_delete=models.CASCADE,
    )
    bio = models.CharField(
        verbose_name='Bio',
        max_length=250,
        help_text='Escreva sobre você'
    )
    site = models.URLField(verbose_name='Site')
    privado = models.BooleanField(verbose_name='Privado', default=False)
    foto = models.ImageField(verbose_name='Foto', upload_to='fotos')
    seguindo = models.ManyToManyField(
        'self',
        related_name='seguidores',
    )
    criado_por = models.ForeignKey(User, related_name='perfis_criados', null=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=True)
    atualizado_por = models.ForeignKey(User, related_name='perfis_atualizados', null=True)
    atualizado_em = models.DateTimeField(auto_now=True, null=True)

    class Meta(object):
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.usuario.username  # pylint: disable=no-member
