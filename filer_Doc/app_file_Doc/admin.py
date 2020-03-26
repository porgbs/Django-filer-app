# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin
from filer.admin.fileadmin import FileAdmin
from .models import Video

admin.site.register(Video, FileAdmin)

