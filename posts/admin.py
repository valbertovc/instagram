# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from posts import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass
