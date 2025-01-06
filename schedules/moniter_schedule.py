from celery.utils.log import get_task_logger
from beats import tasksys

logger = get_task_logger(__name__)

@tasksys.task()
def monitorTask():
    logger.info("Monitor task started")
    return True
   