from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from usuarios import models
import os


def perfil(request, perfil_id):
    perfil = get_object_or_404(models.Perfil, id=perfil_id)

    return render(
        request,
        os.path.join('usuarios', 'perfil.html'),
        {'perfil': perfil}
    )


@login_required
def perfil_list(request):
    perfis = models.Perfil.objects.all()

    return render(
        request,
        os.path.join('usuarios', 'perfil_list.html'),
        {'perfis': perfis}
    )
