# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# pylint: disable=no-member
import datetime
from django import forms
from django.contrib.auth.models import User

from usuarios import models


class PerfilForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        ano_atual = datetime.datetime.now().year
        ano_desde = ano_atual - 2
        self.fields['bio'].help_text = 'Escreva sobre você desde {} até hoje'.format(ano_desde)
        self.fields['usuario'].queryset = User.objects.filter(id=self.request.user.id)

    class Meta(object):
        model = models.Perfil
        fields = (
            'usuario',
            'bio',
            'site',
            'privado',
            'foto',
        )

        widgets = {
            'bio': forms.Textarea(
                attrs={
                    'placeholder': 'Texto do meu placeholder',
                }
            )
        }

        labels = {
            'bio': 'Minha história'
        }

    def clean(self):
        super(PerfilForm, self).clean()
        if not self.errors:
            site = self.cleaned_data.get('site')
            qs = models.Perfil.objects.filter(site=site)
            if self.instance.id:
                qs = qs.exclude(id=self.instance.id)
            if qs.exists():
                self.add_error('site', 'Este site já foi cadastrado.')
            if not site.startswith('https'):
                self.add_error('site', 'Adicione um site seguro.')
        return self.cleaned_data

    def save(self, commit=True):
        if not self.instance.id:
            self.instance.criado_por = self.request.user
        self.instance.atualizado_por = self.request.user
        return super(PerfilForm, self).save(commit)
