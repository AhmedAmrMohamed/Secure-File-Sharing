from PublicKeyEstablishment import PublicKeyEstablishment
from Encrypt import Encrypt
from FileLoader import FileLoader 
import Channels  
import time

class Sender:
    def __init__(self):
        self.channelsManger = Channels.Manger()
        self.keyestablished = self.establishKey()

    def establishKey(self):
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
        self.channelsManger.removeReciverACK()
        print(msg)
        return found
    
    def Encrypt(self, fileName):
        Encrypt(self.readFile(fileName))


        
        

    