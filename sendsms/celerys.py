from __future__ import absolute_import

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sendmessage.settings')

from celery import Celery

from sendsms.config import Config


app = Celery('tasks',
             broker=Config.redis_url,
             backend=Config.redis_url,
             include=['sendsms.tasks'])

app.conf.update(
    task_serializer = 'json',
    accept_content = ['json'],
    result_serializer = 'json',
    timezone = 'Asia/Shanghai',
    enable_utc = True,
)