from celery import Celery
from celery.schedules import crontab

tasksys = Celery()

tasksys.conf.timezone = 'UTC'

tasksys.conf.beat_schedule = {
    
}