import os
import subprocess
from entrypoint import conf

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
    
    return masscan
    
    
    
    
    

    
        