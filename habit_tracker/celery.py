from __future__ import absolute_import, unicode_literals
import os
# from enroll.models import Habit
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE','habit_tracker.settings')

app = Celery('habit_tracker')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace="CELERY")

#Celery beat settings
app.conf.beat_schedule = {
    'adding-task':{
        'task':'home_app.tasks.add_db_data',
        'schedule': 5
    },

    'send-mail-task':{
        'task':'home_app.tasks.send_mail_to_user',
        'schedule':500
    },
    'adding_to_previous_winner':{
        'task':'forum_app.tasks.add_to_previous_winner',
        'schedule':100
    }
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')