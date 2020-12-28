# coding: utf-8
from __future__ import unicode_literals
from celery.task import Task
import time
from celery import Celery
from celery.utils.log import logger
from django_celery._celery import app


@app.task
def add(x, y):
    return x + y


class Upload(Task):
    name = 'upload-task'  # 给任务一个名称

    def run(self, *args, **kwargs):
        time.sleep(2)
        print('run upload task')


class scrawl(Task):
    name = 'spider'

    def run(self, *args, **kwargs):
        time.sleep(3)
        print('执行爬取任务')
