import os
import yaml

class Config:
    
    def __init__(self):
        if not os.path.exists('config.yml'):
            genState = self.genDefultConfig()
            if not genState:
                raise Exception("Error: Unable to generate config file")
            
        with open('config.yml', 'r') as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
            
        self.masscan = self.config['masscan']
        self.postgresql = self.config['postgresql']
        self.redis = self.config['redis']
        
        if os.getenv('SSREBORN_DB_HOST') is not None:
            self.postgresql['host'] = os.environ('SSREBORN_DB_HOST')
            
        if os.getenv('SSREBORN_REDIS_HOST')is not None:
            self.redis['host'] = os.environ('SSREBORN_REDIS_HOST')
        
    
    def genDefultConfig(self):
        configStructure = {
            "masscan": {
                "max-rate": 100000,
                "excludefilePath": "schedules/masscan_config/exclude.conf",   
            },
            "postgresql":{
                "host": "localhost",
                "port": 5432,
                "user": "ssreborn_user",
                "password": "ssreborn_password",
                "database": "ssreborn_db"
            },
            "redis":{
                "host": "localhost",
                "port": 5672,
            }
        }
        dump = yaml.dump(configStructure)
        try:
            with open('config.yml', 'w') as f:
                f.write(dump)
            f.close()
        except:
            return False
        
        return True

            