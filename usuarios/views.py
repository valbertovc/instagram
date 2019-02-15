# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from usuarios import models
from posts import models as posts_models


@login_required
def home(request):
    posts = posts_models.Post.objects.all()
    return render(request, '../templates/home.html', {'posts': posts})


def perfil_detail(request, pk):
    perfil = get_object_or_404(models.Perfil, pk=pk)

    if perfil.privado and not request.user.is_authenticated:
        raise PermissionDenied

    return render(request, 'perfil_detail.html', {'perfil': perfil})

