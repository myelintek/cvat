# Copyright (C) 2018-2022 Intel Corporation
#
# SPDX-License-Identifier: MIT

import os
from .base import *

DEBUG = False

NUCLIO['HOST'] = os.getenv('CVAT_NUCLIO_HOST', 'nuclio')

# Django-sendfile:
# https://github.com/moggers87/django-sendfile2
SENDFILE_BACKEND = 'django_sendfile.backends.nginx'
SENDFILE_URL = '/'

STATIC_URL=os.getenv("PREFIX_URL","") + "/static/"
SECURE_CROSS_ORIGIN_OPENER_POLICY = None
