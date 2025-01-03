import masscan
from lib.task import tasksys

@tasksys.task
def masscan_cron():
    mas = masscan.PortScanner()
    
    rate = 100000
    excludefilePath = 'cronjob/exclude.txt'
    
    mas.scan(hosts='0.0.0.0/0',
            ports='25565',
            arguments=f'--max-rate'
            )
    
    
    
    

    
        