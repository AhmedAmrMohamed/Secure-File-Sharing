from src.PublicKeyEstablishment import PublicKeyEstablishment
from src.Decrypt import Decrypt
from src.FileLoader import FileLoader 
import src.Channels  
import time

class Reciver:
    def __init__(self, secretCode):
        self.secretCode = secretCode.encode('ascii')
        self.channelsManger = src.Channels.Manger()
    
    def writeFile(self, message):
        fl = FileLoader('OPENME') ##TODO: you know what...
        fl.writeFile(message)

    def EstablishKey(self):
        PublicKeyEstablishment(False, self.secretCode)
        self.channelsManger.genReciverACK()
    
    def Decrypt(self):
        msg = Decrypt(self.secretCode).message
        self.writeFile(msg)


