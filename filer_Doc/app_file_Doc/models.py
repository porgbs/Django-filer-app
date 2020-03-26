# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
import os

from django.db import models
from filer.models.filemodels import File


# Create your models here.
class Video(File):
    _icon = 'video'
    file_type = 'video'

    # for now...
    @classmethod
    def matches_file_type(cls, iname, ifile, request):
        filename_extensions = ['.dv', '.mov', '.mp4', '.avi', '.wmv', ]
        ext = os.path.splitext(iname)[1].lower()
        return ext in filename_extensions
