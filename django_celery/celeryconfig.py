# coding: utf-8
from __future__ import unicode_literals
import djcelery
from datetime import timedelta
from celery.schedules import crontab

djcelery.setup_loader()

""""
这些配置是测试配置
"""

CELERY_QUEUES = {

    # 定时任务队列
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    # 普通任务队列
    'work_tasks': {
        'exchange': 'work_tasks',
        'exchange_type': 'direct',
        'binding_key': 'work_tasks'
    }
}

# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'upload-task',  # 指定任务名称
        'schedule': timedelta(seconds=1),  # 任务执行时间，每5秒执行一次
        'options': {
            'queue': 'beat_tasks'
        }
    },
    'task2': {
        'task': 'spider',  # 指定任务名称
        'schedule': crontab(minute='19', hour='16', day_of_week='*', day_of_month='*', month_of_year='*'),
        # 任务执行时间，每5秒执行一次
        'options': {
            'queue': 'beat_tasks'
        }
    },

}

# 设置默认的队列
CELERY_DEFAULT_QUEUE = 'work_tasks'

# 下面是老的API 现在使用autodiscover_tasks自动发现了
# 将每一个app下的tasks进行导入
CELERY_IMPORTS = (
    'app.tasks',
)

# 有些情况防止死锁
CELERYD_FORCE_EXECV = True

# 设置并发的workers数量，根据cpu的数量
CELERYD_CONCURRENCY = 4

# 任务失败允许重试
CELERY_ACKS_LATE = True

# 每个worker最多执行的任务数，超过这个就将worker进行销毁，防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务运行的最大时间，超过这个时间，task就会被kill
CELERYD_TASK_TIME_LIMIT = 12 * 30
