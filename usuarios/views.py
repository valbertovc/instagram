# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from usuarios import models


def home(request):
    return render(request, 'home.html')


def perfil_detail(request, pk):

    perfil = models.Perfil.objects.get(pk=pk)

    return render(request, 'perfil_detail.html', {'perfil': perfil})

