from celery import Celery
from celery.schedules import crontab
from lib import config

conf = config.Config()
tasksys = Celery('tasks')
tasksys.conf.timezone = 'UTC'

tasksys.conf.beat_schedule = {
    "masscan-task": {
        "task": "schedules.masscan_schedule.masscanTask",
        "schedule": crontab(minute=0, hour="0,12")
    },
    "monitor-task": {
        "task": "schedules.monitor_schedule.monitorTask",
        "schedule": crontab(minute=15)
    },
}
