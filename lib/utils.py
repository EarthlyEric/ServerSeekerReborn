import mcstatus

class massScannerOutputParser:
    @staticmethod
    def porcess(file:str):
        IPs = []
        try:
            with open(file, 'r') as fileHandler:
                listOfLines = fileHandler.readlines()
            fileHandler.close()
        except:
            raise Exception("Error: File not found")
        
        for line in listOfLines:
            if line.strip()[0] != "#":
                IPs.append(line.strip().split(' ',4)[3])
                
        return IPs
    

