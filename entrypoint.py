import logging
import os
import sys
import time
import pyfiglet
import psycopg
from multiprocessing import Process, set_start_method

logging.basicConfig(level=logging.INFO, format="[%(asctime)s: %(levelname)s/StartingStageProcess] %(message)s")

def initializeTask():
    def beat():
        os.system("celery -A beats beat --loglevel=info")
        
    beatProcess = Process(target=beat)
    beatProcess.start()
    beatProcess.join()

def checkDatabase():
    logging.info("Checking database connection...")
    import lib.config
    conf = lib.config.Config()
    connection = f"host={conf.postgresql['host']} port={conf.postgresql['port']} user={conf.postgresql['user']} password={conf.postgresql['password']} dbname={conf.postgresql['database']}"
    try:
        database = psycopg.connect(
            conninfo=connection
        )
        curosr = database.cursor()
        database.autocommit = True
        curosr.execute("SELECT version();")
        version = curosr.fetchall()
        database.close()
        logging.info(f"Database connection established: {version}")
    except psycopg.OperationalError:
        logging.error("Error: Unable to connect to database")
        sys.exit(0) 
    
if __name__ == "__main__":
    # add delay to make sure the banner is displayed
    font = pyfiglet.Figlet(direction="auto",width=60)
    print(font.renderText("SSReborn"))
    time.sleep(1) 
    
    if os.name == "nt":
        set_start_method("spawn")
    checkDatabase()
    initializeTask()
