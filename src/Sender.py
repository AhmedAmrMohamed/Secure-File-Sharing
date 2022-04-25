from src.PublicKeyEstablishment import PublicKeyEstablishment
from src.Encrypt import Encrypt
from src.FileLoader import FileLoader 
import src.Channels  
import time

class Sender:
    def __init__(self):
        self.channelsManger = src.Channels.Manger()

    def EstablishKey(self):
        reciverAck = self.waitForReciverACK()
        if reciverAck == True :
            PublicKeyEstablishment(sender=True)
            print('Shared Keys Established.')

    def readFile(self, fileName):
        f = FileLoader(fileName)
        msg = f.readFile()
        return msg

    def waitForReciverACK(self, timeout = 10):
        ack = self.channelsManger.checkReciverACK
        found = True
        while  ack() == False and timeout > 0:
            print('waiting for reciver...')
            timeout-=1
            time.sleep(1)
        found =  timeout > 0
        msg = f"Reciver {'found' if found else 'timeout'}."
        if found:
            self.channelsManger.removeReciverACK()
        print(msg)
        return found
    
    def Encrypt(self, fileName):
        Encrypt(self.readFile(fileName))


        
        

    