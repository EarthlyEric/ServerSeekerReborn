import os
import pyfiglet
from multiprocessing import Process, set_start_method

def initializeTask():
    def beat():
        os.system("celery -A tasks beat --loglevel=info")
        
    beatProcess = Process(target=beat)
    beatProcess.start()
    beatProcess.join()
    
if __name__ == "__main__":
    font = pyfiglet.Figlet(direction="auto",width=60)
    print(font.renderText("SSReborn"))
    if os.name == "nt":
        set_start_method("spawn")
    initializeTask()
