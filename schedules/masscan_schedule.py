import os
import subprocess
from celery.utils.log import get_task_logger
from beats import tasksys
from lib import config
from lib import utils

conf = config.Config()

logger = get_task_logger(__name__)

@tasksys.task()
def masscanTask():
    logger.info("Masscan task started")
    if not os.path.exists('schedules/cache'):
        os.makedirs('schedules/cache')
    
    args=[
        'masscan',
        '-p25565',
        '0.0.0.0/0',
        '--max-rate',
        str(conf.masscan["max-rate"]),
        '--exclude-file',
        str(conf.masscan["excludefilePath"]),
        '-oL',
        'schedules/cache/masscan_output.txt',
    ]

    masscan = subprocess.Popen(
        bufsize=1000,
        args=args,
        stdout=subprocess.PIPE
        )
    
    for line in masscan.stdout:
        logger.info(line.decode('utf-8'))
        
    IPs = utils.parseMasscanOutput('schedules/cache/masscan_output.txt')
    
    return True
        
    
    
    
    
    

    
        