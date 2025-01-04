import os
import subprocess
from tasks import tasksys
from lib import config
from lib import utils

conf = config.Config()

@tasksys.task()
def masscanTask():
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
        print(line.decode())
        
    IPs = utils.parseMasscanOutput('schedules/cache/masscan_output.txt')
    
        
    
    
    
    
    

    
        