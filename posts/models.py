# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuarios import models as usuarios_models


class Post(models.Model):
    perfil = models.ForeignKey(usuarios_models.Perfil, related_name='posts')
    likes = models.PositiveIntegerField(default=0)
    foto = models.ImageField(upload_to='post')
    data = models.DateTimeField(auto_now_add=True)
    legenda = models.TextField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return 'Post #{} de {} em {}'.format(self.id, self.perfil, self.data)
