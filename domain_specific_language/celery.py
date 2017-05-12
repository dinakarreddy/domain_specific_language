from __future__ import absolute_import

import os
import sys
import django
from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'domain_specific_language.settings')

app = Celery('Hackathon_2017')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
from domain_specific_language import celeryconfig
app.config_from_object('domain_specific_language.celeryconfig')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

django.setup()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
