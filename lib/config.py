import os
import yaml

class Config:
    def __init__(self):
        if not os.path.exists('config.yml'):
            genState = self.genConfig()
            if not genState:
                raise Exception("Error: Unable to generate config file")
            
        with open('config.yml', 'r') as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
            
        self.masscan = self.config['masscan']
        
    
    def genConfig(self):
        configStructure = {
            "masscan": {
                "max-rate": 100000,
                "excludefilePath": "schedules/masscan_config/exclude.conf",   
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
            