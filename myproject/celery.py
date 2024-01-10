from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

app.conf.enable_UTC = False

app.conf.update(timezone = 'Africa/Nairobi')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery beat configuration
app.conf.beat_schedule = {
    
}

app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')