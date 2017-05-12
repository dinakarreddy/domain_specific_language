from __future__ import absolute_import
from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {
    # 'Trending projects Scheduler': {
    #     'task': 'projects_trending.tasks.compute_trending_projects',
    #     'schedule': crontab('10', '01', '05', '*', '*'),
    #     'args': (),
    #     'options': {'queue': 'cron'},
    # },
}
