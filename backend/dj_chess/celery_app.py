from celery import Celery
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_chess.settings')

app = Celery('chess')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

