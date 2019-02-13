# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from usuarios import models
from usuarios import forms


@admin.register(models.Perfil)
class PerfilAdmin(admin.ModelAdmin):

    form = forms.PerfilForm

    list_display = (
        'usuario_email',
        'bio',
        'site',
        'ativo'
    )

    list_filter = (
        'usuario__is_active',
        'site',
    )

    search_fields = (
        'bio',
        'site',
        'usuario__username',
    )

    date_hierarchy = 'usuario__date_joined'

    list_per_page = 10

    actions = None

    def get_form(self, request, obj=None, **kwargs):
        form = super(PerfilAdmin, self).get_form(request, obj, **kwargs)
        form.request = request
        return form

    def usuario_email(self, obj):
        return obj.usuario.email

    usuario_email.short_escription = 'E-mail do Usuário'
    usuario_email.admin_order_field = 'usuario__email'

    def ativo(self, obj):
        return obj.usuario.is_active

    ativo.boolean = True

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request, obj=None):
        return request.user.groups.filter(name='Gerenciador de Perfis').exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='Gerenciador de Perfis').exists()

    def get_changeform_initial_data(self, request):
        data = super(PerfilAdmin, self).get_changeform_initial_data(request)
        data.update({'usuario': request.user})
        return data
